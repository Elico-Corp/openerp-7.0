# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Alex Duan <alex.duan@elico-corp.com>
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
from openerp.osv import orm, fields, osv
import openerp.addons.decimal_precision as dp
import time


class sale_prepayment(orm.TransientModel):
    _name = 'sale.prepayment'
    _columns = {
        'journal_id': fields.many2one(
            'account.journal',
            'Journal',
            required=True),
        'amount': fields.float(
            'Amount',
            digits_compute=dp.get_precision('Account'),
            required=True),
        'is_prepayment': fields.boolean(
            'Prepayment',
            help='Check this box if you want the payment method to create a'
            "prepayment payment using the prepayment account instead of direct"
            'accounting moves linked to receivable account')
    }

    def _get_default_amount(self, cr, uid, context=None):
        sale_id = False
        sale_obj = self.pool.get('sale.order')
        if context:
            sale_id = context.get('active_id', False)
        if sale_id:
            sale_record = sale_obj.browse(cr, uid, sale_id, context)
            return sale_record and sale_record.residual or 0.0
        return 0.0

    def _get_default_journal(self, cr, uid, context=None):
        sale_id = False
        sale_obj = self.pool.get('sale.order')
        if context:
            sale_id = context.get('active_id', False)
        if sale_id:
            sale_record = sale_obj.browse(cr, uid, sale_id, context)
            payment_method = sale_record and sale_record.payment_method_id
            return payment_method and payment_method.journal_id.id or False
        return False

    def _get_default_is_prepayment(self, cr, uid, context=None):
        sale_id = False
        sale_obj = self.pool.get('sale.order')
        if context:
            sale_id = context.get('active_id', False)
        if sale_id:
            sale_record = sale_obj.browse(cr, uid, sale_id, context)
            payment_method = sale_record and sale_record.payment_method_id
            return payment_method and payment_method.is_prepayment or False
        return False

    _defaults = {
        'amount': _get_default_amount,
        'journal_id': _get_default_journal,
        'is_prepayment': _get_default_is_prepayment
    }

    def act_prepayment(self, cr, uid, ids, context=None):
        '''do the prepayment '''
        sale_obj = self.pool.get('sale.order')
        sale_id = context and context.get('active_id', False)
        sale = sale_obj.browse(cr, uid, sale_id, context=context)
        date = time.strftime('%Y-%m-%d')
        for prepay in self.browse(cr, uid, ids, context=context):
            journal = prepay.journal_id
            amount = prepay.amount
            is_prepayment = prepay.is_prepayment
            if is_prepayment is True:
                if not sale.partner_id.property_account_prepayable:
                    raise osv.except_osv(
                        'Warning',
                        "Please set this partner's payable account!")
            if amount <= 0:
                raise osv.except_osv('Warning', 'The amount must be positive!')
        if sale.payment_method_id:
            sale.payment_method_id.is_prepayment = is_prepayment
            sale.payment_method_id.journal_id = journal
        sale_obj._add_payment(
            cr, uid, sale, journal,
            amount, date, sale and sale.name or '', context=context)
        #write back the field is_prepayment
        sale_obj.write(cr, uid, sale_id, {'has_prepaid': True})
