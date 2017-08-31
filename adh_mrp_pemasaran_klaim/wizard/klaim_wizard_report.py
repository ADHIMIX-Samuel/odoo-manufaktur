from odoo import fields,api,models,_
from odoo.exceptions import UserError

class klaim_wizard(models.TransientModel):

	_name = "klaim.wizard"
	_description = "Komplain/Klaim Wizard"


	tanggal = fields.Date(string="Tanggal",required=True)

 

	@api.multi
	def klaim_report(self,data):
		data = {'tanggal': self.tanggal}
		return self.env['report'].get_action(
			[], 'adh_mrp_pemasaran_klaim.report_klaim_pelanggan', data=data)
		