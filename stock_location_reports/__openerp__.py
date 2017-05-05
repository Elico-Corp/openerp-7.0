# -*- coding: utf-8 -*-
# © 2014 Elico corp(www.elico-corp.com)
# Licence AGPL-3.0 or later(http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Stock Location Reports',
    'version': '7.0.1.0.0',
    'category': 'Stock',
    'sequence': 19,
    'summary': 'Stock Location Reports',
    'description': """
        Stock Location Reports
        ==================================================
        Add Three new reports for warehouse management:
            * stock location reports
            * stock location overall reports
            * stock inventory reports
    """,
    'author': 'Elico Corp',
    'website': 'http://www.elico-corp.com',
    'images' : [],
    'depends': ['stock','product_stock_type','report_webkit'],
    'data': ['reports.xml'],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}


