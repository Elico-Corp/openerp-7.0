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
    'name': 'Sales Quotation Improve',
    'version': '0.1',
    'category': 'Base',
    'description': """Sales quotation process is an important part of the
    sales process and being able to number all sales quotations and keep
    track of them is essential to the business:
    Successive new sales quotations should be stored in OpenERP.
    Related sales quotations should be linked together so that we can trace
    the history with the customer and final sales order.
    A sales order created from a sales quotation should be linked to the last
    sales quotation.
    Sales Quotations and Sales Order should have different numbering sequences.
    When a sales order is to be set as draft and revalidated (for example to
    recreate the stock pickings), original Sales Order number should be kept.
    Sales Quotation status should allow to identify in which states is a
    quotation (lost and converted).""",
    'author': 'Elico Corp',
    'website': 'http://www.openerp.net.cn',
    'depends': ['sale', 'sale_crm', 'sale_project', 'sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/make_quotation_view.xml',
        'sale_quotation_data.xml',
        'sale_quotation_view.xml',
        'sale_order_view.xml',
        'crm_view.xml',
        # 'report/sale_report_view.xml',
    ],
    'test': [],
    'installable': True,
    'active': False,
    'certificate': '',
}
