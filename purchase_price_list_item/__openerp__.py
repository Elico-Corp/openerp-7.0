# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Jean LELIEVRE <jean.lelievre@elico-corp.com>
#            Andy LU<andy.lu@elico-corp.com>
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
    'name': 'Purchase Price List Item',
    'version': '1.0',
    'category': 'Purchase',
    'sequence': 19,
    'summary': 'Purchase Price List Item',
    'description': """ 
Improve purchase price managment
================================

    * In Purchase List Item, the price is fixed based on price_surchage if base is 'fixed on UOP'
    * If 'fixed on UOP', if product UOP change, the price list price will be change automtically.
    * Add field 'Qty on Hand', and 'Stock Values' for product
    * Add field 'Qty on Hand', 'Stock Values', UOP in product list view

     """,
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'images' : [],
    'depends': ['purchase'],
    'data': [
             'purchase_view.xml',
    ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}