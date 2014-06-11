# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Cubic ERP - Teradata SAC (<http://cubicerp.com>).
#    Copyright (C) 2013 Elico Corp (<http://www.elico-corp.com>).
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
    "name": "Delivery Routes",
    "version": "1",
    "description": """
Manage delivery routes.
=======================
Based on Cubic ERP's Delivery Routes Module\n
it add the following features:\n
* Add group Customer Service
* Add dts_id in purchase order, A purchase order with flag is_collected can have a delivery_route_line
* Improve DTS , PTS. 
* Improve Delivery carrier and driver, picker. Add color for delivery driver and picker.
* Add interface functions with other modules sales, purchase, stock
* use 3-seg daily dts/pts to arrange delivery.
""",
    "author": "Elico Corp",
    "website": "http://www.elico-corp.com",
    "category": "Stock Management",
    "depends": [
            "delivery",
            "stock",
            "hr",
            #'quality_control_elico',
        ],
    "data":[
            "security/delivery_security.xml",
            "security/ir.model.access.csv",
            "wizard/fill_picking.xml",
            "wizard/select_range_view.xml",
            "delivery_view.xml",
            "delivery_sequence.xml",
            "stock_view.xml",
            "purchase_view.xml",
            "wizard/stock_view.xml",
    ],
    "demo_xml": [ ],
    "active": False,
    "installable": True,
    "certificate" : "",
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
