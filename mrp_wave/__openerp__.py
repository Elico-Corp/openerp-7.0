# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Yannick Gouin <yannick.gouin@elico-corp.com>
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
    'name': 'MRP Wave Scheduler',
    'version': '1.0',
    'category': 'Stock',
    'sequence': 19,
    'summary': 'MRP Wave Scheduler',
    'description': """
Stock Big Scheduler + AUTO/FORCE MO (For bundle products with BOM)
==================================================
* Calculate scheduler based on DTS, PTS.
* During scheulder, create and validate mo based on product definition.
* Create  & Update Scheduler Staus message with message group 'scheduler'.
* Launch scheduler in threads when a scheduler is not started.
* Option to stop / kill the scheduler threads.
    """,
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'images' : [],
    'depends': ['product','stock','delivery_plan'],
    'data': [
        'wizard/scheduler.xml',
    ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
