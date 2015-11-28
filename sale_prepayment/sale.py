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
from collections import Iterable


class sale_order(orm.Model):
    _inherit = 'sale.order'

    _columns = {
        'has_prepaid': fields.boolean('Has been Prepaid', readonly=True),

    }

    _defaults = {
        'has_prepaid': False
    }

    def copy(self, cr, uid, id, default=None, context=None):
        if default is None:
            default = {}
        default['has_prepaid'] = False
        return super(sale_order, self).copy(cr, uid, id,
                                            default, context=context)

    def automatic_payment(self, cr, uid, ids, amount=None, context=None):
        """ If this quotation hasn't been prepaid
        Create the payment entries to pay a sale order, respecting
        the payment terms.
        If no amount is defined, it will pay the residual amount of the sale
        order.
        Otherwise do nothing.
        rewrite the function in sale_automatic_payment"""
        if not ids:
            return False
        if isinstance(ids, Iterable):
            assert len(ids) == 1, "one sale order at a time can be paid"
            ids = ids[0]
        sale = self.browse(cr, uid, ids, context=context)
        if sale.has_prepaid is False:
            return super(sale_order, self).automatic_payment(
                cr, uid, ids, amount=amount, context=context)
        return True

    def _prepare_payment_move_line(self, cr, uid, move_name, sale, journal,
                                   period, amount, date, context=None):
        """ """
        debit_line, credit_line = super(
            sale_order, self)._prepare_payment_move_line(
            cr, uid, move_name, sale, journal, period, amount,
            date, context=context)
        partner_obj = self.pool.get('res.partner')
        partner_id = sale.partner_invoice_id or\
            sale.partner_id or False
        partner = partner_obj._find_accounting_partner(partner_id)
        debit_line['partner_id'] = partner.id
        credit_line['partner_id'] = partner.id
        return debit_line, credit_line
