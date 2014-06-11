# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#     Jon Chow <jon.chow@elico-corp.com>
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


class  stock_tracking(osv.osv):
    _inherit ='stock.tracking'
    def _get_net_weight(self, cr, uid, ids, field_name, arg=None, context=None):
        res = {}
        for pack in self.browse(cr, uid, ids, context=context):
            res[pack.id] = sum([m.product_id.weight_net * m.product_qty for m in pack.move_ids])
        return res
    
    _columns={
        'ul_id':    fields.many2one('product.ul','Pack Template'),
        'pack_h':   fields.related('ul_id', 'high', string='H (cm)', type='float', digits=(3,3), readonly=True),
        'pack_w':   fields.related('ul_id', 'width', string='W (cm)', type='float', digits=(3,3), readonly=True),
        'pack_l':   fields.related('ul_id', 'long', string='L (cm)', type='float', digits=(3,3), readonly=True),
        'pack_cbm': fields.related('ul_id', 'cbm', string='CBM',    type='float', digits=(3,3), readonly=True),

        'pack_address': fields.char('Address', size=128),
        'pack_note':    fields.char('Note', size=128),

        'gross_weight': fields.float('GW (Kg)'),
        'net_weight':   fields.function(_get_net_weight, arg=None, type='float', string='NW (Kg)'),
    }



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: