# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Qiao Lei <qiao.lei@elico-corp.com>
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


import time
from openerp.tools.translate import _
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP, float_compare

class sale_order_line(osv.osv):
    _inherit = 'sale.order.line'
    _columns = {
        'sample': fields.boolean('Is Sample? '),                
    }
    _defaults = {
        'delay': lambda *a: 1,
    }
    #move this button to modeul "sale_botton_price"
    #if not need button price 
#===============================================================================
#     def product_id_change___(self, cr, uid, ids, sample, pricelist, product, qty=0,
#             uom=False, qty_uos=0, uos=False, name='', partner_id=False,
#             lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, context=None):
#         
#         res = super(sale_order_line,self).product_id_change( cr, uid, ids, pricelist, product, qty=qty,
#             uom=uom, qty_uos=qty_uos, uos=uos, name=name, partner_id=partner_id,
#             lang=lang, update_tax=update_tax, date_order=date_order, packaging=packaging, 
#             fiscal_position=fiscal_position, flag=flag, context=context)
# 
#         if sample:
#             res['value'].update({'price_unit':0})
#             
#         return res
#===============================================================================

    def product_uom_change(self, cursor, user, ids, sample, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, context=None):

        return True
        return self.product_id_change(cr, uid, ids, sample, pricelist, product,
                qty=qty, uom=uom, qty_uos=qty_uos, uos=uos, name=name,
                partner_id=partner_id, lang=lang, update_tax=update_tax,
                date_order=date_order, context=context)

    # ref issue :Release 0911 SO blocked if product has package default selected 
    # by chen rong at 20140918
    def product_packaging_change(self, cr, uid, ids, pricelist, product, qty=0, uom=False,
                                   partner_id=False, packaging=False, flag=False, context=None):

        res = super(sale_order_line, self).product_packaging_change(cr, uid, ids, pricelist, product, qty=qty, uom=uom,
                                   partner_id=partner_id, packaging=packaging, flag=False, context=context)

        res['warning'] = ''
        return res
    
sale_order_line()


class product_template(osv.osv):

    _inherit = 'product.template'
    _defaults = {
        'sale_delay': lambda *a: 1,
    }
