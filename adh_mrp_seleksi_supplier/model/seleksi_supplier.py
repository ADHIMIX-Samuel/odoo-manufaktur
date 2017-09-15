from odoo import api,fields,models,_ 
import time

class adh_mrp_seleksi_supplier(models.Model):
	_name = "adhimix.mrp.seleksi.supplier"


	name = fields.Char(string="No Dokumen",required=True)
	tanggal_efektif = fields.Date(string="Tanggal Efektif",default=lambda self:time.strftime("%Y-%m-%d"))
	nama_vendor = fields.Char(string="Nama Vendor")
	alamat = fields.Char(string="Alamat")
	contact_person = fields.Char(string="Contact Person")
	telepon = fields.Char(string="Telepon")
	fax = fields.Char(string="Fax")
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	supply_material = fields.Boolean(string="Supply Material")
	supply_peralatan = fields.Boolean(string="Supply Peralatan")
	keterangan = fields.Selection([('Keagenan','Keagenan'),('Distributor','Distributor'),
									('Pabrik','Pabrik'),('Toko','Toko')],string="Keterangan")
	peralatan_konstruksi = fields.Boolean(string="Peralatan Konstruksi")
	peralatan_ringan = fields.Boolean(string="Peralatan Ringan")
	peralatan_transportasi = fields.Boolean(string="Peralatan Transportasi/Investasi")

	# material dan peralatan
	pemenuhan_terhadap_spesifikasi_ya = fields.Boolean(string="Ya")
	pemenuhan_terhadap_spesifikasi_tidak = fields.Boolean(string="Tidak")
	pemenuhan_terhadap_spesifikasi_keterangan = fields.Char(string="Keterangan")

	kapasitas_produksi_ya = fields.Boolean(string="Ya")
	kapasitas_produksi_tidak = fields.Boolean(string="Tidak")
	kapasitas_produksi_keterangan = fields.Char(string="Keterangan")

	kemampuan_supply_ya = fields.Boolean(string="Ya")
	kemampuan_supply_tidak = fields.Boolean(string="Tidak")
	kemampuan_supply_keterangan = fields.Char(string="Keterangan")

	ketepatan_pengiriman_barang_ya = fields.Boolean(string="Ya")
	ketepatan_pengiriman_barang_tidak = fields.Boolean(string="Tidak")
	ketepatan_pengiriman_barang_keterangan = fields.Char(string="Keterangan")

	jumlah_armada_ya = fields.Boolean(string="Ya")
	jumlah_armada_tidak = fields.Boolean(string="Tidak")
	jumlah_armada_keterangan = fields.Char(string="Keterangan")

	produsen_ya = fields.Boolean(string="Ya")
	produsen_tidak = fields.Boolean(string="Tidak")
	produsen_keterangan = fields.Char(string="Keterangan")

	# peralatan

	popularitas_ya = fields.Boolean(string="Ya")
	popularitas_tidak = fields.Boolean(string="Tidak")
	popularitas_keterangan = fields.Char(string="Keterangan")

	pelayanan_purna_jual_ya = fields.Boolean(string="Ya")
	pelayanan_purna_jual_tidak = fields.Boolean(string="Tidak")
	pelayanan_purna_jual_keterangan = fields.Char(string="Keterangan")

	kesediaan_suku_cadang_ya = fields.Boolean("Ya")
	kesediaan_suku_cadang_tidak = fields.Boolean("Tidak")
	kesediaan_suku_cadang_keterangan = fields.Char("Keterangan")

	kemudahan_perbaikan_ya = fields.Boolean("Ya")
	kemudahan_perbaikan_tidak = fields.Boolean("Tidak")
	kemudahan_perbaikan_keterangan  = fields.Char("Keterangan")

	kondisi_umum_ya = fields.Boolean("Ya")
	kondisi_umum_tidak = fields.Boolean("Tidak")
	kondisi_umum_keterangan = fields.Char("Keterangan")


	# Serifikasi
	sertifikasi_iso_9001 = fields.Boolean("ISO 9001(Quality)")
	sertifikasi_iso_9002 = fields.Boolean("ISO 9002(Quality)")
	sertifikasi_smk3 = fields.Boolean("SMK3(HSE)")
	sertifikasi_ohsas_18001 = fields.Boolean("OHSAS 18001 (HSE)")
	sertifikasi_iso_14000 = fields.Boolean("ISO 14000 (ENVIRONMENT)")

	# hasil
	hasil_lulus = fields.Boolean("Lulus")
	hasil_tidak_lulus = fields.Boolean("Tidak Lulus")
	


