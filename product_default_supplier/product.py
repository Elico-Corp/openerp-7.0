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

from openerp.osv import fields, osv
from openerp import SUPERUSER_ID


class product_default_supplier_line(osv.osv):
    _name = 'product.default.supplier.line'

    _product_type = [('product', 'Stockable Product'),
                     ('consu', 'Consumable'),
                     ('service', 'Service')]
    _columns = {
        'name': fields.char('Name', size=24),
        'product_category_id': fields.many2one('product.category',
                                               'Product Category',
                                               required=True),
        'partner_id': fields.many2one('res.partner',
                                      'Supplier',
                                      domian=[('supplier', '=', True)],
                                      required=True),
        'company_id': fields.many2one('res.company', 'Company',
                                      required=True),

        'product_type': fields.selection(_product_type, 'Product Type',
                                         required=True),
    }
    _defaults = {
        'product_type': lambda *a: 'product',
    }
    _sql_constrants = [
        ('record_uniq', 'unique (partner_id,company_id,product_category_id)',
         'Supplier and  Product Category repeat')
    ]
product_default_supplier_line()


class res_company(osv.osv):
    _inherit = 'res.company'
    _columns = {
        'pdt_def_sup_lines': fields.one2many(
            'product.default.supplier.line',
            'company_id',
            'Product Default supplier'),
    }
res_company()


class product_product(osv.osv):
    _inherit = 'product.product'

    def create(self, cr, uid, default, context=None):
        """
        when create product, set the default supplier info
        """

        p_id = super(product_product, self).create(cr, uid, default,
                                                   context=context)
        company_pool = self.pool.get('res.company')
        supplierinfo_pool = self.pool.get('product.supplierinfo')

        if not p_id:
            return p_id

        product = self.browse(cr, uid, p_id)
        company = product.company_id or False

        sup_lines = []
        if company:
            sup_lines = company.pdt_def_sup_lines
        else:
            all_company_ids = company_pool.search(cr, SUPERUSER_ID, [])
            all_company = company_pool.browse(cr, SUPERUSER_ID,
                                              all_company_ids)
            for c in all_company:
                sup_lines += c.pdt_def_sup_lines

        for line in sup_lines:
            if ((product.categ_id.parent_left
                 >= line.product_category_id.parent_left)
                    and (product.categ_id.parent_right
                         <= line.product_category_id.parent_right)
                    and product.type == line.product_type):

                supplierinfo_pool.create(cr, SUPERUSER_ID, {
                    'product_id': p_id,
                    'name': line.partner_id.id,
                    'min_qty': 1,
                    'delay': 1,
                    'company_id': line.company_id.id}
                )

        return p_id

product_product()
