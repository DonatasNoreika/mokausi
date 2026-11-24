import base64

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MokausiVersion(models.Model):
    _name = 'mokausi.version'
    _description = 'Mokymosi svetainės versija'
    _order = 'create_date desc, id desc'

    name = fields.Char('Pavadinimas', required=True, default='Nauja versija')
    html_file = fields.Binary('HTML failas', required=True, attachment=True)
    html_filename = fields.Char('Failo pavadinimas')
    notes = fields.Text('Kas pasikeitė')
    is_current = fields.Boolean('Rodoma svetainėje', copy=False, readonly=True)
    file_size = fields.Integer('Dydis, KB', compute='_compute_file_size', store=True)

    def _raw_html(self):
        self.ensure_one()
        data = self.with_context(bin_size=False).html_file
        return base64.b64decode(data) if data else b''

    @api.depends('html_file')
    def _compute_file_size(self):
        for rec in self:
            rec.file_size = round(len(rec._raw_html()) / 1024)

    @api.constrains('html_file', 'html_filename')
    def _check_html(self):
        for rec in self:
            if rec.html_filename and not rec.html_filename.lower().endswith(('.html', '.htm')):
                raise ValidationError('Įkelkite .html failą.')
            head = rec._raw_html()[:2000].lstrip(b'\xef\xbb\xbf \t\r\n').lower()
            if not (head.startswith(b'<!doctype html') or head.startswith(b'<html')):
                raise ValidationError('Failas neatrodo kaip HTML puslapis: jis turi prasidėti <!DOCTYPE html>.')

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        # Naujausia įkelta versija iškart rodoma svetainėje.
        records[-1:].action_make_current()
        return records

    def action_make_current(self):
        self.ensure_one()
        self.search([('is_current', '=', True), ('id', '!=', self.id)]).write({'is_current': False})
        self.is_current = True
        return True

    def action_open_site(self):
        return {'type': 'ir.actions.act_url', 'url': '/mokausi', 'target': 'new'}

    @api.model
    def _get_current(self):
        return self.search([('is_current', '=', True)], limit=1) or self.search([], limit=1)
