from odoo import api,fields,models,_

class adh_mrp_klaim(models.Model):
	_name ="adhimix.mrp.klaim"

	name = fields.Char(string="No FORM")
	nama_pelanggan = fields.Char(string="Nama Pelanggan/Vendor")
	no_komplain = fields.Char(string="No Komplain/Klaim")
	tanggal_penerimaan = fields.Date(string="Tanggal Peneriman")
	jabatan = fields.Char(string="jabatan")
	nama_pelapor = fields.Char(string="Nama Pelapor")
	no_telp = fields.Char(string="No Telepon")
	uraian = fields.Text(string="Uraian")
	Komplain_klaim = fields.Text(string="Komplain/Klaim")
	tanggal = fields.Date(string="Tanggal")
	jenis_komplain = fields.Selection([('Mutu/Kualitas','Mutu/Kualitas'),('Waktu','Waktu'),
										('Pembayaran','Pembayaran'),('SDM','SDM'),('Lainnya','Lainnya')],
										string="Jenis Komplain")
	analisa_atas_komplain = fields.Text(string="Analisa Atas Komplain/Klaim")
	penyebab_yg_paling_mungkin = fields.Text(string="Penyebab Yang Paling Mungkin")
	upaya_tindakan = fields.Text(string="Upaya Tindakan Koreksi")
	rencana_selesai = fields.Char(string="Rencana Selesai")
	petugas = fields.Char(string="Petugas")
	selesai_tanggal = fields.Date(string="Selesai Tanggal")
	tanggal_pemberitahuan_penanganan = fields.Date(string="Tanggal Pemberitahuan Penanganan Komplain Ke Pelanggan/Vendor")
	status = fields.Selection([('Open','Open'),('Close','Close')],string="Status")
	realisasi_hasil_komplain= fields.Text(string="Realisasi Hasil Komplain")
	bagian_yang_menangani = fields.Selection([('Pemasaran','Pemasaran'),('Produksi','Produksi'),
											('Engineering','Engineering'),('Keuangan','Keuangan')],
											string="Bagian Yang Menangani")
	dinyatakan_selesai = fields.Char(string="Dinyatakan Selesai Oleh")
	komplain = fields.Boolean(string="Komplain")
	klaim = fields.Boolean(string="Klaim")
	company_id = fields.Many2one(comodel_name="res.company",string="Company")


	
	
