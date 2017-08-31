from odoo import api,fields,models,_

class adh_mrp_instalasi(models.Model):
	_name ="adhimix.mrp.instalasi"

	name = fields.Char(string="No Dokumen")
	tanggal = fields.Date(string="Tanggal")
	lokasi_install = fields.Char(string="Lokasi Install")
	nama_pekerjaan = fields.Char(string="Nama Pekerjaan")
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	install_produk_ids = fields.One2many(comodel_name="adhimix.mrp.instalasi.produk",inverse_name="reference",
						string="Kesiapan Alat Dan Bahan")

class adh_mrp_intsalasi_produk(models.Model):
	_name = "adhimix.mrp.instalasi.produk"

	reference = fields.Many2one(comodel_name="adhimix.mrp.instalasi",string="Reference")
	uraian_id = fields.Many2one(comodel_name="adhimix.mrp.instalasi.detail.uraian",string="Uraian")
	kriteria_id = fields.Many2one(comodel_name="adhimix.mrp.instalasi.detail.kriteria",string="Kriteria")
	hasil_oke = fields.Boolean(string="Oke")
	hasil_tidak_oke = fields.Boolean(string="Tidak Oke")
	keterangan = fields.Char(string="Keterangan")


			

class adh_mrp_instalasi_produk_detail_uraian(models.Model):
	_name = "adhimix.mrp.instalasi.detail.uraian"

	name = fields.Char(string="Uraian")

class adh_mrp_instalasi_produk_detail_kriteria(models.Model):
	_name = "adhimix.mrp.instalasi.detail.kriteria"

	name = fields.Char(string="Kriteria")





class adh_mrp_kesiapan_pondasi_produk(models.Model):
	_name ="adhimix.mrp.kesiapan.pondasi.produk"

	name = fields.Char(string="No Dokumen")
	tanggal = fields.Date(string="Tanggal")
	lokasi_install = fields.Char(string="Lokasi Install")
	nama_pekerjaan = fields.Char(string="Nama Pekerjaan")
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	produk_silo_coldbin_ids = fields.One2many(comodel_name="adhimix.mrp.instalasi.silo",inverse_name="reference",
						string="Kesiapan Pondasi Produk")




class adh_mrp_instalasi_silo(models.Model):
	_name="adhimix.mrp.instalasi.silo"

	reference= fields.Many2one(comodel_name="adhimix.mrp.instalasi",string="Reference")
	uraian_id = fields.Many2one(comodel_name="adhimix.mrp.instalasi.silo.detail.uraian",string="Uraian")
	kriteria_id = fields.Many2one(comodel_name="adhimix.mrp.instalasi.silo.detail.kriteria",string="Kriteria")
	hasil_oke = fields.Boolean(string="Oke")
	hasil_tidak_oke = fields.Boolean(string="Tidak Oke")
	keterangan = fields.Char(string="Keterangan")

class adh_mrp_instalasi_silo_detail_uraian(models.Model):
	_name = "adhimix.mrp.instalasi.silo.detail.uraian"

	name = fields.Char(string="Uraian")

class adh_mrp_instalasi_silo_detail_kriteria(models.Model):
	_name = "adhimix.mrp.instalasi.silo.detail.kriteria"

	name = fields.Char(string="Kriteria")
