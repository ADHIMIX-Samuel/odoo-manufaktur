from odoo import api,fields,models,_ 
import time


class adh_mrp_ketidaksesuian_produk(models.Model):
	_name = "adhimix.mrp.ketidaksesuaian.produk"

	name = fields.Char("No Dokumen",required=True)
	tanggal_efektif = fields.Date("Tanggal Efektif", default=lambda self:time.strftime("%Y-%m-%d"))
	no_nc = fields.Char("No NC",required=True)
	tanggal_nc = fields.Date("Tanggal NC",required=True)
	tanggal_realisasi_produk = fields.Date("Tanggal Realisasi Produk",required=True)
	nama_pekerjaan = fields.Char("Nama Pekerjaan")
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	nama_pelanggan =fields.Many2one(comodel_name="res.partner",string="Nama Pelanggan",required=True)
	ketidaksesuaian_produk = fields.Selection([('Internal','Internal'),('Eksternal','Eksternal')]
												,string="Ketidaksesuaian Produk",required=True)
	pic = fields.Char("PIC")
	penjelasan = fields.Char("Penjelasan")
	ketidaksesuaian = fields.Text("Ketidaksesuaian")
	jenis_nc = fields.Selection([('Alat','Alat'),('Bahan','Bahan'),('Lingkungan','Lingkungan'),
								('Metode','Metode'),('SDM','SDM'),('Lainnya','Lainnya')],string="Jenis NC")


	# Penyebab Masalah
	penyebab = fields.Char("Penyebab")
	ketidaksesuaian_penyebab = fields.Text("Ketidaksesuaian")
	kesimpulan_ketidaksesuian = fields.Selection([('Alat','Alat'),('Bahan','Bahan'),('Lingkungan','Lingkungan'),
								('Metode','Metode'),('SDM','SDM'),('Lainnya','Lainnya')],string="Kesimpulan Ketidaksesuaian")


	# rencana tindak lanjut
	rencana_tindak_lanjut = fields.Selection([('Reject','Reject'),('Repair','Repair')],string="Rencana Tindak Lanjut")
	penjelasan_tindak_lanjut = fields.Text("Penjelasan Tindak Lanjut")
	rencana_selesai = fields.Char("Rencana Selesai")
	pic_rencana_tindak_lanjut = fields.Char("PIC")
	tindakan_pencegahan = fields.Char("Tindakan Pencegahan(Jika Ada)")



	# penyelesaian masalah
	realisasi_penyelesaian = fields.Text("Realisasi Penyelesaian")
	tanggal_penyelesaian = fields.Date("Tanggal Penyelesaian")
	biaya_yg_timbul = fields.Char("Biaya Yang Timbul")
	status = fields.Selection([('Open','Open'),('Close','Close')],string="Status") 



