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


class product_product(orm.Model):
    _inherit = 'product.product'

    def _get_cubic_weight(self, cr, uid, ids, name, args, context=None):
        res = {}
        for product in self.browse(cr, uid, ids):
            res[product.id] = product.height / 100.0 * product.width / 100.0 * product.length / 100.0 * 250.0
        return res

    def onchange_hwl(self, cr, uid, ids, height, width, length, context=None):
        res = {}
        res['volume'] = height / 100.0 * width / 100.0 * length / 100.0
        return {'value': res}

    _columns = {'cubic_weight': fields.function(
                _get_cubic_weight,
                type='float', store=True, string='Cubic Weight (kg)'),
                'height': fields.float('Height (cm)'),
                'width': fields.float('Width (cm)'),
                'length': fields.float('Length (cm)'),
                }
