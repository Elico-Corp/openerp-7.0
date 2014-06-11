# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author:    Andy Lu <andy.lu@elico-corp.com>
#               LIN Yu <lin.yu@elico-corp.com>
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

{
    'name': 'Product Inventory Warning',
    'version': '1',
    'category': 'Product',
    'sequence': 1,
    'summary': 'Product Inventory Warning',
    'description': """
Product Inventory Warning
==================================================

Add a wizard to calculate the QTY of product.
    """,
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'images' : [],
    'depends': ['product', 'product_stock_type','product_separate_cost','stock_with_cost'],
    'data': [
        'product_view.xml',
        'wizard/product_qty_view.xml',
        'wizard/product_sfc_view.xml',
        'security/ir.model.access.csv',
    ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
