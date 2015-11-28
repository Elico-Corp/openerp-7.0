# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Alex Duan <alex.duan@elico-corp.com>
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
from openerp.osv import orm, osv


class stock_picking_out(orm.Model):
    _inherit = 'stock.picking.out'
    _name = 'stock.picking.out'

    def action_process(self, cr, uid, ids, context=None):
        '''inherit from stock/stock.py, check if this picking is paid.'''
        sale_obj = self.pool.get('sale.order')
        settings_obj = self.pool.get('stock.config.settings')
        for picking in self.browse(cr, uid, ids, context=context):
            #TODO: how about the DO that has no origin?
            if picking.origin:
                domain = [('name', '=', picking.origin)]
                sale_ids = sale_obj.search(cr, uid, domain, context=context)
                for sale in sale_obj.browse(cr, uid, sale_ids, context):
                    if not sale.invoiced:
                        raise osv.except_osv('Warning', 'The SO %s must be\
                              fully paid before you can process this delivery.' % picking.origin)
        return super(stock_picking_out, self).action_process(cr, uid, ids, context)
