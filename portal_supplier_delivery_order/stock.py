# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    LIN Yu <lin.yu@elico-corp.com>
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


class stock_picking(orm.Model):
    _inherit = 'stock.picking'

    _columns = {
        'sales_man': fields.many2one(
            'res.users', 'Source product', ondelete='cascade'),
    }

    #back order, copy should copy sales man
    # def copy_data(self, cr, uid, id, default=None, context=None):
    #     if default is None:
    #         default = {}
    #     default['sales_man'] = False
    #     return super(sale_order, self).copy_data(cr, uid, id,
    #                                              default=default,
    #                                              context=context)


class stock_picking_out(orm.Model):
    _inherit = 'stock.picking.out'

    _columns = {
        'sales_man': fields.many2one(
            'res.users', 'Portal Sales', ondelete='cascade'),
    }


class sale_order(orm.Model):
    _inherit = 'sale.order'

    def _prepare_order_picking(self, cr, uid, order, context=None):
        picking_vals = super(sale_order, self)._prepare_order_picking(
            cr, uid, order, context=context)
        picking_vals['sales_man'] = order.user_id and order.user_id.id or False
        return picking_vals
