from odoo import api,fields,models,_
import time

class adh_mrp_pengiriman(models.Model):
	_name = "adhimix.mrp.pengiriman"

	name = fields.Char(string="No Dokumen")
	tanggal_efektif = fields.Date(string="Tanggal Efektif",default=lambda self:time.strftime("%Y-%m-%d"))
	company_id = fields.Many2one(comodel_name ="res.company",string="Company")
	uraian_ids = fields.One2many(comodel_name ="adhimix.mrp.pengiriman.detail",inverse_name ="reference",string="Uraian")
	produk_silo_ids = fields.One2many(comodel_name="adhimix.mrp.pengiriman.produk.silo",inverse_name="reference",string="Produk Silo")
	produk_cold_bin_ids = fields.One2many(comodel_name="adhimix.mrp.pengiriman.produk.cold.bin",inverse_name="reference",string="Produk Cold Bin")
	produk_silo_mobile_ids = fields.One2many(comodel_name="adhimix.mrp.produk.silo.mobile",inverse_name="reference",string="Produk Silo Mobile")
	aksesoris_drum_mixer_ids = fields.One2many(comodel_name="adhimix.mrp.aksesoris.drum.mixer",inverse_name="reference",string="Aksesoris Drum Mixer")


class adh_mrp_pengiriman_detail(models.Model):
	_name ="adhimix.mrp.pengiriman.detail"
	
	reference = fields.Many2one(comodel_name = "adhimix.mrp.pengiriman",string="Reference")
	uraian_id = fields.Many2one(comodel_name="adhimix.mrp.pengiriman.detail.uraian", string="Uraian")
	kriteria_id = fields.Many2one(comodel_name="adhimix.mrp.pengiriman.detail.kriteria", string="Kriteria")
	hasil_1 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 1")
	hasil_2 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 2")
	keterangan = fields.Char(string="Keterangan")
	
	
class adh_mrp_pengiriman_detail_uraian(models.Model):
	_name ="adhimix.mrp.pengiriman.detail.uraian"

	name = fields.Char(string="Uraian")	

class adh_mrp_pengiriman_detail_kriteria(models.Model):
	_name ="adhimix.mrp.pengiriman.detail.kriteria"	

	name = fields.Char(string="Kriteria")

	


class adh_mrp_pengiriman_produk_silo(models.Model):
	_name = "adhimix.mrp.pengiriman.produk.silo"

	reference = fields.Many2one(comodel_name="adhimix.mrp.pengiriman",string="Reference")
	uraian_id = fields.Many2one(comodel_name="adhimix.mrp.pengiriman.produk.silo.detail.uraian", string="Uraian")
	kriteria_id = fields.Many2one(comodel_name="adhimix.mrp.pengiriman.produk.silo.detail.kriteria", string="Kriteria")
	toleransi = fields.Char(string="Toleransi")
	hasil_1 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 1")
	hasil_2 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 2")
	keterangan = fields.Char(string="Keterangan")
	aksesoris_silo_id = fields.Many2one(comodel_name="adhimix.mrp.aksesoris.silo",string="Aksesoris Silo")

class adh_mrp_pengiriman_produk_silo_detail_uraian(models.Model):
	_name ="adhimix.mrp.pengiriman.produk.silo.detail.uraian"

	name = fields.Char(string="Uraian")

class adh_mrp_pengiriman_produk_silo_detail_kriteria(models.Model):
	_name = "adhimix.mrp.pengiriman.produk.silo.detail.kriteria"

	name = fields.Char(string="Kriteria")

class adh_mrp_aksesoris_silo(models.Model):
	_name = "adhimix.mrp.aksesoris.silo"

	name = fields.Char(string="Aksesoris Silo")
	kriteria_id = fields.Many2one(comodel_name="adhimix.mrp.pengiriman.produk.silo.detail.kriteria", string="Kriteria")
	toleransi = fields.Char(string="Toleransi")
	hasil_1 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 1")
	hasil_2 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 2")
	keterangan = fields.Char(string="Keterangan")

	

	

class adh_mrp_pengiriman_produk_cold_bin(models.Model):
	_name = "adhimix.mrp.pengiriman.produk.cold.bin"

	reference = fields.Many2one(comodel_name="adhimix.mrp.pengiriman",string="Reference")
	uraian_id = fields.Many2one(comodel_name="adhimix.mrp.pengiriman.produk.cold.bin.detail.uraian", string="Uraian")
	kriteria_id = fields.Many2one(comodel_name="adhimix.mrp.pengiriman.produk.cold.bin.detail.kriteria", string="Kriteria")
	toleransi = fields.Char(string="Toleransi")
	hasil_1 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 1")
	hasil_2 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 2")
	keterangan = fields.Char(string="Keterangan")

class adh_mrp_pengiriman_produk_cold_bin_detail_uraian(models.Model):
	_name ="adhimix.mrp.pengiriman.produk.cold.bin.detail.uraian"

	name = fields.Char(string="Uraian")

class adh_mrp_pengiriman_produk_cold_bin_detail_kriteria(models.Model):
	_name ="adhimix.mrp.pengiriman.produk.cold.bin.detail.kriteria"

	name = fields.Char(string="Kriteria")
	


class adh_mrp_produk_silo_mobile(models.Model):
	_name = "adhimix.mrp.produk.silo.mobile"

	reference = fields.Many2one(comodel_name ="adhimix.mrp.pengiriman",string="Reference")
	uraian_id = fields.Many2one(comodel_name ="adhimix.mrp.produk.silo.mobile.detail.uraian", string="Uraian")
	kriteria_id = fields.Many2one(comodel_name ="adhimix.mrp.produk.silo.mobile.detail.kriteria", string="Kriteria")
	toleransi = fields.Char(string="Toleransi")
	hasil_1 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 1")
	hasil_2 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 2")
	keterangan = fields.Char(string="Keterangan")
	aksesoris_silo_mobile_id = fields.Many2one(comodel_name="adhimix.mrp.aksesoris.silo.mobile",string="Aksesoris Silo Mobile")

class adh_mrp_produk_silo_mobile_detail_uraian(models.Model):
	_name ="adhimix.mrp.produk.silo.mobile.detail.uraian"

	name = fields.Char(string="Uraian")

class adh_mrp_produk_silo_mobile_detail_kriteria(models.Model):
	_name ="adhimix.mrp.produk.silo.mobile.detail.kriteria"

	name = fields.Char(string="Kriteria")

class adh_mrp_aksesoris_silo_mobile(models.Model):
	_name = "adhimix.mrp.aksesoris.silo.mobile"

	name = fields.Char(string="Aksesoris Silo Mobile")
	kriteria_id = fields.Many2one(comodel_name="adhimix.mrp.produk.silo.mobile.detail.kriteria", string="Kriteria")
	toleransi = fields.Char(string="Toleransi")
	hasil_1 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 1")
	hasil_2 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 2")
	keterangan = fields.Char(string="Keterangan")




class adh_mrp_aksesoris_drum_mixer(models.Model):
	_name = "adhimix.mrp.aksesoris.drum.mixer"

	reference = fields.Many2one(comodel_name="adhimix.mrp.pengiriman",string="Reference")
	uraian_id = fields.Many2one(comodel_name="aksesoris.drum.mixer.detail.uraian", string="Uraian")
	kriteria_id = fields.Many2one(comodel_name="aksesoris.drum.mixer.detail.kriteria", string="Kriteria")
	toleransi = fields.Char(string="Toleransi")
	hasil_1 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 1")
	hasil_2 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 2")
	keterangan = fields.Char(string="Keterangan")

class adh_mrp_aksesoris_drum_mixer_detail_uraian(models.Model):
	_name ="aksesoris.drum.mixer.detail.uraian"

	name = fields.Char(string="Uraian")

class adh_mrp_aksesoris_drum_mixer_detail_kriteria(models.Model):
	_name ="aksesoris.drum.mixer.detail.kriteria"

	name = fields.Char(string="Kriteria")




	
