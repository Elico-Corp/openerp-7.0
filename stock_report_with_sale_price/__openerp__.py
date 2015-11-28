# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Author: LIN Yu <lin.yu@elico-corp.com>
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
    'name': 'Access Delivery Note Report with Sales Price',
    'version': '1.0',
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'summary': 'Print Delivery note report with sales price and signature',
    'description': """
         Print Delivery note report with sales price and signature.
         Add Print Delivery Note Button on stock picking.
    """,
    'depends': ['stock', 'report_multi_printout_formats'],
    'category': 'Warehouse Management',
    'sequence': 10,
    'demo': [],
    'data': [
        'stock_view.xml',
        'stock_report_with_sale_price_report.xml',
        ],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'css': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
