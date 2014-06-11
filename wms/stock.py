# -*- coding: utf-8 -*-
##############################################################################
#
#    wms module for OpenERP, This module allows to manage crossdocking in warehouses
#    Copyright (C) 2011 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#              Sebastien LANGE <sebastien.lange@syleam.fr>
#
#    This file is a part of wms
#
#    wms is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    wms is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv
from openerp.osv import fields


class stock_location_category(osv.osv):
    _name = 'stock.location.category'
    _description = 'Category of stock location'

    _columns = {
        'name': fields.char('Name', size=64, required=True, help='Name of the category of stock location'),
        'code': fields.char('Code', size=64, required=True, help='Code of the category of stock location'),
        'active': fields.boolean('Active', help='This field allows to hide the category without removing it'),
    }

stock_location_category()


class stock_location(osv.osv):
    _inherit = 'stock.location'

    _columns = {
        'warehouse_id': fields.many2one('stock.warehouse', 'Warehouse', help='Warehouse where is located this location'),
        'categ_id': fields.many2one('stock.location.category', 'Category', help='Category of this location'),
    }

stock_location()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
