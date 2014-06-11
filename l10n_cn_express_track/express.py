# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: LIN Yu <lin.yu@elico-corp.com>
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
from openerp.addons.base_status.base_state import base_state
from openerp.osv import fields, osv
from tools.translate import _
from tools import ustr


class res_partner(osv.Model):
    _inherit = 'res.partner'
    _columns = {
        'is_deliver':  fields.boolean('Deliver?'),
    }
    _defaults = {
        'is_deliver': False,
    }


class stock_picking_express(base_state, osv.Model):
    _name = "stock.picking.express"
    # _inherit = ['mail.thread', 'ir.needaction_mixin']
    _description = "Stock Picking Express"
    _order = 'date,deliver_id'

    def _get_url_express(self, cursor, user, ids, name, arg, context=None):
        res = {}
        default_url = "http://www.kuaidi100.com/chaxun?com=%s&nu=%s"
        for express in self.browse(cursor, user, ids, context=context):
            res[express.id] = default_url % (express.deliver_id.ref,
                                             express.num_express)
        return res

    _columns = {
        'deliver_id': fields.many2one(
            'res.partner', 'Deliver Company',
            domain=[('is_deliver', '=', 1)]),
        'state': fields.selection(
            [('draft', 'Draft Quotation'),
             ('cancel', 'Cancelled'),
             ('progress', 'Sales Order'),
             ('manual', 'Sale to Invoice'),
             ('done', 'Done')],
            'Status', readonly=True,
            track_visibility='onchange', select=True),
        'partner_id': fields.many2one('res.partner', 'Partner'),
        'num_express':  fields.char('No. Express'),
        'url_express': fields.function(
            _get_url_express, method=True, type='char',
            string='Link', readonly=1),
        'date': fields.datetime('Date Deliver'),
    }
