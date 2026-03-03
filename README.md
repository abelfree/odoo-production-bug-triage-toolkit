# Odoo Production Bug Triage Toolkit

[![Odoo](https://img.shields.io/badge/Odoo-16%2B-5E2750)](https://www.odoo.com/)
[![License: LGPL-3.0](https://img.shields.io/badge/License-LGPL--3.0-blue.svg)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-Portfolio_Ready-brightgreen)](#)
[![Last Commit](https://img.shields.io/github/last-commit/abelfree/odoo-production-bug-triage-toolkit)](https://github.com/abelfree/odoo-production-bug-triage-toolkit/commits/master)


## Problem
Production incidents in Odoo environments need fast triage, reliable documentation, and safe mitigations. Ad hoc incident handling leads to repeat outages.

## Solution
This project introduces a structured incident model and a practical SQL slow-log helper script.

## What It Demonstrates
- Incident lifecycle tracking with severity and status
- Support-friendly fields for root cause and mitigation notes
- Slow query scanning utility for PostgreSQL logs
- Playbook template for urgent blocker response

## Architecture
- `addons/ops_triage/models/incident_record.py`
- `scripts/scan_slow_log.ps1`
- `docs/incident_playbook.md`

## Demo Flow
1. Install addon and create example incidents.
2. Simulate support workflow from `open` to `resolved`.
3. Run `scripts/scan_slow_log.ps1 -LogPath <path>` on sample logs.
4. Apply playbook steps for SEV1 and SEV2 scenarios.

## Portfolio Talking Points
- How standard triage data improves post-incident analysis.
- Practical ways to reduce blocker resolution time.
- Safe hotfix workflow expectations for ERP systems.


## Screenshots

![Project Screenshot](assets/screenshots/placeholder.svg)

Replace ssets/screenshots/placeholder.svg with real screenshots from your Odoo demo environment.

