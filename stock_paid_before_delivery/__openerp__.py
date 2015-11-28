# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Alex Duan <alex.duan@elico-corp.com>
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
    'name': 'Must be paid before delivery',
    'version': '1.0',
    'author': 'Elico Corp <alex.duan@elico-corp.com>',
    'depends': ['stock'],
    'category': 'Generic Modules/Others',
    'description': """
This module modify the process of delivery.
=========================================
The DO must be paid before it can be deliveried.
      """,
    'data': ['res_config_view.xml'],
    'auto_install': False,
    'installable': True,
    'active': True,
}
