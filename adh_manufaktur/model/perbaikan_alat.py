from odoo import api,fields,models,_
import time

class adh_mrp_perbaikan_alat(models.Model):
	_name = "adhimix.mrp.perbaikan.alat"


	name = fields.Char("No Dokumen",required=True)
	nama_pekerjaan = fields.Char("Nama Pekerjaan")
	no_identitas_alat = fields.Char("No Identitas Alat")
	tipe_alat = fields.Char("Tipe Alat")
	tanggal_masuk = fields.Date("Tanggal Masuk",required=True)
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	tanggal_checklist_eng = fields.Date("Tanggal Check List ENG",required=True)
	tanggal_checklist_qc = fields.Date("Tanggal Check List QC")
	tanggal_efektif = fields.Date("Tanggal Efektif", default=lambda self:time.strftime("%Y-%m-%d"))
	bagian_cabin_ids = fields.One2many(comodel_name="adhimix.mrp.perbaikan.alat.cabin",inverse_name="reference")
	chassis_drummixer_ids = fields.One2many(comodel_name="adhimix.mrp.perbaikan.alat.chassis",inverse_name="reference")
	aksesoris_drummixer_ids = fields.One2many(comodel_name="adhimix.mrp.perbaikan.alat.aksesoris",inverse_name="reference")

# Class Bagian Cabin
class adh_mrp_perbaikan_alat_cabin(models.Model):
	_name = "adhimix.mrp.perbaikan.alat.cabin"

	reference = fields.Many2one(comodel_name="adhimix.mrp.perbaikan.alat",string="Reference")
	bagian_yg_dikerjakan_cabin = fields.Many2one(comodel_name="perbaikan.alat.cabin.detail.bagian",string="Bagian Yang Dikerjakan")
	kriteria_cabin = fields.Many2one(comodel_name="perbaikan.alat.cabin.detail.kriteria",string="Kriteria")
	qty_cabin = fields.Float("Qty",default="1.0")
	hasil_1_cabin = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil 1")
	hasil_2_cabin = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil 2")
	bobot_cabin = fields.Float("Bobot")
	tindak_lanjut_cabin = fields.Char("Tindak Lanjut")

class perbaikan_alat_cabin_detail_bagian(models.Model):
	_name ="perbaikan.alat.cabin.detail.bagian"

	name = fields.Char("Bagian Yang Dikerjakan")

class perbaikan_alat_cabin_detail_kriteria(models.Model):
	_name ="perbaikan.alat.cabin.detail.kriteria"

	name = fields.Char("Kriteria")

# Class Chassis Drum Mixer

class adh_mrp_perbaikan_alat_chassis(models.Model):
	_name = "adhimix.mrp.perbaikan.alat.chassis"

	reference = fields.Many2one(comodel_name="adhimix.mrp.perbaikan.alat",string="Reference")
	bagian_yg_dikerjakan_chassis = fields.Many2one(comodel_name="perbaikan.alat.chassis.detail.bagian",string="Bagian Yang Dikerjakan")
	kriteria_chassis = fields.Many2one(comodel_name="perbaikan.alat.chassis.detail.kriteria",string="Kriteria")
	qty_chassis = fields.Float("Qty",default="1.0")
	hasil_1_chassis = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil 1")
	hasil_2_chassis = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil 2")
	bobot_chassis = fields.Float("Bobot")
	tindak_lanjut_chassis = fields.Char("Tindak Lanjut")

class perbaikan_alat_chassis_detail_bagian(models.Model):
	_name ="perbaikan.alat.chassis.detail.bagian"

	name = fields.Char("Bagian Yang Dikerjakan")

class perbaikan_alat_chassis_detail_kriteria(models.Model):
	_name ="perbaikan.alat.chassis.detail.kriteria"

	name = fields.Char("Kriteria")

# Class aksesoris drum mixer
class adh_mrp_perbaikan_alat_aksesoris(models.Model):
	_name = "adhimix.mrp.perbaikan.alat.aksesoris"

	reference = fields.Many2one(comodel_name="adhimix.mrp.perbaikan.alat",string="Reference")
	bagian_yg_dikerjakan_aksesoris = fields.Many2one(comodel_name="perbaikan.alat.aksesoris.detail.bagian",string="Bagian Yang Dikerjakan")
	kriteria_aksesoris = fields.Many2one(comodel_name="perbaikan.alat.aksesoris.detail.kriteria",string="Kriteria")
	qty_aksesoris = fields.Float("Qty",default="1.0")
	hasil_1_aksesoris = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil 1")
	hasil_2_aksesoris = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil 2")
	bobot_aksesoris = fields.Float("Bobot")
	tindak_lanjut_aksesoris = fields.Char("Tindak Lanjut")

class perbaikan_alat_cabin_detail_aksesoris_bagian(models.Model):
	_name ="perbaikan.alat.aksesoris.detail.bagian"

	name = fields.Char("Bagian Yang Dikerjakan")

class perbaikan_alat_cabin_detail_aksesoris_kriteria(models.Model):
	_name ="perbaikan.alat.aksesoris.detail.kriteria"

	name = fields.Char("Kriteria")

