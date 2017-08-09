from odoo import api, fields, models, _

class adhimix_mrp_info_pasar(models.Model):
	_name = "adhimix.mrp.info.pasar"

	name = fields.Char(string="No",required=True)
	tanggal_informasi = fields.Date(string="Tanggal Informasi Pasar",required=True)
	nama_pelanggan = fields.Many2one(comodel_name="res.partner",string="Nama Pelanggan")
	nama_spesifikasi_produk = fields.Char(string="Nama/Spesifikasi Produk")
	volume = fields.Float(string="Volume(Buah)")
	tanggal_dibutuhkan = fields.Date(string="Tanggal di Butuhkan",required=True)
	lokasi = fields.Char(string="Lokasi")
	sumber_informasi_dari = fields.Selection([('OWNER','OWNER'),('REKANAN','REKANAN')],string="Dari")
	sumber_informasi_cara = fields.Selection([('BY PHONE','BY PHONE'),('DOOR TO DOOR','DOOR TO DOOR'),
										('MEDIA ELEKTRONIK','MEDIA ELEKTRONIK'),('MEDIA CETAK','MEDIA CETAK')],string="Cara")
	nama = fields.Char(string="Nama")
	telepon = fields.Char(string="Telepon")
	status = fields.Selection([('Terklarifikasi','Terklarifikasi'),('Belum Terklarifikasi','Belum Terklarifikasi')],string="Status") 
	ya = fields.Boolean(string="Ya")
	tidak = fields.Boolean(string="Tidak")
	tanggal = fields.Date(string="Tanggal")



