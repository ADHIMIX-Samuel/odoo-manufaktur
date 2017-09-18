from odoo import api,fields,models,_ 
import time


class adh_mrp_perencanaan_pemasaran(models.Model):
	_name = "adhimix.mrp.perencanaan.pemasaran"

	name = fields.Char("No Dokumen",required=True)
	tanggal_efektif = fields.Date("Tanggal Efektif",required=True,default=lambda self:time.strftime("%Y-%m-%d"))
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	total_amount = fields.Float("Total")
	readymix_ids = fields.One2many(comodel_name="adhimix.perencanaan.pemasaran.readymix",inverse_name="reference",string="Divisi Readymix")
	precast_ids = fields.One2many(comodel_name="adhimix.perencanaan.pemasaran.precast",inverse_name="reference",string="Divisi Precast")
	external_ids = fields.One2many(comodel_name="adhimix.perencanaan.pemasaran.external",inverse_name="reference",string="External")

class adh_perencanaan_pemasaran_readymix(models.Model):
	_name = "adhimix.perencanaan.pemasaran.readymix"

	reference = fields.Many2one(comodel_name="adhimix.mrp.perencanaan,pemasaran",string="Reference")
	pelanggan = fields.Many2one(comodel_name="res.partner",string=" Nama Pelanggan",required=True,domain=[('customer','=',True)])
	jenis_pekerjaan = fields.Char("Jenis Pekerjaan/Alat")
	qty = fields.Float(string="Qty",default="1.0")
	# Total
	total_sales = fields.Float("Sales")
	total_biaya = fields.Float("Biaya")
	total_laba = fields.Float("Laba")
	total_pm = fields.Float("PM")

	# Rencana 
	# rencana_periode = fields.Date("Periode",required=True)
	rencana_volume = fields.Float("Volume")
	rencana_sales = fields.Float("Sales")
	rencana_biaya = fields.Float("Biaya")
	rencana_laba = fields.Float("Laba")

	# Real 
	# real_periode = fields.Date("Periode",required=True)
	real_volume = fields.Float("Volume")
	real_sales = fields.Float("Sales")
	real_biaya = fields.Float("Biaya")
	real_laba = fields.Float("Laba")

class adh_perencanaan_pemasaran_precast(models.Model):
	_name = "adhimix.perencanaan.pemasaran.precast"

	reference = fields.Many2one(comodel_name="adhimix.mrp.perencanaan,pemasaran",string="Reference")
	pelanggan = fields.Many2one(comodel_name="res.partner",string="Nama Pelanggan",required=True,domain=[('customer','=',True)])
	jenis_pekerjaan = fields.Char("Jenis Pekerjaan/Alat")
	qty = fields.Float(string="Qty",default="1.0")
	# Total
	total_sales = fields.Float("Sales")
	total_biaya = fields.Float("Biaya")
	total_laba = fields.Float("Laba")
	total_pm = fields.Float("PM")

	# Rencana 
	# rencana_periode = fields.Date("Periode",required=True)
	rencana_volume = fields.Float("Volume")
	rencana_sales = fields.Float("Sales")
	rencana_biaya = fields.Float("Biaya")
	rencana_laba = fields.Float("Laba")

	# Real 
	# real_periode = fields.Date("Periode",required=True)
	real_volume = fields.Float("Volume")
	real_sales = fields.Float("Sales")
	real_biaya = fields.Float("Biaya")
	real_laba = fields.Float("Laba")

class adh_perencanaan_pemasaran_external(models.Model):
	_name = "adhimix.perencanaan.pemasaran.external"

	reference = fields.Many2one(comodel_name="adhimix.mrp.perencanaan,pemasaran",string="Reference")
	pelanggan = fields.Many2one(comodel_name="res.partner",string="Nama Pelanggan",required=True,domain=[('customer','=',True)])
	jenis_pekerjaan = fields.Char("Jenis Pekerjaan/Alat")
	qty = fields.Float(string="Qty",default="1.0")
	# Total
	total_sales = fields.Float("Sales")
	total_biaya = fields.Float("Biaya")
	total_laba = fields.Float("Laba")
	total_pm = fields.Float("PM")

	# Rencana 
	# rencana_periode = fields.Date("Periode",required=True)
	rencana_volume = fields.Float("Volume")
	rencana_sales = fields.Float("Sales")
	rencana_biaya = fields.Float("Biaya")
	rencana_laba = fields.Float("Laba")

	# Real 
	# real_periode = fields.Date("Periode",required=True)
	real_volume = fields.Float("Volume")
	real_sales = fields.Float("Sales")
	real_biaya = fields.Float("Biaya")
	real_laba = fields.Float("Laba")
