from odoo import fields,api,models,_
from odoo.exceptions import UserError

class klaim_wizard(models.TransientModel):

	_name = "klaim.wizard"
	_description = "Komplain/Klaim Wizard"


	# tanggal_penerimaan = fields.Date(string="Tanggal Penerimaan",required=True)
	start_date = fields.Datetime(required=True)
	end_date = fields.Datetime(required=True, default=fields.Datetime.now)

	@api.onchange('start_date')
	def _onchange_start_date(self):
		if self.start_date and self.end_date and self.end_date < self.start_date:
			self.end_date = self.start_date

	@api.onchange('end_date')
	def _onchange_end_date(self):
		if self.end_date and self.end_date < self.start_date:
			self.start_date = self.end_date


 

	@api.multi
	def klaim_report(self,data):
		# data = {'tanggal_penerimaan': self.tanggal_penerimaan}
		data = {'date_start': self.start_date, 'date_stop': self.end_date}
		return self.env['report'].get_action(
			[], 'adh_mrp_pemasaran_klaim.report_klaim_pelanggan', data=data)
		