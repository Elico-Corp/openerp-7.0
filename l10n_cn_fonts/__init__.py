# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2011 Elico Corp. All Rights Reserved.
#    Author:            Eric CAUDAL <contact@elico-corp.com>
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

from tools.config import config
import report
import os

def wrap_trml2pdf(method):
    """We have to wrap the original parseString() to modify the rml data
    before it generates the pdf."""
    def convert2TrueType(*args, **argv):
        """This function replaces the type1 font names with their truetype
        substitutes and puts a font registration section at the beginning
        of the rml file. The rml file is acually a string (data)."""
        odata = args[0]
	fontmap = {
            'Times-Roman':                   'DroidSansFallback',
            'Times-BoldItalic':              'DroidSansFallback',
            'Times-Bold':                    'DroidSansFallback',
            'Times-Italic':                  'DroidSansFallback',

            'Helvetica':                     'DroidSansFallback',
            'Helvetica-BoldItalic':          'DroidSansFallback',
            'Helvetica-Bold':                'DroidSansFallback',
            'Helvetica-Italic':              'DroidSansFallback',
            'Helvetica-Oblique':             'DroidSansFallback',
            'Helvetica-BoldOblique':         'DroidSansFallback',

            'Courier':                       'DroidSansFallback',
            'Courier-Bold':                  'DroidSansFallback',
            'Courier-BoldItalic':            'DroidSansFallback',
            'Courier-Italic':                'DroidSansFallback',
            'Courier-Oblique':               'DroidSansFallback',
            'Courier-BoldOblique':           'DroidSansFallback',

            'Helvetica-ExtraLight':          'DroidSansFallback',

            'TimesCondensed-Roman':          'DroidSansFallback',
            'TimesCondensed-BoldItalic':     'DroidSansFallback',
            'TimesCondensed-Bold':           'DroidSansFallback',
            'TimesCondensed-Italic':         'DroidSansFallback',

            'HelveticaCondensed':            'DroidSansFallback',
            'HelveticaCondensed-BoldItalic': 'DroidSansFallback',
            'HelveticaCondensed-Bold':       'DroidSansFallback',
            'HelveticaCondensed-Italic':     'DroidSansFallback',

            'DejaVu Sans':            'DroidSansFallback',
            'DejaVu Sans BoldItalic': 'DroidSansFallback',
            'DejaVu Sans Bold':       'DroidSansFallback',
            'DejaVu Sans Italic':     'DroidSansFallback',

            'VeraSansYuanTi':          'DroidSansFallback',
        } 
        i = odata.find('<docinit>')
        if i == -1:
            i = odata.find('<document')
            i = odata.find('>', i)
            i += 1
            starttag = '\n<docinit>\n'
            endtag = '</docinit>'
        else:
            i = i + len('<docinit>')
            starttag = ''
            endtag = ''
        data = odata[:i] + starttag
        adp = os.path.abspath(config['addons_path'])
        _localDir=os.path.dirname(__file__)
        _curpath=os.path.normpath(os.path.join(os.getcwd(),_localDir))
        adp = _curpath
        print adp
        for new in fontmap.itervalues():
            fntp = os.path.normcase(os.path.join(adp, 'fonts', new))
            data += '    <registerFont fontName="' + new + '" fontFile="' + fntp + '.ttf"/>\n'
        data += endtag + odata[i:]
	while len(fontmap)>0:
		ck=max(fontmap)
		data = data.replace(ck,fontmap.pop(ck))
       
        return method(data, args[1:] if len(args) > 2 else args[1], **argv)
    return convert2TrueType

report.render.rml2pdf.parseString = wrap_trml2pdf(report.render.rml2pdf.parseString)

report.render.rml2pdf.parseNode = wrap_trml2pdf(report.render.rml2pdf.parseNode)
