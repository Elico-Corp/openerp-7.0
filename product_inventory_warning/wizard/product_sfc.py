# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-Today Elico Corp. All Rights Reserved.
#    Author: Andy Lu <andy.lu@elico-corp.com>
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


from osv import fields, osv
from tools.translate import _
import time

class product_sfc(osv.osv_memory):
    _name = "run.product.inventory.dates"
    _description = "Compute Product Inventory betweend dates"
    _columns = {
                
        'from_date': fields.datetime('From', required=True), 
        'to_date': fields.datetime('To', required=True),

    }
    _defaults = {
        'from_date': lambda *a: time.strftime('%Y-%m-%d 16:00:00'),
        'to_date': lambda *a: time.strftime('%Y-%m-%d 15:59:59'),
    }

    def compute_inventory(self, cr, uid, ids, context=None):
        """ To compute inventory.
        @param self: The object pointer.
        @param cr: A database cursor
        @param uid: ID of the user currently logged in
        @param ids: the ID or list of IDs if we want more than one
        @param context: A standard dictionary
        @return:
        """
        if context is None:
            context = {}
        data = self.browse(cr, uid, ids, context=context)[0]        
        context['from_date'] = data.from_date
        context['to_date'] = data.to_date

        pi_obj = self.pool.get('product.inventory.dates')
        pi_obj.compute_inventory(cr, uid, context)

        mod_obj = self.pool.get('ir.model.data')

        res = mod_obj.get_object_reference(cr, uid, 'product_inventory_warning', 'view_product_inventory_dates_tree')
        res_id = res and res[1] or False,

        return {
            'name': _('Product Inventory between dates'),
            'view_type': 'form',
            'view_mode': 'tree',
            'view_id': res_id,
            'res_model': 'product.inventory.dates',
            'context': "{}",
            'type': 'ir.actions.act_window',
            'target': 'current',
            'res_id': False,
        }
        #return {'type': 'ir.actions.act_window_close'}

product_sfc()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
