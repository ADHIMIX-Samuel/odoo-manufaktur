from odoo import api,fields,models,_ 
import time
from odoo.tools import amount_to_text_en

class sale_order(models.Model):
	_inherit = 'sale.order'

	@api.depends('amount_total')
	def _terbilang(self):
		for rec in self:
			amount = rec.amount_total
			terbilang = self.env['wit.terbilang'].terbilang(amount,'IDR')
			rec.terbilang = terbilang


	terbilang = fields.Char(string="Terbilang", required=False, compute="_terbilang")
	perihal = fields.Text("Perihal")
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	kondisi_penawaran_ids = fields.One2many(comodel_name="sale.order.line.inherit",inverse_name="reference",string="Kondisi Penawaran")


class sale_order_line(models.Model):
	_name = 'sale.order.line.inherit'

	reference = fields.Many2one(comodel_name="sale.order",string="Reference")
	uraian_id  = fields.Many2one(comodel_name="sale.order.line.detail.uraian",string="Uraian")
	# sequence = fields.Integer('Sequence')

class sale_order_line_detail_uraian(models.Model):
	_name = "sale.order.line.detail.uraian"

	name = fields.Char("Uraian")