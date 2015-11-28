# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2012 Elico Corp. All Rights Reserved.
#    Author:            Andy Lu <andy.lu@elico-corp.com>
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

class stock_slowing_move(osv.osv_memory):
    _name = "stock.slowing.move"
    _description = "Compute Slowing Move"
    _columns = {

    }

    def compute_slowingmove(self, cr, uid, ids, context=None):
        """ To Import stock inventory according to products available in the selected locations.
        @param self: The object pointer.
        @param cr: A database cursor
        @param uid: ID of the user currently logged in
        @param ids: the ID or list of IDs if we want more than one
        @param context: A standard dictionary
        @return:
        """
        if context is None:
            context = {}

        slow_obj = self.pool.get('stock.slowmove')
        slow_obj.process_slowmove(cr, uid)

        mod_obj = self.pool.get('ir.model.data')

        res = mod_obj.get_object_reference(cr, uid, 'stock_report_slowmoving', 'view_stock_slowmove_tree')
        res_id = res and res[1] or False,

        return {
            'name': _('Stock Slow Moving'),
            'view_type': 'form',
            'view_mode': 'tree',
            'view_id': res_id,
            'res_model': 'stock.slowmove',
            'context': "{}",
            'type': 'ir.actions.act_window',
            'target': 'current',
            'res_id': False,
        }
        #return {'type': 'ir.actions.act_window_close'}

stock_slowing_move()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
