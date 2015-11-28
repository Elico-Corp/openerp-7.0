# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Author: LIN Yu <lin.yu@elico-corp.com>
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

from openerp import tools
from openerp.osv import fields, osv, orm


class pos_order_report(orm.Model):
    _inherit = "report.pos.order"
    _columns = {
        'total_wo_disc': fields.float('Total w/o Discount', readonly=True),
        'event_id': fields.many2one(
            'event.event', 'Event',
            help="Please input the event related to this sales order"),
        'section_id': fields.many2one(
            'crm.case.section', 'Sales Team',
            help="Please input the Sales team related to this POS order"),
        # 'channel_id': fields.many2one(
        #     'res.partner.category', 'Channel',
        #     help="Please input the channel related to this POS  order"),
    }

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'report_pos_order')
        cr.execute("""
            create or replace view report_pos_order as (
                select
                    min(l.id) as id,
                    count(*) as nbr,
                    to_date(to_char(s.date_order, 'dd-MM-YYYY'),'dd-MM-YYYY') as date,
                    sum(l.qty * u.factor) as product_qty,
                    sum(l.qty * l.price_unit) as total_wo_disc,
                    sum(l.qty * l.price_unit * (100.0-l.discount) / 100.0) as price_total,
                    sum((l.qty * l.price_unit) * (l.discount / 100)) as total_discount,
                    (sum(l.qty*l.price_unit)/sum(l.qty * u.factor))::decimal(16,2) as average_price,
                    sum(cast(to_char(date_trunc('day',s.date_order) - date_trunc('day',s.create_date),'DD') as int)) as delay_validation,
                    to_char(s.date_order, 'YYYY') as year,
                    to_char(s.date_order, 'MM') as month,
                    to_char(s.date_order, 'YYYY-MM-DD') as day,
                    s.partner_id as partner_id,
                    s.state as state,
                    s.user_id as user_id,
                    s.shop_id as shop_id,
                    s.company_id as company_id,
                    s.sale_journal as journal_id,
                    l.product_id as product_id,
                    s.section_id as section_id,
                    s.event_id as event_id
                from pos_order_line as l
                    left join pos_order s on (s.id=l.order_id)
                    left join product_product p on (l.product_id=p.id)
                    left join product_template pt on (p.product_tmpl_id=pt.id)
                    left join product_uom u on (u.id=pt.uom_id)
                group by
                    to_char(s.date_order, 'dd-MM-YYYY'),to_char(s.date_order, 'YYYY'),to_char(s.date_order, 'MM'),
                    to_char(s.date_order, 'YYYY-MM-DD'), s.partner_id,s.state,
                    s.user_id,s.shop_id,s.company_id,s.sale_journal,l.product_id,s.create_date,
                    s.section_id, s.event_id
                having
                    sum(l.qty * u.factor) != 0)""")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
