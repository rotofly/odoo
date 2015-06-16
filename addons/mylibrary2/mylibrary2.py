# -*- coding: utf-8 -*-
from openerp import models, fields

class author(models.Model):
    _name = 'mylibrary.author'
    _rec_name = 'lastname'
    firstname = fields.Char('FirstName', required=True)
    lastname = fields.Char('LastName', required=True) 
    book_ids = fields.One2many('mylibrary.book','author_id','Books')
 
class book(models.Model):
    _name = 'mylibrary.book'
    title = fields.Char('Title', required=True)
    genre = fields.Char('Genre', required=True)
    author_id = fields.Many2one('mylibrary.author','Author',ondelete='cascade')
