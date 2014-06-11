# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Lin Yu <lin.yu@elico-corp.com>
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
    'name': 'l10n_cn_express_track',
    'version': '1.0',
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'summary': '',
    'description' : """
        Chinese Express Track
* Track your Express Delivery (快递/"kuaidi") in China with OpenERP. More than 100 companies supported (DHL, SF, UPS, EMS, etc...)!

* With this module, users can get a link directly in the OpenERP by entering tracking numbers and track the real-time delivery status by clicking this link.

* To install this module, module web_url is needed, available here: http://www.emiprotechnologies.com/openerp/module7/

* Next version will include a full API with state management.

    """,
    'depends': ['web_url','base'],
    'category': '',
    'sequence': 10,
    'demo': [],
    'data': [
        'express_view.xml',
        ],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'css' : [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
