# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Jean LELIEVRE <jean.lelievre@elico-corp.com>
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

class product_product(osv.osv):
    _name = "product.product"
    _inherit = "product.product"
    
    def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):

        if context and context.get('supplier_id', False):
            product_limit = self.pool.get('res.partner').read(cr,uid,context['supplier_id'],['supplier_product_limit'])['supplier_product_limit']
            if product_limit:
                #    ids = []
                cr.execute("SELECT distinct(product_id) FROM product_supplierinfo where name = %s" % (context.get('supplier_id')))
                ids = [x[0] for x in cr.fetchall()]
                args.append(('id', 'in', ids))
                order = 'default_code'
        return super(product_product, self).search(cr, uid, args, offset=offset, limit=limit, order=order, context=context, count=count)

product_product()

class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'

    _columns = {
        'supplier_product_limit':fields.boolean("Control Supplier Search", help="""If checked, allows you to search only the product in this supplier )"""),
    }

    _defaults = {
        'supplier_product_limit': True,
    }