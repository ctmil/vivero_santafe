from odoo import fields, models
from odoo.exceptions import ValidationError

class Plantas(models.Model):
    _name = 'vivero.planta'

    def btn_demo(self):
        raise ValidationError('Hola mundo')
    
    name = fields.Char("Planta")
    price = fields.Float("Precio")
    order_ids = fields.One2many(comodel_name='vivero.pedido',inverse_name='plant_id',string='Pedidos')


class Pedidos(models.Model):
    _name = 'vivero.pedido'

    plant_id = fields.Many2one('vivero.planta',string='Planta')
    partner_id = fields.Many2one('res.partner',string='Cliente')
    qty = fields.Integer('Cantidad')
