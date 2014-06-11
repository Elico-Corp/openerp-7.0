# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2012 Elico Corp. All Rights Reserved.
#    Author: Yannick Gouin <yannick.gouin@elico-corp.com>
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

from osv import osv, fields

class arrange_time(osv.osv_memory):
    _name = 'arrange.time'

    _columns = {
        'dts_id' : fields.many2one('delivery.time', 'Time', required=True, domain=[('type', '=', 'dts')]),
    }

    def confirm_add(self, cr, uid, ids, context=None):
        data = self.browse(cr, uid, ids)[0]
        picking_ids = context['active_ids']
        
        picking_obj = self.pool.get('stock.picking')
        line_obj = self.pool.get('delivery.route.line')
        #TODO give warning to limit the rewrite!!
        picking_obj.write(cr, uid, picking_ids, {'dts_id':data.dts_id.id})
        for picking_id in picking_ids:
            line_obj.create(cr, uid, {'picking_id':picking_id}, context=context)
        return {
                'type': 'ir.actions.act_window_close',
                }

arrange_time()
