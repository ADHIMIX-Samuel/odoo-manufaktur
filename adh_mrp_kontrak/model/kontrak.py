from odoo import api,fields,models,_
import datetime
import time
import calendar


class adh_mrp_kontrak(models.Model):
	_name = "adhimix.mrp.kontrak"



	name = fields.Char("No Penawaran",required=True)
	tanggal = fields.Date("Tanggal",required=True)
	tanggal_efektif = fields.Date("Tanggal Efektif",default=lambda self:time.strftime("%Y-%m-%d"))
	pekerjaan = fields.Char("Pekerjaan")
	lokasi = fields.Char("lokasi")
	spesifikasi = fields.Char("Spesifikasi")
	waktu_pelaksanaan = fields.Date("Waktu Pelaksanaan",required=True)
	harga_negosiasi = fields.Float("Harga Negosiasi")
	cara_pembayaran = fields.Char("Cara Pembayaran")
	scope_pekerjaan_owner = fields.Char("Scope Pekerjaan PT. API")
	scope_pekerjaan_client = fields.Char("Scope Pekerjaan")
	nama_pelanggan = fields.Many2one(comodel_name="res.partner",string="Nama Pelanggan")
	lampiran = fields.Many2many(comodel_name="ir.attachment",string="Lampiran")
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	# current_date = datetime

