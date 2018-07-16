# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DataEntry(models.Model):
    _name = 'data.entry'

    name = fields.Char()
    email = fields.Char()
    password = fields.Char()
    country_name = fields.Char()
    ip_address = fields.Char()
    city = fields.Char()
    region = fields.Char()
    country_code = fields.Char()
    sender_email = fields.Char()

    @api.multi
    def update_data(self, vals):
        vals[0]['name'] = vals[0]['email']
        self.env['data.entry'].create(vals[0])
        return True
