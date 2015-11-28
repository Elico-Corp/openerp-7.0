# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (c) 2010-2012 Elico Corp. All Rights Reserved.
#    Author:            Andy Lu <andy.lu@elico-corp.com>
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv
from tools.translate import _
import time
import netsvc
import decimal_precision as dp

class sale_confirm_warning(osv.osv_memory):
    _name = "sale.confirm.warning"
    _description = "Confirm Check"
    
    def _get_name(self, cr, uid, context=None):
        if context is None:
            context = {}
        return context.get('sale_name', '')
    def _get_amount(self, cr, uid, context=None):
        if context is None:
            context = {}
        return context.get('amount_total', '0.0')
    def _get_credit(self, cr, uid, context=None):
        if context is None:
            context = {}
        return context.get('credit', '0.0')
    def _get_debit(self, cr, uid, context=None):
        if context is None:
            context = {}
        return context.get('debit', '0.0')
    def _get_credit_limit(self, cr, uid, context=None):
        if context is None:
            context = {}
        return context.get('credit_limit', '0.0')                    
    _columns = {
        
        'name': fields.char('Sale Order', size=64, required=True),
        'amount_total': fields.float('Order Amount', digits_compute=dp.get_precision('Account')),
        'credit': fields.float('Total Receivable', digits_compute=dp.get_precision('Account')),
        'debit': fields.float('Total Payable', digits_compute=dp.get_precision('Account')),
        'credit_limit': fields.float('Receivable Limit', digits_compute=dp.get_precision('Account')),
    }
    _defaults = {
        'name': _get_name,
        'amount_total': _get_amount,
        'credit': _get_credit,
        'debit': _get_debit,
        'credit_limit': _get_credit_limit,
    }
   
    def do_order_confirm(self, cr, uid, ids, context=None):
        """ Confirm Order after Check warning.
        @param self: The object pointer.
        @param cr: A database cursor
        @param uid: ID of the user currently logged in
        @param ids: List of fields for which we want default values
        @param context: A standard dictionary
        @return: A dictionary.
        """
    
        if context is None:
            context = {}

        record_id = context and context.get('sale_id', False) or False
        if record_id:
            self.pool.get('sale.order').pre_action_wait(cr, uid , [record_id,])
        return {'type': 'ir.actions.act_window_close'}

sale_confirm_warning()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
