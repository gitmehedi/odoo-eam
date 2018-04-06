# -*- coding: utf-8 -*-

from odoo import api, fields, models


class stock_location(models.Model):
    _inherit = "stock.location"

    usage = fields.Selection(selection_add=[('asset', 'Asset Location')],
                             default='asset', index=True, required=True)
