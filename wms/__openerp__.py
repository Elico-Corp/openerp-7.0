# -*- coding: utf-8 -*-
##############################################################################
#
#    wms module for OpenERP, This module allows to manage crossdocking in warehouses
#    Copyright (C) 2011 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#				Elico Corp (port to 7.0) <Contact@elico-corp.com>
#    This file is a part of wms
#
#    wms is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    wms is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Warehouse Management System',
    'version': '1.2',
    'category': 'Generic Modules/Inventory Control',
    'description': """This module is extensions to stock module""",
    'author': 'SYLEAM',
    'website': 'http://www.syleam.fr/',
    'depends': [
        'base',
        'stock',
    ],
    'init_xml': [],
    'images': [],
    'update_xml': [
        'security/ir.model.access.csv',
        #'stock_view.xml',
        # 'report_stock_view.xml',
        #'wizard/stock_to_date_view.xml',
    ],
    'demo_xml': [],
    'test': [
        #'test/wms_test01.yml',
        #'test/wms_test02.yml',
        #'test/wms_test03.yml',
        #'test/wms_test04.yml',
        #'test/wms_test05.yml',
        #'test/wms_test06.yml',
        #'test/wms_test07.yml',
        #'test/wms_test08.yml',
        #'test/wms_test09.yml',
        #'test/wms_test10.yml',
        #'test/wms_test11.yml',
        #'test/wms_test12.yml',
        #'test/wms_test13.yml',
        #'test/wms_test14.yml',
        #'test/wms_test15.yml',
        #'test/wms_test16.yml',
        #'test/wms_test17.yml',
        #'test/wms_test18.yml',
        #'test/wms_test19.yml',
        #'test/wms_test20.yml',
        #'test/wms_test21.yml',
        #'test/wms_test22.yml',
        #'test/wms_test23.yml',
        #'test/wms_test24.yml',
        #'test/wms_test25.yml',
        #'test/wms_test26.yml',
        #'test/wms_test27.yml',
        #'test/wms_test28.yml',
        #'test/wms_test29.yml',
    ],
    'installable': True,
    'active': False,
    'license': 'AGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
