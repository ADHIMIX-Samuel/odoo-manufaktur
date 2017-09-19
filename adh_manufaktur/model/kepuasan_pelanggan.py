from odoo import api,fields,models,_ 
import time

class adh_mrp_kepuasan_pelanggan(models.Model):
	_name = "adhimix.mrp.kepuasan.pelanggan"

	name = fields.Char("No Dokumen",required=True)
	tanggal_efektif = fields.Date("Tanggal Efektif",default=lambda self:time.strftime("%Y-%m-%d"),required=True)
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	pengelolaan_ids = fields.One2many(comodel_name="adhimix.mrp.kepuasan.pelanggan.line",inverse_name="reference")

class adh_mrp_pengelolaan_pelanggan_line(models.Model):
	_name ="adhimix.mrp.kepuasan.pelanggan.line"

	reference = fields.Many2one(comodel_name="adhimix.mrp.kepuasan.pelanggan",string="Reference")
	permasalahan_id = fields.Many2one(comodel_name="kepuasan.pelanggan.permasalahan",string="Permasalahan")
	tindakan_pencegahan = fields.Char("Tindakan Perbaikan/Pencegahan")
	pic_terkait = fields.Char("PIC Terkait")
	target_waktu = fields.Date("Taget Waktu Penyelesaian")
	status = fields.Selection([('Puas','Puas'),('Tidak Puas','Tidak Puas')],string="Status")

class kepuasan_pelanggan_permaslahan(models.Model):
	_name = "kepuasan.pelanggan.permasalahan"

	name = fields.Char("Permasalahan")

