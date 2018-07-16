# -*- coding: utf-8 -*-
from odoo import http

# class DataEntry(http.Controller):
#     @http.route('/data_entry/data_entry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/data_entry/data_entry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('data_entry.listing', {
#             'root': '/data_entry/data_entry',
#             'objects': http.request.env['data_entry.data_entry'].search([]),
#         })

#     @http.route('/data_entry/data_entry/objects/<model("data_entry.data_entry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('data_entry.object', {
#             'object': obj
#         })