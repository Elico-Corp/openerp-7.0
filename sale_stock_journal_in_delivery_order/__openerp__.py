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
{
    'name': 'Sale stock journal in delivery order',
    'version': '1.0',
    'author': 'Elico Corp <alex.duan@elico-corp.com>',
    'depends': ['stock', 'sale_stock'],
    'category': 'Generic Modules/Others',
    'description': """
This module add field on warehouse and pass from SO to DO..
=========================================
A stock journal should be assigned per warehouse and
    used in the DO created from the SO.
Add field at warehouse level (not mandatory)
Modify the method to create the stock picking to include the
    journal from shop/warehouse (if there is one)
      """,
    'data': ['stock_view.xml'],
    'auto_install': False,
    'installable': True,
    'active': True,
}
