{
	"name": "Produksi - Install Produk", 
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
	"description": "Module yang digunakan untuk daftar Install produk produk di Divisi Produksi",
	"data": [
		"menu.xml",
		"view/instalasi_view.xml",
		"wizard/kesiapan_produk_wizard.xml",
		# "report/pondasi_report.xml",
		"wizard/kesiapan_alat_wizard.xml",
	],
	"installable": True,
	"auto_install": False,
	"application" : True,
}