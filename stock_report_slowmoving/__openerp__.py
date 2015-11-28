#-*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (c) 2010-today Elico Corp. All Rights Reserved.
#    Author:            Andy Lu <andy.lu@elico-corp.com>
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Slow moving stock report in a night scheduler',
    'version': '1.0',
    'category': 'Custom',
    'description': """

	This is a slow-moving analysis report aimed to classified the products according to their stock rotation
	in order to identify slow-moving products. 
	Features
	- Add a scheduler has been added to create a table nightly
	- This report is based on webkit
	- only displays references with stock
     """,
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'depends': ['base', 'product', 'stock', 'sale', 'purchase', 'mrp',
        'report_webkit',
        'base_headers_webkit'],
    'init_xml': [],
    'update_xml': [
        'security/ir.model.access.csv',
        'stock_slowmoving_view.xml',
        'stock_slowmoving_report_view.xml',
        'wizard/stock_slowing_move_view.xml',
    ],
    'demo_xml': [], 
    'test': [],
    'installable': True,
    'active': False,
    'certificate': '',
}
