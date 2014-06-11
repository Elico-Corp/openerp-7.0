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


class product_ul(osv.osv):
    _inherit = 'product.ul'
    def _get_cbm(self, cr, uid, ids, fields, arg=None,  context=None):
        res = {}
        for ul in self.browse(cr, uid, ids, context=context):
            cbm = ul.high * ul.width * ul.long 
            cbm = cbm != 0 and cbm/1000000 
            res[ul.id] = cbm
            
        return res
    _columns = {
        'name': fields.char('name', size=32),
        'high': fields.float('H (cm)', digits=(3,3)),
        'width':fields.float('W (cm)', digits=(3,3)),
        'long': fields.float('L (cm)', digits=(3,3)),
        'cbm': fields.function(_get_cbm, arg=None, type='float', digits=(3,3), string='CBM'),
    }

 # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
