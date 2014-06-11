# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#     Jon Chow <jon.chow@elico-corp.com>
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

from openerp.osv import orm, fields


class payment_method(orm.Model):
    _inherit = "payment.method"
    _columns = {
        'is_prepayment': fields.boolean('Prepayment', help='Check this box if you want the payment method to create a prepayment payment using the prepayment account instead of direct accounting moves linked to receivable account'),
    }
    _defaults={       
    }
    
    
class sale_order(orm.Model):
    _inherit = 'sale.order'
    def _prepare_payment_move_line(self, cr, uid, move_name, sale, journal,
                                       period, amount, date, context=None):
        debit_line, credit_line = super(sale_order, self)._prepare_payment_move_line(cr, uid, move_name, sale, journal,
                                        period, amount, date, context=context)
        
        if sale.payment_method_id and sale.payment_method_id.is_prepayment:
            credit_line.update({'account_id': sale.partner_id.property_account_prereceivable.id,})
            
        return debit_line, credit_line
    
    
    
 # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
  
