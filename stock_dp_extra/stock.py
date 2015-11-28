# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Ian Li @ Elico Corp(<http://www.openerp.net.cn>).
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

import decimal_precision as dp
from osv import fields, orm


class stock_move(orm.Model):
    _inherit = "stock.move"
    _name = "stock.move"

    _columns = {
        'price_unit': fields.float(
            'Unit Price',
            digits_compute=dp.get_precision('Stock Move'),
            help="Technical field used to record the product cost set by the\
                  user during a picking confirmation (when average price \
                  costing method is used)")
    }

    def _get_reference_accounting_values_for_valuation(self, cr, uid, move,
                                                       context=None):
        """
        Return the reference amount and reference currency representing the
        inventory valuation for this move.
        These reference values should possibly be converted before being posted
        in Journals to adapt to the primary
        and secondary currencies of the relevant accounts.
        """
        product_uom_obj = self.pool.get('product.uom')

        # by default the reference currency is that of the move's company
        reference_currency_id = move.company_id.currency_id.id

        default_uom = move.product_id.uom_id.id
        qty = product_uom_obj._compute_qty(
            cr, uid, move.product_uom.id, move.product_qty, default_uom)

        # if product is set to average price and a specific value was entered
        # in the picking wizard,
        # we use it
        if move.product_id.cost_method == 'average' and move.price_unit:
            reference_amount = qty * move.price_unit
            reference_currency_id = move.price_currency_id.id\
                or reference_currency_id

        # Otherwise we default to the company's valuation price type
        # considering that the values of the
        # valuation field are expressed in the default currency of the move's
        # company.
        else:
            if context is None:
                context = {}
            amount_unit = move.product_id.price_get(
                'standard_price', context=context)[move.product_id.id]
            reference_amount = amount_unit * qty

        return reference_amount, reference_currency_id


class stock_picking(orm.Model):
    _inherit = 'stock.picking'

    def _prepare_invoice(self, cr, uid, picking, partner, inv_type, journal_id, context=None):
        res = super(stock_picking, self)._prepare_invoice(cr, uid, picking, partner, inv_type, journal_id, context=context)
        if picking.sale_id:
            if picking.sale_id.user_id:
                res['user_id'] = picking.sale_id.user_id.id
            if picking.sale_id.section_id:
                res['section_id'] = picking.sale_id.section_id.id
        return res
