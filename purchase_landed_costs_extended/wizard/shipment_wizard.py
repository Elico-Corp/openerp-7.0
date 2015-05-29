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
from openerp.osv import orm, fields


class landed_costs_shipment_po(orm.TransientModel):

    _name = 'landed.costs.shipment.po'
    _columns = {
        'purchase_ids': fields.many2many(
            'purchase.order', 'landed_cost_shipment_group_rel',
            'shipment_id', 'po_id',
            'Purchase Order',
            domain=[('shipment_id', '=', False)]),
    }

    def link_po(self, cr, uid, ids, context=None):
        purchase_obj = self.pool.get('purchase.order')
        for assigner in self.browse(cr, uid, ids, context=context):
            po_ids = [po.id for po in assigner.purchase_ids]
            if context and context.get('active_id', False):
                # link the pos to the current shipment
                for po in purchase_obj.browse(cr, uid, po_ids, context=context):
                    po.write({'shipment_id': context.get('active_id')})
                    
        return {'type': 'ir.actions.act_window_close'}

    def confirm(self, cr, uid, ids, context=None):
        shipment_id = context.get('active_id', False)
