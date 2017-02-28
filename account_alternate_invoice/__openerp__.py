# -*- coding: utf-8 -*-
# © 2016 Elico corp(www.elico-corp.com)
# Licence AGPL-3.0 or Later(http://www.gnu.org/licenses/agpl.html)
{
    'name': 'account_alternate_invoice',
    'version': '1.0',
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'summary': '',
    'description': """
         Account Alternate Invoice
    """,
    'depends': ['base', 'account', ],
    'category': '',
    'sequence': 10,
    'demo': [],
    'data': [
        'account_invoice_view.xml',
        'report.xml',
        # 'security/ir.model.access.csv',
        ],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'css': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
