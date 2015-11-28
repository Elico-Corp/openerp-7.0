# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    LIN Yu<lin.yu@elico-corp.com>
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
from openerp.osv import fields, orm


class product_product(orm.Model):
    _inherit = 'product.product'

    def write(self, cr, uid, ids, vals, context=None):
        user_pool = self.pool.get('res.users')
        # check if user belong to portal
        # if yes, the state of product will become draft
        is_portal = user_pool.has_group(cr, uid, 'portal.group_portal')
        if is_portal:
            vals.update({'state': 'draft'})

        return super(product_product, self).write(
            cr, uid, ids, vals, context=context)
