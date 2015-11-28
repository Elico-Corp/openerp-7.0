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
    'name': 'The POS report should have display the total without discount',
    'version': '1.0',
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'summary': 'The POS report should have display the total without discount.',
    'description': """
        * The POS report should have display the total without discount.
        * Add new column totat w/o discouont on point of sale analysis report.
        * Make POS order Salesman mandatory.
    """,
    'depends': ['point_of_sale'],
    'category': 'Sales Management',
    'sequence': 10,
    'demo': [],
    'data': [
        'point_of_sale_view.xml',
        'report/pos_order_report_view.xml',
        ],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'css': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
