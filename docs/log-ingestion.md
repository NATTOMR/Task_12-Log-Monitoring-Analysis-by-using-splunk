# 📥 Log Ingestion & Data Management

This document details the log ingestion procedure, dataset schema, and parsing configuration for **P1 — Splunk SOC Home Lab & Log Analysis**.

---

## Ingestion Status

- **Direct Web Ingestion:** ✅ **IMPLEMENTED** (Utilized for the 1,200-event `data/ssh_logs.json` dataset).
- **Universal Forwarder Pipeline:** ⚪ **PLANNED** (Documented in `configs/inputs.conf.example` for P2/P3).

---

## Dataset Profile: `data/ssh_logs.json`

- **Format:** Structured JSON objects (one event per line).
- **Total Event Count:** 1,200 events.
- **Protocol:** TCP / SSH (Port 22).
- **File Location:** [`data/ssh_logs.json`](../data/ssh_logs.json)

### Key Extracted Fields:
| Field Name | Type | Description | Sample Value |
|---|---|---|---|
| `ts` | String (ISO 8601) | Event UTC Timestamp | `2025-04-24T10:20:09.508780Z` |
| `uid` | String | Unique Session Identifier | `SH4886434` |
| `id.orig_h` | IP | Source / Attacker IP | `10.0.0.43` |
| `id.orig_p` | Integer | Originating Client Port | `58221` |
| `id.resp_h` | IP | Destination / Server IP | `10.0.1.6` |
| `id.resp_p` | Integer | Destination Port | `22` |
| `proto` | String | Network Protocol | `tcp` |
| `auth_success` | Boolean | Authentication Result | `true` / `false` / `null` |
| `auth_attempts`| Integer | Password Attempts in Session | `1`, `3`, `8` |
| `event_type` | String | Security Event Category | `Multiple Failed Authentication Attempts` |

---

## Step-by-Step Ingestion Workflow

1. Navigate to **Settings** → **Add Data** in the Splunk Web interface.
2. Select **Upload files from my computer**.
3. Select [`data/ssh_logs.json`](../data/ssh_logs.json).
4. On the **Set Source Type** step:
   - Splunk automatically detects JSON objects. Select `_json` (or verify key-value extractions).
5. On the **Input Settings** step:
   - Set **Index** to `main`.
6. Review the summary and click **Submit**.
7. Validate ingestion by running:
   ```spl
   index=main | stats count
   ```
   Confirm result equals `1,200`.
