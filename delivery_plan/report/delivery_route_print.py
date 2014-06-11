# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (c) 2010-2012 Elico Corp. All Rights Reserved.
#    Author: Yannick Gouin <yannick.gouin@elico-corp.com>
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time

from report import report_sxw
import pooler

class report_delivery_route_print(report_sxw.rml_parse):
    _name = 'report.delivery.route.print'
    
    def __init__(self, cr, uid, name, context):
        super(report_delivery_route_print, self).__init__(cr, uid, name, context)


report_sxw.report_sxw('delivery.route.print', 'delivery.route',
        'addons/fc_delivery_plan/report/delivery_route_print.mako', parser=report_delivery_route_print)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
