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


class stock_picking(orm.Model):
    _inherit = 'stock.picking'

    _columns = {
        'carrier_website': fields.related(
            'carrier_id', 'partner_id', 'website',
            type='char', string="Carrier website"),
        'tracking_website': fields.related(
            'carrier_id', 'tracking_website',
            string='Tracking Website Url', type='char'),
    }


class stock_picking_out(orm.Model):
    _inherit = 'stock.picking.out'

    _columns = {
        'carrier_website': fields.related(
            'carrier_id', 'partner_id', 'website',
            type='char', string="Carrier website"),
        'tracking_website': fields.related(
            'carrier_id', 'tracking_website',
            string='Tracking Website Url', type='char'),
    }


class delivery_carrier(orm.Model):
    _inherit = 'delivery.carrier'

    _columns = {
        'tracking_website': fields.char(
            'Tracking Website Url')
    }
