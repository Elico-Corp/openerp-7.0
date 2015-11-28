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
from openerp.tools.translate import _


class mrp_product_produce(orm.TransientModel):
    _name = "mrp.product.produce"
    _inherit = "mrp.product.produce"

    _columns = {
        'product_qty': fields.float(
            'Select Quantity',
            digits_compute=dp.get_precision('Product Unit of Measure'),
            required=True),
    }

    def _get_product_qty(self, cr, uid, context=None):
        """ To obtain product quantity
        @param self: The object pointer.
        @param cr: A database cursor
        @param uid: ID of the user currently logged in
        @param context: A standard dictionary
        @return: Quantity
        <<<< rewrite this method to get the right number of product_qty
            to produce.
        """
        if context is None:
            context = {}
        prod = self.pool.get('mrp.production').browse(
            cr, uid,
            context['active_id'], context=context)
        unproduced_qty = 0
        for unproduced_product in prod.move_created_ids:
            if (unproduced_product.scrapped) or \
                    unproduced_product.state in (
                        'cancel', 'assigned', 'done') or\
                    (unproduced_product.product_id.id != prod.product_id.id):
                continue
            unproduced_qty += unproduced_product.product_qty
        return unproduced_qty or 0

    _defaults = {
        'product_qty': _get_product_qty,
    }

    def do_produce(self, cr, uid, ids, context=None):
        production_id = context.get('active_id', False)
        assert production_id, "Production Id should be specified in"
        " context as a Active ID."
        reasonable_qty = self._get_product_qty(cr, uid, context=context)
        data = self.browse(cr, uid, ids[0], context=context)
        if data.product_qty > reasonable_qty:
            raise osv.except_osv(
                _('Warning!'),
                _('You are going to produce total %s\n' +
                    'But you can only produce up to total %s quantities.') %
                (data.product_qty, reasonable_qty))
        self.pool.get('mrp.production').action_produce(
            cr, uid, production_id,
            data.product_qty, data.mode, context=context)
        return {}
