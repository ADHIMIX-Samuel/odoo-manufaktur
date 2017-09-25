from odoo import fields,api,models,_

class ketidaksesuaian_produk_wizard(models.TransientModel):

    _name = "ketidaksesuaian.produk.wizard"
    _description = "ketidaksesuaian produk wizard"

    start_date = fields.Datetime(required=True)
    # tanggal_informasi = fields.Date(string="Tanggal Infomasi",required=True)
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
    def generate_report(self):
        data = {'date_start': self.start_date, 'date_stop': self.end_date}
        # data = {'tanggal_informasi':self.tanggal_informasi}
        return self.env['report'].get_action(
            [], 'adh_manufaktur.report_ketidaksesuain_produk',data=data)


   
