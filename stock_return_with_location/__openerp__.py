# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Alex Duan <alex.duan@elico-corp.com>
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
    'name': 'Return product to specified location',
    'version': '1.0',
    'category': 'Stock',
    'sequence': 20,
    'summary': 'Return product to specified location',
    'description': """
Return with location
==================================================
When you return a product, you can specify a warehouse location you want.
Fixed: Sequence is not created for return internal picking, partial internal picking and back order of internal picking
    """,
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'images': [],
    'depends': ['stock'],
    'data': [
        'stock_return_with_location_view.xml',
    ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
