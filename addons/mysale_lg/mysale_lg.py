# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class sale_order_line(osv.osv):
    _inherit = 'sale.order.line'
    _name = 'sale.order.line'
    _columns = {'lg': fields.integer('Length'),}

sale_order_line()
