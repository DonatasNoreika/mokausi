from odoo import fields, models


class MokausiProgress(models.Model):
    _name = 'mokausi.progress'
    _description = 'Mokymosi progresas'
    _rec_name = 'user_id'
    _order = 'write_date desc'

    user_id = fields.Many2one('res.users', 'Naudotojas', required=True, ondelete='cascade', index=True)
    points = fields.Integer('Taškai', readonly=True)
    data = fields.Text('Duomenys (JSON)', readonly=True)

    _sql_constraints = [
        ('user_unique', 'unique(user_id)', 'Kiekvienas naudotojas turi vieną progreso įrašą.'),
    ]
