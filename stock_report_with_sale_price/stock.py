# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Jon Chow <jon.chow@elico-corp.com>
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

class stock_picking(osv.osv):
    _inherit = 'stock.picking'

    def print_delivery_note(self, cr, uid, ids, context=None):
        '''
        This function prints the delivery note
        '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time'
        datas = {
                 'model': 'stock.picking',
                 'ids': ids,
                 'form': self.read(cr, uid, ids[0], context=context),
                 'is_default_lang': self._is_default_lang
        }
        return {'type': 'ir.actions.report.xml', 'report_name': 'print.delivery.note', 'datas': datas, 'nodestroy': True}

    def _is_default_lang(self, user, partner_lang):
        # TODO not sure if all Odoo's default language is en_US
        '''decide if we print the alt_name of product.
            * first check if we have alt_language defined in user's company.
            * check if the partner's language is default: en_US'''
        if user.company_id and user.company_id.alt_language:
            return user.company_id.alt_language in ('en_US', None, False)
        elif partner_lang:
            return (partner_lang in ('en_US', None, False))
        else:
            return True
stock_picking()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
