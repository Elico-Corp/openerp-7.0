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

class select_line_range(osv.osv_memory):
    _name = 'select.line.range'

    _columns = {
        'dts_id' : fields.many2one('delivery.time', 'Time', required=True, domain=[('type', '=', 'dts')]),
            }

    def show(self, cr, uid, ids, context=None):
        data = self.browse(cr, uid, ids)[0]
        route_obj = self.pool.get('delivery.route')
        route_ids = route_obj.search(cr, uid, [
                    ('dts_id', '=', data.dts_id.id),
                    ], context=context)
        return {
                'type': 'ir.actions.act_window',
                'res_model':'delivery.route.line',
                'view_type':'tree',
                'view_mode':'kanban,form',
                # how to use domain "in" 
                'domain':'["|",("route_id","in",%s),("route_id","=",None)]' % str(route_ids),
                }

select_line_range()
