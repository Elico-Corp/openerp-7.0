# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Qiao Lei <qiao.lei@elico-corp.com>
#    Author: Alex Duan <alex.duan@elico-corp.com> 2014-11-27
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
    'name': 'Sales Bottom Price Management',
    'version': '2.0',
    'category': 'Sales Management',
    'summary': 'Sales Bottom Price Management',
    'description': """ Sales Bottom Price Management  """,
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'images': [],
    'depends': [
        'sale_sample',
        'sale',
        'product',
        'sale_stock',
        'account',
        'stock',
        'account_accountant'],
    'data': ['sale_view.xml'],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
