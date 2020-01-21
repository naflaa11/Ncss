# -*- coding: utf-8 -*-
from odoo import http

# class HcmPro(http.Controller):
#     @http.route('/hcm_pro/hcm_pro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hcm_pro/hcm_pro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hcm_pro.listing', {
#             'root': '/hcm_pro/hcm_pro',
#             'objects': http.request.env['hcm_pro.hcm_pro'].search([]),
#         })

#     @http.route('/hcm_pro/hcm_pro/objects/<model("hcm_pro.hcm_pro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hcm_pro.object', {
#             'object': obj
#         })