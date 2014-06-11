    # -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Augustin Cisterne-Kaas <augustin.cisterne-kaas@elico-corp.com>
#    Eric Caudal <eric.caudal@elico-corp.com>

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
from openerp.osv import fields, orm


class res_intercompany(orm.Model):
    _inherit = 'res.intercompany'

    def _select_concepts(self, cr, uid, context=None):
        """ Available concepts

        Can be inherited to add custom versions.
        """
        res = super(res_intercompany, self)._select_concepts(cr, uid, context)
        res += [('so2po', 'SO to PO'),
                ('so2so', 'SO to SO'),
                ('po2so', 'PO to SO')]
        return res

    def _select_models(self, cr, uid, context=None):
        """ Available Object names

        Can be inherited to add custom versions.
        """
        res = super(res_intercompany, self)._select_models(
            cr, uid, context)
        new_dict = {'so2po': 'sale.order',
                    'so2so': 'sale.order',
                    'po2so': 'purchase.order'}
        res = dict(res.items() + new_dict.items())
        return res

    _columns = {
        'concept': fields.selection(_select_concepts, string="Concept",
                                    required=True),
    }
