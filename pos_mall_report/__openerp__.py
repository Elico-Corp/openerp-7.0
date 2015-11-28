# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Augustin Cisterne-Kaas <augustin.cisterne-kaas@elico-corp.com>
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
    "name": "Mall Report",
    "version": "1.0",
    "author": "Elico Corp",
    "website": "http://www.openerp.net.cn",
    "description": """
    """,
    "depends": ['point_of_sale'],
    "category": "Sales",
    "demo_xml": [],
    "update_xml": ["security/pos_mall_report_security.xml",
                   "security/ir.model.access.csv",
                   "wizard/upload_mall_file_view.xml",
                   "pos_mall_report_data.xml",
                   "pos_mall_report_view.xml",
                   "pos_mall_report_sequence.xml"],
    "license": "AGPL-3",
    "active": False,
    "installable": True
}
