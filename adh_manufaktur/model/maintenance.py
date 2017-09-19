from odoo import api,fields,models,_
import time

Mtc_STATES =[('Draft','Draft'),('Progress','Progress'),('Done','Done')]
class adhimix_mrp_maintenance(models.Model):
	_name = "adhimix.mrp.maintenance"

	name = fields.Char(string="Nomor Maintenance",readonly=True)
	tanggal_maintenance = fields.Date(string="Tanggal Maintenance",required=True,default=lambda self:time.strftime("%Y-%m-%d"))
	tanggal_selesai = fields.Date(string="Tanggal Selesai",readonly=True)
	dibuat_oleh = fields.Many2one (string="Dibuat Oleh",comodel_name="res.users",readonly=True,default=lambda self: self._uid)
	state = fields.Selection(string="Status", selection=Mtc_STATES, required=True,readonly=True,default=Mtc_STATES[0][0])
	sparepart_list = fields.One2many(comodel_name="adhimix.mrp.maintenance.sparepart",inverse_name="reference",string="Sparepart List")


	@api.multi
	def button_Draft(self):		
		self.state = Mtc_STATES[0][0]
        
	@api.multi
	def button_Progress(self):
		self.state = Mtc_STATES[1][0]
        
	@api.multi
	def button_Done(self):
		self.state = Mtc_STATES[2][0]


	@api.model
	def create(self,vals):
		vals['name'] = self.env['ir.sequence'].next_by_code('adhimix.mrp.maintenance')
		return super(adhimix_mrp_maintenance, self).create(vals)

class adhimix_mrp_maintenance_sparepart(models.Model):
	_name ="adhimix.mrp.maintenance.sparepart"

	reference = fields.Many2one(comodel_name="adhimix.mrp.maintenance",string="Maintenance ID")
	nama_barang = fields.Many2one(comodel_name="product.product",required=True,string="Nama Barang")
	qty = fields.Float(string="QTY",required=True,default="1.0")
	hpp = fields.Float(string="HPP",required=True)
	total_hpp = fields.Float(string="Total HPP",required=True,)
	
	@api.onchange('qty','hpp','total_hpp')
	def onchange_total_hpp(self):
		self.total_hpp =(self.qty * self.hpp)
	
	

	@api.onchange('nama_barang')
	def onchange_nama_barang(self):
			self.hpp = self.nama_barang.standard_price
