# -*- coding: utf-8 -*-
{
    "name": "Stock Picking Totals Report",
    "version": "17.0.0.0.0",
    "category": "Inventory",
    "summary": "Pick docket showing total qty per product and stock available per source location",
    "description": """
Stock Picking Totals Report
=======================================

Replaces the standard stock picking report (which lists one line per lot/serial)
with a cleaner pick docket designed for warehouse pickers and barcode scanning
workflows.

Features
--------
* One row per product showing the TOTAL quantity required
* Per-product breakdown listing each source location and the qty reserved there
* Lot/serial numbers are intentionally omitted — the pick docket is the source
  of truth for quantities; the barcode scanning app is the source of truth for
  which serials are scanned
* Works alongside the product_hide_cost module which provides the base template

Technical Details
-----------------
* Inherits stock.report_picking (as overridden by product_hide_cost)
* Uses stock.move records (one per product) for the total quantity
* Groups stock.move.line records by location_id to build the location breakdown
* No Python model changes required — pure QWeb template inheritance

Author: John Ashurst
Company: SJR Nebula
Website: https://sjr.ie
Email: info@sjr.ie
    """,
    "author": "SJR Nebula",
    "website": "https://sjr.ie",
    "email": "info@sjr.ie",
    "depends": ["stock"],
    "data": [
        "views/stock_picking_report_views.xml",
    ],
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
