# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (c) 2010-Today Elico Corp. All Rights Reserved.
#    Author: LIN Yu<lin.yu@elico-corp.com>
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
    'name': ' Move Report',
    'version': '1',
    'category': 'custom',
    'sequence': 1,
    'summary': 'Move Reports',
    'description': """
Custom Reports:
===============

python lib dependancy : xlsxwriter.
 * Purchase Order
 * RFQ
 * Picking
 * Move Report ()
    """,
    'author': 'Elico Corp',
    'website': 'http://www.openerp.net.cn',
    'images' : [],
    'depends': ['stock_with_cost','product_stock_type'],
    'data': [        
        'stock_move_report/stock_move_report_view.xml',
        'security/ir.model.access.csv',
    ],
    'test': [
        
    ],
    'demo': [
       
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
