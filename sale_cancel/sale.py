# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Alex Duan <alex.duan@elico-corp.com>
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
from openerp.osv import orm
from openerp import netsvc
import logging

_logger = logging.getLogger(__name__)


class sale_order(orm.Model):
    _inherit = 'sale.order'

    def action_cancel_order_with_moves_not_delivered(
            self, cr, uid, ids, context=None):
        wf_service = netsvc.LocalService("workflow")
        if context is None:
            context = {}
        for sale in self.browse(cr, uid, ids, context=context):
            try:
                for pick in sale.picking_ids:
                    if pick.state != 'cancel':
                        wf_service.trg_validate(
                            uid, 'stock.picking', pick.id, 'button_cancel', cr)
                        # pick.write({'state':'cancel'})

                #cancel the invoice?
                # for inv in sale.invoice_ids:
                #     wf_service.trg_validate(
                #         uid, 'account.invoice', inv.id, 'invoice_cancel', cr)

                # for line in sale.order_line:
                #     if line.procurement_id:
                #         wf_service.trg_validate(
                #             uid, 'procurement.order',
                #             line.procurement_id.id, 'button_check', cr)
                
                order_ref = context.get('order_ref', False)
                self.action_cancel(cr, uid, [sale.id], context=context)
                self.write(
                    cr, uid,
                    [sale.id],
                    {'client_order_ref': order_ref})
                cr.commit()
            except:
                raise
                _logger.error(
                    '==== #elico-corp: Cancel SO and DO fail! %s====' % (
                        sale.id))
        return True
