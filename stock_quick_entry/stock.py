# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Andy Lu <andy.lu@elico-corp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it wil    l be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv, fields
import time


class StockMove(osv.osv):
    _inherit = 'stock.move'

    def product_id_change(self, cr, uid, ids, product, location_id,
                          location_dest_id, date_expected, context=None):
        context = context or {}
        result = {}

        product_obj = self.pool.get('product.product').browse(
            cr, uid, product, context=context)
        if product_obj and product_obj.uom_id:
            result['product_uom'] = product_obj.uom_id.id
        result['name'] = product_obj.name
        result['location_id'] = location_id
        result['location_dest_id'] = location_dest_id
        result['date_expected'] = date_expected
        return {'value': result}

StockMove()


class stock_picking(osv.osv):
    _inherit = 'stock.picking'
    _columns = {
        'min_date': fields.datetime('Min date'),
    }

    _defaults = {
        'min_date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
    }
stock_picking()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
