# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time

from osv import osv, fields
from tools.translate import _
import logging
_logger = logging.getLogger(__name__)

class route_fill_picking(osv.osv_memory):
    _name = 'delivery.route.fill.picking'
    _description = 'Fill Pickings in Delivery Route'

    _columns = {
        'delivery_date': fields.date("Delivery Date"),
        'dts_id': fields.many2one('delivery.time', string="Delivery Time", domain=[('type','=','dts')]),
        'country_id': fields.many2one("res.country", 'Country'),
        'state_id': fields.many2one("res.country.state", 'State', domain="[('country_id','=',country_id)]"),
        'carrier_id': fields.many2one('delivery.carrier', string="Delivery Carrier"),
        'stock_journal_id': fields.many2one('stock.journal', string="Stock Journal"),
        
        'wo_route': fields.boolean("Find all pickings without delivery route")
    }
    _defaults = {
        'wo_route': True,
    }
    
    def default_get(self, cr, uid, fields, context=None):
        res = super(route_fill_picking, self).default_get(cr, uid, fields, context=context)
        route_obj = self.pool.get('delivery.route')
        for route in route_obj.browse(cr, uid, context.get('active_ids', []), context=context):
            res.update({'delivery_date': route.date})
            if route.driver_id.carrier_id:
                res.update({'carrier_id': route.driver_id.carrier_id.id})
            if route.dts_id:
                res.update({'dts_id': route.dts_id.id})
        return res
    
    def view_init(self, cr , uid , fields, context=None):
        if context is None:
            context = {}
        route_obj = self.pool.get('delivery.route')
        for route in route_obj.browse(cr, uid, context.get('active_ids', []), context=context):     
            if not route.state in ('draft'):
                raise osv.except_osv(_('Delivery route not in draft state !'), _('The delivery route state have to be draft to add picking lines.'))
        pass

    def get_picking_search_args(self,cr,uid,datas,context=None):
        srch = [('delivered','=',False)]
        if datas.delivery_date:
            srch += [('delivery_date','=',datas.delivery_date)]
        if datas.dts_id:
            srch += [('dts_id','=',datas.dts_id.id)]
        if datas.country_id:
            srch += [('address_id.country_id','=',datas.country_id.id)]
        if datas.state_id:
            srch += [('address_id.state_id','=',datas.state_id.id)]
            
        if datas.carrier_id:
            srch += [('carrier_id','=',datas.carrier_id.id)]
        if datas.stock_journal_id:
            srch += [('stock_journal_id','=',datas.stock_journal_id.id)]
        
        if datas.wo_route:
            cr.execute("""select id 
                            from stock_picking 
                           where state <> 'cancel'
                             and delivered = False
                             and type = 'out'
                             and id not in (select picking_id 
                                              from delivery_route_line 
                                             where state <> 'cancel')""")
            srch += [('id','in',map(lambda x: x[0], cr.fetchall()))]
        return srch

    def fill_picking(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        rec_ids = context and context.get('active_ids',[])
        route_obj = self.pool.get('delivery.route')
        line_obj = self.pool.get('delivery.route.line')
        picking_obj = self.pool.get('stock.picking')
        route_objs = route_obj.browse(cr, uid, rec_ids, context=context)
        
        for datas in self.browse(cr, uid, ids, context=context):
            srch = self.get_picking_search_args(cr,uid,datas,context=context)
            picking_ids = picking_obj.search(cr,uid,srch,context=context)
            seq = 0
            
            for picking in picking_obj.browse(cr,uid,picking_ids,context=context):
                for route in route_objs:
                    duplicate = False
                    for line in route.line_ids:
                        if picking.id == line.picking_id.id:
                            duplicate = True
                            continue
                    if duplicate:
                        continue
                    seq += 1
                    line_obj.create(cr, uid, {'sequence':seq,'route_id':route.id,'picking_id':picking.id}, context=context)

        return {'type': 'ir.actions.act_window_close'}

route_fill_picking()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
