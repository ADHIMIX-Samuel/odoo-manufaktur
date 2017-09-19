from odoo import api,fields,models,_ 
import time

class adh_mrp_evaluasi_penawaran(models.Model):
	_name = "adhimix.mrp.evaluasi.penawaran"

	name = fields.Char("No Dokumen",required=True)
	no_penawaran = fields.Char("No Penawaran",required=True)
	tanggal_penawaran = fields.Date("Tanggal Penawaran",required=True)
	nama_pelanggan = fields.Many2one(comodel_name="res.partner",string="Nama Pelanggan")
	nama_spesifikasi_produk = fields.Char("Nama Spesifikasi Produk")
	kontak_person = fields.Char("Kontak Person")
	status = fields.Selection([('Proses','Proses'),('Menang/Kontrak','Menang/Kontrak'),
								('Kalah','Kalah')],string="Status")
	penyebab_kekalahan = fields.Selection([('Harga','Harga'),('Waktu Pelaksanaan','Waktu Pelaksanaan'),
											('Lama Waktu Produksi/Perbaikan','Lama Waktu Produksi/Perbaikan'),
											('Kualitas Layanan(Pengalaman masa lalu)','Kualitas Layanan(Pengalaman masa lalu)'),
											],string="Penyebab Kekalahan")
	pic = fields.Char("PIC")
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	# period = fields.Char("Period")
	tanggal_efektif = fields.Date("Tanggal Efektif",default=lambda self:time.strftime("%Y-%m-%d"))
