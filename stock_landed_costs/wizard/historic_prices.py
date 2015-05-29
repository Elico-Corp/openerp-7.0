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
from openerp.osv import orm, fields


class historic_prices(orm.TransientModel):
    """ inherit this class to support duty zone cost prices.
    """
    _inherit = 'historic.prices'
    # _columns = {
    #     'company_id': fields.many2one(
    #         'res.company', 'Company', required=True),

    # }

    # _defaults = {
    #     'company_id': lambda self, cr, uid, c: self.pool.get('res.users').browse(
    #         cr, uid, uid, c).company_id.id,
    # }

    def action_open_window(self, cr, uid, ids, context=None):
        """
        Open the historical prices view

        rewrite this function to set the context to be able to dynamically
        select the cost to show in the list view.
        """
        res = super(historic_prices, self).action_open_window(
            cr, uid, ids, context=context)
        ctx = res.get('context').copy()
        wiz = self.browse(cr, uid, ids, context=context)[0]
        duty_zone = wiz.location_id.duty_zone_id
        if duty_zone:
            cost_type = duty_zone.price_type_id.field
        else:
            cost_type = 'standard_price'
        ctx.update(cost_type=cost_type)
        res.update(context=ctx)

        # use the inherited view
        d_obj = self.pool.get('ir.model.data')
        product_view_id = d_obj.get_object_reference(
            cr, uid,
            'stock_landed_costs',
            'LC_view_product_price_history')
        res.update(view_id=product_view_id[1])
        return res

