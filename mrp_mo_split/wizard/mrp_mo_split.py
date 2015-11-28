# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2009 Albert Cervera i Areny - NaN  (http://www.nan-tic.com)
#    All Rights Reserved.
#    Copyright (c) 2010-Today Elico Corp. All Rights Reserved.
#    Author: Andy Lu <andy.lu@elico-corp.com>
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

from openerp.osv import osv, fields
from tools.translate import _


class mrp_mo_split(osv.osv_memory):
    _name = 'mro.mo.split'

    _columns = {
        'quantity': fields.float('Quantity', required=True)
    }

    def split(self, cr, uid, ids, context=None):
        context = context or {}
        assert 'active_ids' in context
        active_id = context['active_id']
        productions = []
        for mro_mo_split in self.browse(
                cr, uid, ids, context=context):
            quantity = mro_mo_split.quantity
            if not quantity or quantity <= 0:
                raise osv.except_osv(_('Error !'), _(
                    'You must specify a value greater than 0.'))
            productions = self.pool.get('mrp.production')._split(
                cr, uid, active_id, quantity, context)
        return {
            'domain': "[('id','in',%s)]" % productions,
            'name': _('Production Orders'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'mrp.production',
            'view_id': False,
            'type': 'ir.actions.act_window'
        }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
