from odoo import fields,api,models,_

class kesiapan_alat_wizard(models.TransientModel):

    _name = "kesiapan.alat.wizard"
    _description = "Kesiapan Alat Dan Bahan"

 

    # @api.multi
    # def kesiapan_alat_report(self):
    # 	# print "wakwawwkakwakwkakwkakwkkawkkak"
    # 	return self.env['report'].get_action(self, 'adh_mrp_instalasi.report_kesiapan_alat')


    # def _default_start_date(self):
    # """ Find the earliest start_date of the latests sessions """
    # # restrict to configs available to the user
    # config_ids = self.env['pos.config'].search([]).ids
    # # exclude configs has not been opened for 2 days
    # self.env.cr.execute("""
    #     SELECT
    #     max(start_at) as start,
    #     config_id
    #     FROM pos_session
    #     WHERE config_id = ANY(%s)
    #     AND start_at > (NOW() - INTERVAL '2 DAYS')
    #     GROUP BY config_id
    # """, (config_ids,))
    # latest_start_dates = [res['start'] for res in self.env.cr.dictfetchall()]
    # # earliest of the latest sessions
    # return latest_start_dates and min(latest_start_dates) or fields.Datetime.now()

    start_date = fields.Datetime(required=True,)
    end_date = fields.Datetime(required=True, default=fields.Datetime.now)
    alat_id = fields.Many2one('adhimix.mrp.instalasi',)

    @api.onchange('start_date')
    def _onchange_start_date(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            self.end_date = self.start_date

    @api.onchange('end_date')
    def _onchange_end_date(self):
        if self.end_date and self.end_date < self.start_date:
            self.start_date = self.end_date

    @api.multi
    def kesiapan_alat_report(self):
        data = {'date_start': self.start_date, 'date_stop': self.end_date, 'alat_id': self.alat_id.id}
        return self.env['report'].get_action(
            [], 'adh_mrp_instalasi.report_kesiapan_alat', data=data)
