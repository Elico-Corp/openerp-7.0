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

from osv import osv, fields
from tools.translate import _

class res_partner(osv.osv):
    _inherit = 'res.partner'

    _columns = {
        'property_account_prepayable': fields.property(
            'account.account',
            type='many2one',
            relation='account.account',
            string="Account Payable (Prepayment)",
            view_load=True,
            domain="[('type', '=', 'payable')]",
            help="This account will be used instead of the default one as the prepayment payable account for the current partner",
            required=True),
        'property_account_prereceivable': fields.property(
            'account.account',
            type='many2one',
            relation='account.account',
            string="Account Receivable (Prepayment)",
            view_load=True,
            domain="[('type', '=', 'receivable')]",
            help="This account will be used instead of the default one as the prepayment receivable account for the current partner",
            required=True),
    }

class account_voucher(osv.osv):
    _inherit = "account.voucher"
    
    _columns = {
        'use_prepayment_account': fields.boolean('Use Prepayment account', help="Check this if you want to input a prepayment on the prepayment accounts."),
    }
    _defaults = {
        'use_prepayment_account': False,
    }
    
    def writeoff_move_line_get(self, cr, uid, voucher_id, line_total, move_id, name, company_currency, current_currency, context=None):
        line_vals = super(account_voucher, self).writeoff_move_line_get(cr, uid, voucher_id, line_total, move_id, name, company_currency, current_currency, context=context)
        if line_vals:            
            account_id = False
            voucher_brw = self.pool.get('account.voucher').browse(cr,uid,voucher_id,context)
            if voucher_brw.use_prepayment_account:
                if voucher_brw.payment_option == 'with_writeoff':
                    account_id = voucher_brw.writeoff_acc_id.id
                elif voucher_brw.type in ('sale', 'receipt'):
                    if not voucher_brw.partner_id.property_account_prereceivable:
                        raise osv.except_osv(_('Unable to validate payment !'), _('Please configure the partner Prereceivable Account at first!'))
                    account_id = voucher_brw.partner_id.property_account_prereceivable.id
                else:
                    if not voucher_brw.partner_id.property_account_prepayable:
                        raise osv.except_osv(_('Unable to validate payment !'), _('Please configure the partner Prepayable Account at first!'))
                    account_id = voucher_brw.partner_id.property_account_prepayable.id
                if account_id:                    
                    line_vals['account_id'] = account_id
        return line_vals
account_voucher()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
