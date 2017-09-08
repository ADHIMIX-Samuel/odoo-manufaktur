from odoo import api,fields,models,_ 
import time


class adh_mrp_seleksi_subkontraktor(models.Model):
	_name ="adhimix.mrp.seleksi.subkontraktor"

	name = fields.Char(string="No Dokumen")
	tanggal_efektif = fields.Date(string="Tanggal Efektif",default=lambda self:time.strftime("%Y-%m-%d"))
	nama_subkontraktor = fields.Char(string="Nama Sub Kontraktor")
	contact_person = fields.Char(string="Contact Person")
	alamat = fields.Char(string="Alamat")
	telepon = fields.Char(string="Telepon")
	fax = fields.Char(string="Fax")
	supplai_utama = fields.Char(string="Supplai Utama")
	company_id = fields.Many2one(comodel_name="res.company",string="Company")

	# Surat-surat ijin perusahaan
	akte_notaris_ya = fields.Boolean("Ya")
	akte_notaris_tidak = fields.Boolean("Tidak")
	akte_notaris_keterangan = fields.Char("Keterangan")

	siup_ya = fields.Boolean("Ya")
	siup_tidak = fields.Boolean("Tidak")
	siup_keterangan = fields.Char("Keterangan")

	pengukuhan_pengusaha_ya = fields.Boolean("Ya")
	pengukuhan_pengusaha_tidak = fields.Boolean("Tidak")
	pengukuhan_pengusaha_keterangan = fields.Char("Keterangan")

	tanda_daftar_ya = fields.Boolean("Ya")
	tanda_daftar_tidak = fields.Boolean("Tidak")
	tanda_daftar_keterangan = fields.Char("Keterangan")

	kartu_nomor_pajak_ya = fields.Boolean("Ya")
	kartu_nomor_pajak_tidak = fields.Boolean("Tidak")
	kartu_nomor_pajak_keterangan = fields.Char("Keterangan")

	sijk_ya = fields.Boolean("Ya")
	sijk_tidak = fields.Boolean("Tidak")
	sijk_keterangan =fields.Char("Keterangan")

	# Jumlah pekerjaan yang telah / dalam kontrak

	sd_15jt_ya = fields.Boolean("Ya")
	sd_15jt_tidak = fields.Boolean("Tidak")
	sd_15jt_keterangan = fields.Char("Keterangan")

	s15_50jt_ya = fields.Boolean("Ya")
	s15_50jt_tidak = fields.Boolean("Tidak")
	s15_50jt_keterangan = fields.Char("Keterangan")

	s50_200jt_ya = fields.Boolean("Ya")
	s50_200jt_tidak = fields.Boolean("Tidak")
	s50_200jt_keterangan = fields.Char("Keterangan")

	up_200jt_ya = fields.Boolean("Ya")
	up_200jt_tidak = fields.Boolean("Tidak")
	up_200jt_keterangan = fields.Char("Keterangan")

	# Kemampuan yang dimiliki

	peralatan_kerja_ya = fields.Boolean("Ya")
	peralatan_kerja_tidak = fields.Boolean("Tidak")
	peralatan_kerja_keterangan = fields.Char("Keterangan")

	kualifikasi_peralatan_ya = fields.Boolean("Ya")
	kualifikasi_peralatan_tidak = fields.Boolean("Tidak")
	kualifikasi_peralatan_keterangan = fields.Char("Keterangan")

	tepat_waktu_ya = fields.Boolean("Ya")
	tepat_waktu_tidak = fields.Boolean("Tidak")
	tepat_waktu_keterangan = fields.Char("Keterangan")

	# Serifikasi
	sertifikasi_iso_9001 = fields.Boolean("ISO 9001(Quality)")
	sertifikasi_iso_9002 = fields.Boolean("ISO 9002(Quality)")
	sertifikasi_smk3 = fields.Boolean("SMK3(HSE)")
	sertifikasi_ohsas_18001 = fields.Boolean("OHSAS 18001 (HSE)")
	sertifikasi_iso_14000 = fields.Boolean("ISO 14000 (ENVIRONMENT)")

	# hasil
	hasil_lulus = fields.Boolean("Lulus")
	hasil_tidak_lulus = fields.Boolean("Tidak Lulus")




