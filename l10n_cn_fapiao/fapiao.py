# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (c) 2010-Today Elico Corp. All Rights Reserved.
#    Author: Chen Puyu <chen.puyu@elico-corp.com>
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


class fapiao(orm.Model):
    _name = "fapiao"
    _inherit = ['mail.thread']
    _order = "fapiao_date desc"

    _columns = {
        'fapiao_type': fields.selection(
            [('customer', 'Customer'), ('supplier', 'Supplier'),
             ('customer_credit_note', 'Customer Credit note'),
             ('customer_credit_note', 'Customer Credit note')],
            'Fapiao Type', required=True),
        'tax_type': fields.selection(
            [('13%', '13%'), ('17%', '17%'),
             ('normal', 'normal'), ('no_tax', 'no tax')],
            'Tax Type', required=True),
        'partner_id': fields.many2one('res.partner', 'Partner', required=True),
        'fapiao_number': fields.integer(string="Fapiao Number", required=True),
        'fapiao_date': fields.date(string="Fapiao Date", required=True),
        'reception_date': fields.date(string="Reception Date"),
        'amount_with_taxes': fields.float('Fapiao total amount',
                                          required=True),
        'invoice_ids': fields.many2many('account.invoice', string="Invoices"),
        'tag_ids': fields.many2many('fapiao_tag', string="Tags"),
        'notes': fields.text(string="Notes"),
    }

    _defaults = {
        'tax_type': 'normal',
    }


class fapiao_tag(orm.Model):
    _name = 'fapiao_tag'

    _columns = {
        'name': fields.char("Name"),
    }


class account_invoice(orm.Model):
    _inherit = 'account.invoice'

    _columns = {
        'fapiao_ids': fields.one2many('fapiao', 'invoice_ids', 'Fapiao'),
    }
