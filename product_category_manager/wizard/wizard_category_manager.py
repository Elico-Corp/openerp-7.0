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
from openerp.osv import osv, fields
from openerp.tools.translate import _


class wizard_category_manager(osv.osv_memory):
    _name = "wizard.category.manager"
    _columns = {
        'categ_from': fields.many2one(
            'product.category', 'Category Origin'),
        'categ_to': fields.many2one(
            'product.category', 'Category Destination')
    }

    def assign(self, cr, uid, ids, context=None):
        assert len(ids) == 1
        wizard = self.browse(cr, uid, ids[0], context=context)
        categ_ids = []
        if wizard.categ_from:
            categ_ids.append((3, wizard.categ_from.id))
        if wizard.categ_to:
            categ_ids.append((4, wizard.categ_to.id))
        if not categ_ids:
            raise osv.except_osv(
                _('Warning!'),
                _('Please select at least one category'))
        product_pool = self.pool.get('product.product')
        product_pool.write(
            cr, uid, context['active_ids'],
            {'categ_ids': categ_ids})

    def remove_all(self, cr, uid, ids, context=None):
        product_pool = self.pool.get('product.product')
        product_pool.write(
            cr, uid, context['active_ids'], {'categ_ids': [(5,)]})
