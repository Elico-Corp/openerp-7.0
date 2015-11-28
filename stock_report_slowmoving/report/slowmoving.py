# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (c) 2010-2012 Elico Corp. All Rights Reserved.
#    Author:            Andy Lu <andy.lu@elico-corp.com>
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
import decimal_precision as dp
from report import report_sxw
import pooler

class Slowmove(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        res_user = pooler.get_pool(cr.dbname).get('res.users')
        self.context = context
        user = res_user.browse(cr, uid, uid)
        self.context.update({'lang':user.context_lang or 'en_US'})
        super(Slowmove, self).__init__(cr, uid, name, context=self.context)
        self.localcontext.update( {
            'time': time, 
            'dp': dp,
            'loginuser': user,
        })


report_sxw.report_sxw('report.stock.slowmove', 'stock.slowmove',
        'addons/stock_report_slowmoving/report/slowmoving_webkit.mako', parser=Slowmove)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
