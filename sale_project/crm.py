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
from openerp.osv import orm, fields


class crm_lead(orm.Model):
    _inherit = 'crm.lead'
    _columns = {
        'sale_project_id': fields.many2one(
            'sale.project',
            'Sale Project',
            domain="[('partner_id', '=', partner_id)]")
    }

    def on_change_partner(self, cr, uid, ids, partner_id, context=None):
        res = super(crm_lead, self).on_change_partner(
            cr, uid, ids, partner_id, context=context)
        project_pool = self.pool.get('sale.project')
        project_ids = project_pool.search(
            cr, uid, [('partner_id', '=', partner_id)], context=context)
        res['value']['sale_project_id'] = None
        if project_ids:
            res['value']['sale_project_id'] = project_ids[-1]
        return res
