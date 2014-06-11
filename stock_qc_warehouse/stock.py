# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
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

from openerp.osv import fields, osv
from openerp.tools.translate import _

class stock_location(osv.osv):
    _inherit = "stock.location"
    
    _columns = {
        'qc_location': fields.boolean('QC Location'),
    }
    _defaults = {
        'qc_location': False,
    }
    
    def check_chained_auto_packing(self, cr, uid, vals):
        """ Chained location check
        @param vals: to create or write key values
        @return: True or False
        """
        if vals.get('qc_location', False) and vals.get('chained_auto_packing', False) != 'manual':
            raise osv.except_osv(_('Error'),
                                    _('QC Location must be chained manually.'))

        return True

    def create(self, cr, uid, vals, context=None):
        self.check_chained_auto_packing(cr, uid, vals)
        return super(stock_location, self).create(cr, uid, vals, context=context)

    def write(self, cr, uid, ids, vals, context=None):
        cur_loc = self.browse(cr, uid, ids and ids[0] or False)
        if not vals.get('chained_auto_packing', False) and ids:
            vals['chained_auto_packing'] = cur_loc.chained_auto_packing
        if vals.get('chained_auto_packing', False) != 'manual':
            if vals.get('qc_location', False):
                raise osv.except_osv(_('Error'),
                                    _('QC Location must be chained manually.'))
            else:
                if vals.get('qc_location', 5) == 5 and cur_loc.qc_location:
                    raise osv.except_osv(_('Error'),
                                    _('QC Location must be chained manually.'))

        if not vals.get('usage', False) and ids:
            vals['usage'] = cur_loc.usage
        if vals.get('usage', 'view') != 'internal':
            vals['qc_location'] = False
        return super(stock_location, self).write(cr, uid, ids, vals, context=context)

stock_location()


class stock_location_path(osv.osv):
    _inherit = "stock.location.path"

    def create(self, cr, uid, vals, context=None):
        if vals.get('location_from_id', False) and vals.get('auto', False):
            chloc = self.pool.get('stock.location').browse(cr, uid, vals.get('location_from_id',False), context=context)
            if chloc.qc_location and vals.get('auto', False) != 'manual':
                raise osv.except_osv(_('Error'),
                                    _('QC Location must be chained in manual.'))
        return super(stock_location_path, self).create(cr, uid, vals, context=context)

    def write(self, cr, uid, ids, vals, context=None):
        if vals.get('location_from_id', False) and vals.get('auto', False):
            chloc = self.pool.get('stock.location').browse(cr, uid, vals.get('location_from_id',False), context=context)
            if chloc.qc_location and vals.get('auto', False) != 'manual':
                raise osv.except_osv(_('Error'),
                                    _('QC Location must be chained in manual.'))
        return super(stock_location_path, self).write(cr, uid, ids, vals, context=context)

stock_location_path()


class stock_picking(osv.osv):
    _inherit = 'stock.picking'

    def _get_qc_location(self, cr, uid, ids, field, arg, context=None):
        res = {}
        for pick_obj in self.browse(cr, uid, ids, context):
            for move in pick_obj.move_lines:
                res[pick_obj.id] = move.location_id.qc_location
                if move.location_id.qc_location:
                    break
        return res

    _columns = {
        'qc_picking': fields.function(_get_qc_location, type='boolean', string='From QC Location',store=True),
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: