from odoo import api,fields,models,_ 
import time

class adh_mrp_pemeriksaan_kerusakan_alat(models.Model):
	_name = "adhimix.mrp.pemeriksaan.kerusakan.alat"

	name = fields.Char(string="No Dokumen")
	nama_alat = fields.Char(string="Nama alat")
	tipe_alat = fields.Char(string="Tipe Alat")
	nomor_alat = fields.Char(string="Nomor Alat")
	lokasi_alat = fields.Char(string="Lokasi Alat")
	tanggal_efektif = fields.Date(string="Tanggal Efektif",default=lambda self:time.strftime("%Y-%m-%d"))
	tanggal_masuk_alat = fields.Date(string="Tanggal Masuk Alat")
	tanggal_checklist_alat = fields.Date(string="Tanggal Checklist Alat")
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	kerusakan_alat = fields.Selection([('Internal','Internal'),('Eksternal','Eksternal')])
	pemeriksaan_alat_ids = fields.One2many(comodel_name="adhimix.mrp.pemeriksaan.alat.detail",inverse_name="reference",string="Reference")


class adh_mrp_pemeriksaan_alat_detail(models.Model):
	_name = "adhimix.mrp.pemeriksaan.alat.detail"

	reference = fields.Many2one(comodel_name="adhimix.mrp.pemeriksaan.kerusakan.alat",string="Reference")
	kategori_alat = fields.Many2one(comodel_name="adhimix.kategori.alat",string="Kategori/Bagian Alat")
	kriteria_alat = fields.Many2one(comodel_name="adhimix.kriteria.alat",string="Kriteria")
	hasil_sesuai = fields.Boolean(string="Sesuai")
	hasil_tidak_sesuai = fields.Boolean(string="Tidak Sesuai")
	keterangan = fields.Char(string="Keterangan")
	

class adh_kategori_alat(models.Model):
	_name = "adhimix.kategori.alat"

	name = fields.Char(string="Kategori/Bagian Alat")

class adh_kriteria_alat(models.Model):
	_name = "adhimix.kriteria.alat"

	name = fields.Char(string="Kriteria")