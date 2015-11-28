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


class sale_project(orm.Model):
    _name = 'sale.project'
    _description = 'Sale Project'

    def _get_name(self, cr, uid, ids, name, args, context=None):
        res = {}
        for p in self.browse(cr, uid, ids, context=context):
            res[p.id] = '%s-%s-%s' % (
                p.partner_id.name, p.project_partner.name, p.project_name)
        return res

    _columns = {
        'name': fields.function(
            _get_name,
            type='char',
            method=True,
            string='Full name',
            store=False),
        'partner_id': fields.many2one(
            'res.partner', 'Customer', required=True,
            domain="[('customer', '=', True)]"),
        'project_partner': fields.many2one(
            'res.partner', 'End User', required=True,
            domain="[('customer', '=', True)]"),
        'project_name': fields.char('Project Name', required=True),
        'property_product_pricelist': fields.property(
            'product.pricelist',
            type='many2one',
            relation='product.pricelist',
            domain=[('type', '=', 'sale')],
            string="Pricelist",
            method=True,
            view_load=True,
            help="This pricelist will be used, instead of the default one,\
                  for sales to the current partner"),
        'lead_ids': fields.one2many('crm.lead', 'sale_project_id', 'Leads')
    }

    def copy(self, cr, uid, record_id, default=None, context=None):
        if default is None:
            default = {}

        default.update({'lead_ids': []})

        return super(sale_project, self).copy(
            cr, uid, record_id, default, context)

    def onchange_partner_id(self, cr, uid, ids, part, context=None):
        res = {'value': {'property_product_pricelist': False}}
        if not part:
            return res

        part = self.pool.get('res.partner').browse(
            cr, uid, part, context=context)
        pricelist = part.property_product_pricelist and\
            part.property_product_pricelist.id or False
        if pricelist:
            res['value']['property_product_pricelist'] = pricelist
        return res
