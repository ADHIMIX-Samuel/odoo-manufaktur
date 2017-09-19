from odoo import api,fields,models,_ 
import time

class adh_mrp_cost_control(models.Model):
	_name = "adhimix.mrp.cost.control"

	name = fields.Char(string="No Kontrak",required=True)
	pelanggan = fields.Many2one(comodel_name="res.partner",string="Pelanggan")
	proyek = fields.Char("Proyek")
	deadline_kontrak = fields.Date("Deadline Kontrak",required=True)
	subkon = fields.Many2one(comodel_name="res.partner",string="Subkon",domain=[('supplier','=',True)])
	id_cost_control = fields.Char("ID Cost Control")
	tanggal_efektif = fields.Date("Tanggal Efektif",default=lambda self:time.strftime("%Y-%m-%d"))
	company_id = fields.Many2one(comodel_name="res.company",string="Company")
	cost_control_ids = fields.One2many(comodel_name="adhimix.mrp.cost.control.line",inverse_name="reference",string="Reference")

class adh_mrp_cost_control_line(models.Model):
	_name ="adhimix.mrp.cost.control.line"

	reference = fields.Many2one(comodel_name="adhimix.mrp.cost.control")
	no_directory = fields.Char("No Directory Cost Control")
	uraian_id = fields.Many2one(comodel_name="product.product",string="Uraian")
	spesifikasi = fields.Char("Spesifikasi")
	om_biaya = fields.Float("O/M Biaya")
	om_jumlah = fields.Float("O/M Jumlah")

	# Rencana HPP
	jumlah_volume_hpp = fields.Float("Jumlah Volume")
	satuan_volume_hpp = fields.Many2one(string="Satuan Volume",comodel_name="product.uom")
	harga_hpp = fields.Float("Harga")
	total_harga_hpp = fields.Float("Total HPP")


	# Realisasi Saat ini
	jumlah_volume_realisasi = fields.Float("Jumlah Volume")
	satuan_volume_realisasi =fields.Many2one(string="Satuan Volume",comodel_name="product.uom")
	harga_realisasi = fields.Float("Harga")
	total_harga_realisasi = fields.Float("Total Realisasi")


	@api.onchange('jumlah_volume_hpp','harga_hpp','total_harga_hpp')
	def onchange_total_harga_hpp(self):
		self.total_harga_hpp =(self.jumlah_volume_hpp * self.harga_hpp)

	@api.onchange('jumlah_volume_realisasi','harga_realisasi','total_harga_realisasi')
	def onchange_total_harga_realisasi(self):
		self.total_harga_realisasi =(self.jumlah_volume_realisasi * self.harga_realisasi)
	






	


