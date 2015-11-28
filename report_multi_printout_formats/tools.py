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


def is_default_lang(user, partner_lang):
    # TODO not sure if all Odoo's default language is en_US
    '''decide if we print the alt_name of product.
        * first check if we have alt_language defined in user's company.
        * check if the partner's language is default: en_US.
        * check if alt language is the same as user's language '''
    if user.company_id and user.company_id.alt_language:
        return (user.company_id.alt_language in (
            'en_US', None, False, user.lang))
    elif partner_lang:
        return (partner_lang in ('en_US', None, False))
    else:
        return True


def choose_lang(user, o):
    return (user.company_id and user.company_id.alt_language) or\
        o.partner_id.lang
