# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Elico Corp <contact@elico-corp.com>
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
    'name': 'Account Prepayment',
    'version': '1.0',
    'category': 'Account',
    'sequence': 19,
    'summary': 'Account Prepayment',
    'description': """
Prepayment Process with payment wizard
==================================================
Create the possibility to generate the prepayment  directly from the payment wizard:
** add the prepayment account in the partner

** add a check box in the payment form Prepayment: if checked the prepayment account in the partner will be chosen

** Usage for Supplier:
Normal Payment (Choose the invoice in the payment form)
AP 		debit 	3000
Bank 	Credit 	-3000


** Prepayment Move (At money reception, use the payment form with prepayment and select no invoice). It creates:
Prepayment 		debit 	1000
Bank 			Credit 	-1000

** Create an Invoice
AP				Credit 	-3000
Sales 			Debit 	3000

** New Payment (after invoice is created)
Use the payment form (no prepayment option and select the invoice and already existing Prepayment move)
Prepayment 		Credit 	-1000
AP	 			Debit 	3000
Bank			Credit	-2000

    """,
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'images' : [],
    'depends': ['account', 'account_voucher'],
    'data': [
        'account_view.xml',
    ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
