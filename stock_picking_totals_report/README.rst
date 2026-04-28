==============================
Stock Picking Totals Report
==============================

.. |badge1| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3

.. |badge2| image:: https://img.shields.io/badge/odoo-18.0-blueviolet
    :alt: Odoo 18.0

|badge1| |badge2|

Replaces the standard stock picking report with a cleaner pick docket designed
for warehouse pickers using barcode scanners. Instead of one row per lot/serial,
the report shows a single **total quantity** per product followed by a breakdown
of **source locations** and the stock available at each.

**Table of contents**

.. contents::
   :local:

Problem
=======

The standard Odoo picking report prints one line per lot/serial number
reservation. When a product is reserved from multiple lots spread across
multiple locations, this produces a long, confusing list - especially on a
handheld scanner screen.

Pickers need to know two things:

- **How many** of each product to pick (the total demand)
- **Where to find it** - which locations hold stock, and how much

The barcode scanning app is the source of truth for *which* serials are scanned.
The pick docket is the source of truth for *how many* to pick. Printing
lot/serial rows on the docket duplicates the scanner's job and adds noise.

Solution
========

The report is restructured so that for each product on the picking:

1. A bold header row shows the product name and the **total quantity required**.
2. Indented sub-rows list each unique **source location** and the qty reserved
   there.

Lot/serial number and product barcode columns are removed entirely.

Example Output
==============

=========================  =============  ==================
Product                    Qty Required   From
=========================  =============  ==================
**Widget A**               **10 units**
*Available at location*    6 units        Shelf 1-A
*Available at location*    4 units        Shelf 2-B
**Widget B**               **5 units**
*Available at location*    5 units        Main Stock
=========================  =============  ==================

Before vs After
===============

==============================  ==========================  ==============================
Feature                         Standard Odoo               With This Module
==============================  ==========================  ==============================
Row per lot/serial              Yes (cluttered)             Removed
Total qty per product           No                          Yes - bold header row
Source location per product     Spread across many rows     Grouped as sub-rows
Qty available per location      Mixed with lot/serial info  Clear sub-row per location
Lot/Serial and barcode columns  Present                     Removed
==============================  ==========================  ==============================

Installation
============

1. Ensure ``product_hide_cost`` is installed first.
2. Copy the ``stock_picking_totals_report`` folder to your Odoo addons directory.
3. Update the apps list: **Settings → Apps → Update Apps List**.
4. Search for *"Stock Picking Totals Report"* and install.

Configuration
=============

No configuration is required. Once installed the module automatically applies
to all stock picking reports.

Usage
=====

Print or preview a picking (delivery order, internal transfer, or receipt) as
normal. The report will show one product row per line with location sub-rows
beneath it.

If stock has not yet been reserved for a product, a warning sub-row is shown:
*"No stock reserved - check availability"*.

Features
========

- **Consolidated product rows** - one bold row per product showing total demand
- **Location breakdown** - sub-rows per source location with reserved qty
- **No lot/serial clutter** - serial scanning is handled by the barcode app
- **No Python required** - pure QWeb template inheritance, no model changes
- **Handles unreserved products** - warning row shown when no stock is reserved
- **Respects multi-location groups** - location columns only shown when the
  ``stock.group_stock_multi_locations`` group is active

Technical Notes
===============

The module works across a single QWeb template inheritance:

``report_picking_totals`` (inherits ``stock.report_picking``)
    - Removes ``th_serial_number`` and ``th_barcode`` column headers via XPath
    - Replaces the ``<tr t-as="ml">`` loop (per-move-line rows) with a new
      structure that iterates ``move_ids_without_package`` (one ``stock.move``
      per product)
    - For each move, calls ``move.move_line_ids.mapped('location_id')`` to
      obtain unique source locations, then sums ``quantity`` per location using
      a ``filtered()`` lambda

Support
=======

For support, please contact SJR Nebula:

- Website: https://sjr.ie
- Email: info@sjr.ie

Credits
=======

Authors
-------

* SJR Nebula

Contributors
------------

* John Ashurst
