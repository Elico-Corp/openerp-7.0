# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Augustin Cisterne-Kaas <augustin.cisterne-kaas@elico-corp.com>
#    Eric Caudal <eric.caudal@elico-corp.com>

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

{'name': 'Base Intercompany',
 'version': '0.4',
 'category': 'Generic Modules',
 'depends': ['connector'],
 'author': 'Elico Corp',
 'license': 'AGPL-3',
 'website': 'https://www.elico-corp.com',
 'description': """
This module is the structure designed to manage Inter-company Process (ICOPS)
and allows 2 companies to create objects in each other.
This module needs to be installed with one of the following modules:
     - Base Intercompany Sale
     - Base Intercompany Stock (in development)
     - Any module which extends the Base Intercompany module

TODO: demo data to be improved.\n
Blueprint: https://blueprints.launchpad.net/multi-company/+spec/icops
""",
 'images': [],
 'demo': ['base_intercompany_demo.xml'],
 'data': ['security/ir.model.access.csv',
          'icops_model_view.xml',
          'base_intercompany_menu.xml'],
 'installable': True,
 'application': False,
 }
