{
	"name": "Produksi - Inspeksi Pengiriman", 
	"version": "1.0", 
	"depends": [
		"base",
		"product",
		"mrp",
	], 
	"author": "PT.WITACO -Samuel-Haerul",
	"website": "https://www.adhimix.co.id",
	"category": "Pengiriman Produk",
	"summary": "Divisi Produksi PT.Adhimix Indonesia",
	"description": "Module yang digunakan untuk daftar Pengiriman produk di Divisi Produksi",
	"data": [
		"menu.xml",
		"view/pengiriman_view.xml",
		# "report/klaim_report.xml",
		"wizard/pengiriman_wizard.xml",
	],
	"installable": True,
	"auto_install": False,
	"application" : True,
}