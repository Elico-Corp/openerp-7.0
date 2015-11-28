# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
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
    'name' : 'Approvement for Plan',
    'version' : '1.0',
    'author': 'Elico Corp',
    'website': 'www.openerp.net.cn',
    'category' : 'Generic Modules/Production',
    'depends' : ['procurement', 'sale', 'l10n_cn_apem_procurement'],
    'description': """
        Support a new field supply_method for planner to confirm.
        Default value is from product when confirm the sale order.
    """,
    'init_xml': [],
    'update_xml': [
        'procurement_supply_ext_views.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
    'certificate': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
