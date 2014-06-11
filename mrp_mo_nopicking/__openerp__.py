# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (c) 2010-Today Elico Corp. All Rights Reserved.
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
    'name': 'MO for Non Standard Manufacturing Products',
    'version': '1.1',
    'author': 'Elico Corp',
    'website': 'http://www.openerp.com.cn',
    'category': 'Manufacturing',
    'sequence': 18,
    'summary': 'Manufacturing Orders with no Bill of Materials defined',
    'images': [],
    'depends': ['mrp','procurement'],
    'description': """
Manage the Non Standard Manufacturing Product with no BoM in OpenERP
====================================================================

Allows to manage the transition when implementing MRP in the project
The module allows you to create a MO without BoM for the product.
It will create a MO with only an incoming shipment and no error in procurement.


    """,
    'data': [
        'mrp_workflow.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
