# -*- coding: utf-8 -*-
# © 2016 Elico corp(www.elico-corp.com)
# Licence AGPL-3.0 or Later(http://www.gnu.org/licenses/agpl.html)

{
    'name': 'customs_invoice_report',
    'version': '1.0',
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'summary': '',
    'description': """
         customs_invoice_report
         
          invoice tree view, 'more' button, 'Customs Invoice Report',
    """,
    'depends': ['base', 'account'],
    'category': '',
    'sequence': 10,
    'demo': [],
    'data': [
        'wizard/wizard_customs_invoice_report.xml',
        'report/customs_invoice_report.xml',
        # 'security/ir.model.access.csv',
        ],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'css': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
