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
from osv import fields, orm
from tools.translate import _


class crm_lead(orm.Model):
    """ CRM Lead Case """
    _inherit = "crm.lead"
    _rec_name = 'nao_name'

    _columns = {
        'nao_name': fields.char(
            'NAO Reference', size=64, required=False, readonly=True,
            states={'draft': [('readonly', True)]}),
        'order_ids': fields.one2many(
            'sale.order', 'file_number', 'Sale Orders',
            readonly=True, required=False),
        'sale_project_id': fields.many2one(
            'sale.project', 'Sale Project', required=False,
            domain="['|',('partner_id','=',partner_id),\
                    ('partner_id','=',False)]"
        ),
    }

    _defaults = {
        'nao_name': lambda obj, cr, uid, context: obj.pool.get(
            'ir.sequence').get(cr, uid, 'crm.lead.nao'),
    }

    def copy(self, cr, uid, id, default=None, context=None):
        if not default:
            default = {}
        default.update({
            'nao_name': self.pool.get(
                'ir.sequence').get(cr, uid, 'crm.lead.nao'),
        })
        return super(crm_lead, self).copy(
            cr, uid, id, default, context=context)

    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        result = []
        for r in self.browse(cr, uid, ids, context=context):
            result.append((r.id, r.nao_name))
        return result

    def name_search(self, cr, uid, name='', args=None, operator='ilike',
                    context=None, limit=None):
        args = args or []
        context = context or {}
        ids = None
        if name:
            ids = self.search(
                cr, uid,
                ['|', ('name', operator, name),
                 ('nao_name', operator, name)] + args, limit=limit,
                context=context)
        else:
            ids = self.search(cr, uid, args, limit=limit, context=context)
        return self.name_get(cr, uid, ids, context=context)

    def set_to_lost(self, cr, uid, ids, context=None):
        for o in self.browse(cr, uid, ids):
            msg = _("Opportunity Lost(name: %s).Reason:%s,note:%s") % (
                o.name, context.get('quotation_reason', ''),
                context.get('quotation_notes', ''))
            self.history(cr, uid, [o.id], _("Note"), history=True, details=msg)
            self.case_mark_lost(cr, uid, ids)

        return {'type': 'ir.actions.act_window_close'}
