# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2014 Elico Corp (<http://www.elico-corp.com>)
#    Alex Duan <alex.duan@elico-corp.com>

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

{'name': 'Purchase Landed Costs -- Duty zones',
 'version': '1.0',
 'category': 'Generic Modules',
 # depends on sale_automatic_workflow because we wanna use the sale_ids on invoice.
 'depends': ['account', 'stock',
             'purchase_landed_costs_extended',
             'anglo_saxon_account_pos', 'account_anglo_saxon',
             'sale_automatic_workflow'],
 'author': 'Elico Corp',
 'license': 'AGPL-3',
 'website': 'https://www.elico-corp.com',
 'description': """
Modification on purchase_landed_costs:
    * no invoices created for landed cost any more when the po confirmed.

Limitations:
    *
""",
 'images': [],
 'demo': [],
 'data': [
     'security/landed_cost_security.xml',
     'security/ir.model.access.csv',
     'wizard/historic_prices_view.xml',
     'wizard/stock_change_standard_price_view.xml',
     'wizard/generate_invoice_from_picking_view.xml',
     'stock_view.xml',
     # 'stock_landed_costs_data.xml'
     'product_view.xml'],
 'installable': True,
 'application': False,
 }
