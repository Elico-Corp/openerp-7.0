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
from openerp.osv import orm, fields


class stock_warehouse(orm.Model):
    _inherit = 'stock.warehouse'
    _columns = {
        'purchase_journal_id': fields.many2one(
            'stock.journal', 'Stock Journal For Purchase')
    }


class stock_journal(orm.Model):
    _inherit = 'stock.journal'
    _columns = {

    }


class purchase_order(orm.Model):
    _inherit = 'purchase.order'

    def _prepare_order_picking(self, cr, uid, order, context=None):
        res = super(purchase_order, self)._prepare_order_picking(
            cr, uid, order, context)
        if order.warehouse_id:
            res['stock_journal_id'] = order.warehouse_id.purchase_journal_id\
                and order.warehouse_id.purchase_journal_id.id
        return res
