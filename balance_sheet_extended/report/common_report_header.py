# -*- coding: utf-8 -*-
# © 2014 Elico Corp (https://www.elico-corp.com)
# Licence AGPL-3.0 or later(http://www.gnu.org/licenses/agpl.html)


from openerp import pooler
from openerp.tools.translate import _

class common_report_header(object):

    def _sum_debit(self, period_id=False, journal_id=False):
        if journal_id and isinstance(journal_id, int):
            journal_id = [journal_id]
        if period_id and isinstance(period_id, int):
            period_id = [period_id]
        if not journal_id:
            journal_id = self.journal_ids
        if not period_id:
            period_id = self.period_ids
        if not (period_id and journal_id):
            return 0.0
        self.cr.execute('SELECT SUM(debit) FROM account_move_line l '
                        'WHERE period_id IN %s AND journal_id IN %s ' + self.query_get_clause + ' ',
                        (tuple(period_id), tuple(journal_id)))
        return self.cr.fetchone()[0] or 0.0

    def _sum_credit(self, period_id=False, journal_id=False):
        if journal_id and isinstance(journal_id, int):
            journal_id = [journal_id]
        if period_id and isinstance(period_id, int):
            period_id = [period_id]
        if not journal_id:
            journal_id = self.journal_ids
        if not period_id:
            period_id = self.period_ids
        if not (period_id and journal_id):
            return 0.0
        self.cr.execute('SELECT SUM(credit) FROM account_move_line l '
                        'WHERE period_id IN %s AND journal_id IN %s '+ self.query_get_clause+'',
                        (tuple(period_id), tuple(journal_id)))
        return self.cr.fetchone()[0] or 0.0

    def _get_start_date(self, data):
        if data.get('form', False) and data['form'].get('date_from', False):
            return data['form']['date_from']
        return ''

    def _get_target_move(self, data):
        if data.get('form', False) and data['form'].get('target_move', False):
            if data['form']['target_move'] == 'all':
                return _('All Entries')
            return _('All Posted Entries')
        return ''

    def _get_end_date(self, data):
        if data.get('form', False) and data['form'].get('date_to', False):
            return data['form']['date_to']
        return ''

    def get_start_period(self, data):
        if data.get('form', False) and data['form'].get('period_from', False):
            return pooler.get_pool(self.cr.dbname).get('account.period').browse(self.cr,self.uid,data['form']['period_from']).name
        return ''

    def get_end_period(self, data):
        if data.get('form', False) and data['form'].get('period_to', False):
            return pooler.get_pool(self.cr.dbname).get('account.period').browse(self.cr, self.uid, data['form']['period_to']).name
        return ''

    def _get_account(self, data):
        if data.get('form', False) and data['form'].get('chart_account_id', False):
            return pooler.get_pool(self.cr.dbname).get('account.account').browse(self.cr, self.uid, data['form']['chart_account_id']).name
        return ''

    def _get_sortby(self, data):
        raise (_('Error!'), _('Not implemented.'))

    def _get_filter(self, data):
        if data.get('form', False) and data['form'].get('filter', False):
            if data['form']['filter'] == 'filter_date':
                return self._translate('Date')
            elif data['form']['filter'] == 'filter_period':
                return self._translate('Periods')
        return self._translate('No Filters')

    def _sum_debit_period(self, period_id, journal_id=None):
        journals = journal_id or self.journal_ids
        if not journals:
            return 0.0
        self.cr.execute('SELECT SUM(debit) FROM account_move_line l '
                        'WHERE period_id=%s AND journal_id IN %s '+ self.query_get_clause +'',
                        (period_id, tuple(journals)))

        return self.cr.fetchone()[0] or 0.0

    def _sum_credit_period(self, period_id, journal_id=None):
        journals = journal_id or self.journal_ids
        if not journals:
            return 0.0
        self.cr.execute('SELECT SUM(credit) FROM account_move_line l '
                        'WHERE period_id=%s AND journal_id IN %s ' + self.query_get_clause +' ',
                        (period_id, tuple(journals)))
        return self.cr.fetchone()[0] or 0.0

    def _get_fiscalyear(self, data):
        if data.get('form', False) and data['form'].get('fiscalyear_id', False):
            return pooler.get_pool(self.cr.dbname).get('account.fiscalyear').browse(self.cr, self.uid, data['form']['fiscalyear_id']).name
        return ''

    def _get_company(self, data):
        if data.get('form', False) and data['form'].get('chart_account_id', False):
            return pooler.get_pool(self.cr.dbname).get('account.account').browse(self.cr, self.uid, data['form']['chart_account_id']).company_id.name
        return ''

    def _get_journal(self, data):
        codes = []
        if data.get('form', False) and data['form'].get('journal_ids', False):
            self.cr.execute('select code from account_journal where id IN %s',(tuple(data['form']['journal_ids']),))
            codes = [x for x, in self.cr.fetchall()]
        return codes

    def _get_currency(self, data):
        if data.get('form', False) and data['form'].get('chart_account_id', False):
            return pooler.get_pool(self.cr.dbname).get('account.account').browse(self.cr, self.uid, data['form']['chart_account_id']).company_id.currency_id.symbol
        return ''

