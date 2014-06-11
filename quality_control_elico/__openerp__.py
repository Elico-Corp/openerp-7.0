# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
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
    'name': 'Quality Management',
    'version': '1.0',
    'category': 'Quality Management',
    'sequence': 19,
    'summary': 'Process Stock Picking / Move by QC user / manager',
    'description': """
Quality Management
==================
Process Stock Picking / Move by QC user / manager\n
* Add Group QC Manager \ QC user
* Link QC location with manual chained picking. 
* Check when location update
* Check when update push flow
* Add a flag qc_picking to picking when it is a qc picking.

    """,
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'images' : [],
    'depends': ['stock', 'stock_location'],
    'data': [
        'security/qc_security.xml',
        'security/ir.model.access.csv',
        'stock_view.xml',
    ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: