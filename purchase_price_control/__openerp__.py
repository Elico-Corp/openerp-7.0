# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Yannick Gouin <yannick.gouin@elico-corp.com>
#    Author: Andy Lu <andy.lu@elico-corp.com>
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
    'name': 'Purchase Enhancements',
    'version': '1.0',
    'category': 'Purchase',
    'sequence': 19,
    'summary': 'Allow several enhancements on purchase management',
    'description': """
Purchase management enhancements
==================================================
** 2 new check for price control: one at supplier level, on at Product level: both False/Unchecked means user cannot change the price in PO Line

** New Price list calculation scheme based on the UoP: if chosen, user needs only to input the "Surcharge" field and price is refered to UoP.

** Efficient Search list per PO line

** Improved Header addresses.


    """,
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'images' : [],
    'depends': ['product', 'purchase'],
    'data': [
             
        'security/ir.model.access.csv',
        'purchase_view.xml',
    ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
