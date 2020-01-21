# -*- coding: utf-8 -*-
from odoo import http

# class TelenocHcm(http.Controller):
#     @http.route('/telenoc_hcm/telenoc_hcm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/telenoc_hcm/telenoc_hcm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('telenoc_hcm.listing', {
#             'root': '/telenoc_hcm/telenoc_hcm',
#             'objects': http.request.env['telenoc_hcm.telenoc_hcm'].search([]),
#         })

#     @http.route('/telenoc_hcm/telenoc_hcm/objects/<model("telenoc_hcm.telenoc_hcm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('telenoc_hcm.object', {
#             'object': obj
#         })