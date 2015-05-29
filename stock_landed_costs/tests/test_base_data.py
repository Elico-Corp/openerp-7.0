# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2014 Elico Corp (<http://www.elico-corp.com>)
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
from openerp.test.common import TransactionCase


class TransactionCaseBaseData(TransactionCase):
    def setUp(self):
        cr, uid = self.cr, self.uid
        # base objects
        self.picking_obj = self.registry('stock.picking')
        self.move_obj = self.registry('stock.move')
        self.location_obj = self.registry('stock.location')
        self.model_data_obj = self.registry('ir.model.data')

        # base data for this module's test

        # locations
        self.duty_free_locaton_id = self.model_data_obj.get_object_reference(
            cr, uid, 'stock_location', 'stock_location_duty_free_zone_001')[1]
        self.duty_paid_location_id = self.model_data_obj.get_object_reference(
            cr, uid, 'stock_location', 'stock_location_duty_paid_zone_001')[1]
        self.transit_location_id = self.model_data_obj.get_object_reference(
            cr, uid, 'stock_location', 'stock_location_transit')[1]

        # company
        self.company_id = self.model_data_obj.get_object_reference(
            cr, uid, 'res.company', 'base.main_company')[1]

        # picking
        self.picking_id = self.picking_obj.create(
            cr, uid, self.prepare_base_picking('direct'))

    def prepare_base_picking(self, type):
        '''prepare the base picking'''
        return {
            'name': 'Picking1',
            'state': 'auto',
            'type': type,
            'move_type': 'direct',
            'invoice_state': 'none',
            'company_id': self.company_id
        }

    def tearDown(self):
        self.cr.rollback()
