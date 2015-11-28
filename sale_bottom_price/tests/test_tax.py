# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2014 Elico Corp (<http://www.elico-corp.com>)
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
from openerp.tests.common import TransactionCase


class TestTax(TransactionCase):
    '''Tests for tax'''

    def setUp(self):
        super(TestTax, self).setUp()
        self.imd = self.registry('ir.model.data')
        so_obj = self.registry('sale.order')
        tax_obj = self.registry('account.tax')
        self.invoice_obj = self.registry('account.invoice')

        # get test SO
        so_id = self.imd.get_object_reference(self.cr, self.uid, 'sale', 'sale_order_5')[-1]
        self.so = so_obj.browse(self.cr, self.uid, so_id)

        # get testing tax
        tax_ids = tax_obj.search(
            self.cr, self.uid, [('type_tax_use', '=', 'sale'), ('amount', '>', 0)])
        tax = tax_obj.browse(self.cr, self.uid, tax_ids[0])

        # add tax to every sale order line.
        for line in self.so.order_line:
            line.write({
                # 'discount': 0,
                'final_price': line.price_unit * (100 - line.discount) / 100,
                'tax_id': [(4, tax.id)],
                'product_uom_qty': 123
            })
        # create invoice on sale order
        self.so.write({'order_policy': 'prepaid'})

        # confirm the sale order
        self.so.action_button_confirm()

        # create the invoice for the sale order
        res = so_obj.manual_invoice(self.cr, self.uid, [self.so.id])
        self.inv_id = res.get('res_id')
        if self.inv_id:
            self.inv = self.invoice_obj.browse(self.cr, self.uid, self.inv_id)

    def test_invoice_rounding(self):
        '''test if the tax amount of Sale order is the same as invoice's.
        For more details please see issue:2574, different tax between the SO and ivnoice.'''
        if self.inv_id:
            self.assertEqual(self.inv.amount_tax, self.so.amount_tax)