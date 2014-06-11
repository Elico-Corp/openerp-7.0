# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (c) 2010-Today Elico Corp. All Rights Reserved.
#    Author: Chen Puyu <chen.puyu@elico-corp.com>
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
    'name': 'Chinese Fapiao Management',
    'version': '0.1',
    'category': 'Accounting',
    'sequence': 19,
    'summary': 'Chinese Fapiao Management and link with OpenERP Invoice',
    'description': """

* "Fapiao" is an official invoice in China, printed in a separate official software.
* This module allows the users to manage all emitted and received "fapiao"  as object in OpenERP. It has no impact on accounting books and doesnot (yet) integrate with external official software. It adds new submenu called Fapiao under the menu Accounting.

The procedure to follow for the fapiao management is as below:
* Step 1: A fapiao is received or emitted
* Step 2: The document can be scanned as image
* Step 3: A new fapiao is created in OpenERP
* Step 4: The scanned document is uploaded to the newly created object as attachment.
* Step 5: Fapiao allocation to invoice: Fapiao and OpenERP invoices can be linked to each other
    """,
    'author': 'Elico Corp',
    'website': 'http://www.openerp.net.cn',
    'images': [],
    'depends': ['account'],
    'data': [
        'fapiao_view.xml',
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
