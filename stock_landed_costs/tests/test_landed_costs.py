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
from test_base_data import TransactionCaseBaseData


class TestLandedCosts(TransactionCaseBaseData):
    '''Tests for landed costs
    Demo data:
        1 stock picking with landed costs:
            * distributed by volume
            * distributed by value
            * distributed by quantity
            
        2 stock moves with landed costs:
            * distributed by volume
            * distributed by value
            * distributed by quantity
    '''
    def setUp(self):
        # prepare the stock moves for testing.
        self.move_id1 = self.move_obj.create({
            'name': 'Move1',
            'product_id': self.product_id
        })

    def StockMove_LandingCostField(self):
        # Environment:
        #   A stock move of a stock picking with landed costs
        # Action:
        #   compute the landing cost
        # Output:
        #   the right landing cost
        pass
