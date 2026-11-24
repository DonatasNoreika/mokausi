import json

from odoo import http
from odoo.http import request

MAX_STATE_BYTES = 256 * 1024


class Mokausi(http.Controller):

    @http.route('/mokausi', type='http', auth='public', website=True, sitemap=True)
    def page(self, **kw):
        return request.render('mokausi.page')

    @http.route('/mokausi/app', type='http', auth='public', sitemap=False)
    def app(self, **kw):
        version = request.env['mokausi.version'].sudo()._get_current()
        if not version:
            return request.not_found()
        return request.make_response(version._raw_html(), headers=[
            ('Content-Type', 'text/html; charset=utf-8'),
            ('Cache-Control', 'no-cache'),
            ('X-Frame-Options', 'SAMEORIGIN'),
            ('Content-Security-Policy', "frame-ancestors 'self'"),
        ])

    @http.route('/mokausi/api/state', type='json', auth='public', methods=['POST'])
    def state(self, state=None, **kw):
        user = request.env.user
        if user._is_public():
            return {'login': False}
        Progress = request.env['mokausi.progress'].sudo()
        record = Progress.search([('user_id', '=', user.id)], limit=1)
        if state is None:
            return {'login': True, 'state': json.loads(record.data) if record.data else None}
        if not isinstance(state, dict):
            return {'login': True, 'saved': False}
        data = json.dumps(state, ensure_ascii=False)
        if len(data.encode()) > MAX_STATE_BYTES:
            return {'login': True, 'saved': False}
        try:
            points = int(state.get('pts') or 0)
        except (TypeError, ValueError):
            points = 0
        vals = {'data': data, 'points': max(points, 0)}
        if record:
            record.write(vals)
        else:
            Progress.create(dict(vals, user_id=user.id))
        return {'login': True, 'saved': True}
