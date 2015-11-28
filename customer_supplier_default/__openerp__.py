# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Author: LIN Yu <lin.yu@elico-corp.com>
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
    "name" : "Un-select customer or supplier by default when creating contacts for companies.",
    "version" : "1.0",
    "author" : "Elico Corp",
    "website" : "http://www.openerp.net.cn",
    "description": """
    * Un-select customer or supplier by default when creating contacts for companies.
    * Assign "Staff" tag to contact linked to users.
    * Make Partner Checked When Converting a quotation.
    """,
    "depends" : ['base','sale_crm'],
    "category" : "Sales",
    "demo_xml" : [],
    "update_xml" : ['customer_supplier_view.xml'],
    "license": "AGPL-3",
    "active": False,
    "installable": True
}
