# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Augustin Cisterne-Kaas <augustin.cisterne-kaas@elico-corp.com>
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
{'name': 'Mail Organizer',
 'version': '0.1',
 'category': 'Social Network',
 'depends': ['web_polymorphic', 'mail'],
 'author': 'Elico Corp',
 'license': 'AGPL-3',
 'website': 'https://www.elico-corp.com',
 'description': """
This module allows you to assign a message to an existing or
a new resource dynamically.

You can configure the available model through
"Settings" -> "Technical" -> "Email Organizer"

Screencasts available at:
    https://www.youtube.com/watch?v=XYgswq6_J1I
    http://v.youku.com/v_show/id_XNjc3Njc0Nzky.html
""",
 'images': [],
 'demo': [],
 'data': ['wizard/wizard_mail_organizer_view.xml',
          'model_view.xml'],
 'qweb': [
     'static/src/xml/mail.xml'
 ],
 'js': [
     'static/src/js/mail.js'
 ],
 'css': [
     'static/src/css/mail.css'
 ],
 'installable': True,
 'application': False}
