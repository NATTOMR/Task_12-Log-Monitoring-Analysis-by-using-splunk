# 📊 Splunk SOC Security Dashboard

This directory documents the 5-panel interactive **Splunk SOC Security Dashboard** built for Project P1.

> **Note on Source Format:** In accordance with lab standards, because the original dashboard was created dynamically within Splunk Enterprise Web UI without an exported XML definition, this document provides the exact panel layout, visualization specifications, underlying SPL queries, and step-by-step instructions to recreate the dashboard in any Splunk instance.

---

## Dashboard Overview

- **Dashboard Title:** Splunk SOC Security Dashboard
- **Target Index:** `index=main`
- **Sourcetype:** `_json`
- **Data Source:** `data/ssh_logs.json` (1,200 events)
- **Primary Objective:** Provide SOC Tier 1/Tier 2 analysts with real-time situational awareness across authentication volume, failed attempts, adversary IP rankings, and target asset exposure.

![SOC Dashboard](../screenshots/soc-dashboard.jpeg)

---

## Panel Breakdown & SPL Definitions

### Panel 1: Total SSH Log Volume
- **Visualization Type:** Single Value Metric
- **Screenshot:** [`screenshots/dashboard-panel-01.jpeg`](../screenshots/dashboard-panel-01.jpeg)
- **Security Purpose:** Quick-glance visibility into the total volume of ingested telemetry events.
- **SPL Query:**
  ```spl
  index=main | stats count
  ```
- **Expected Value:** `1,200` total events.

---

### Panel 2: Authentication Status Breakdown
- **Visualization Type:** Pie Chart
- **Screenshot:** [`screenshots/dashboard-panel-02.jpeg`](../screenshots/dashboard-panel-02.jpeg)
- **Security Purpose:** Visualizes the proportion of successful sessions versus brute-force failures and unauthenticated probes.
- **SPL Query:**
  ```spl
  index=main | stats count by event_type
  ```
- **Expected Distribution:**
  - `Successful SSH Login`: 306 (25.50%)
  - `Failed SSH Login`: 305 (25.42%)
  - `Multiple Failed Authentication Attempts`: 303 (25.25%)
  - `Connection Without Authentication`: 286 (23.83%)

---

### Panel 3: Attacker IP Ranking (Top Threat Actors)
- **Visualization Type:** Bar Chart / Column Chart
- **Screenshot:** [`screenshots/dashboard-panel-03.jpeg`](../screenshots/dashboard-panel-03.jpeg)
- **Security Purpose:** Ranks top offending source IP addresses generating authentication failures to accelerate firewall containment.
- **SPL Query:**
  ```spl
  index=main auth_success=false OR event_type="Multiple Failed Authentication Attempts"
  | stats count as failed_attempts by id.orig_h
  | where failed_attempts > 5
  | sort - failed_attempts
  ```
- **Top Sources Identified:** `10.0.0.25` (31 failures), `10.0.0.18` (29 failures), `10.0.0.46` (27 failures).

---

### Panel 4: Server Load & Target Distribution
- **Visualization Type:** Column Chart
- **Screenshot:** [`screenshots/dashboard-panel-04.jpeg`](../screenshots/dashboard-panel-04.jpeg)
- **Security Purpose:** Maps which internal server assets are experiencing the highest concentration of connection attempts.
- **SPL Query:**
  ```spl
  index=main 
  | stats count by id.resp_h
  | sort - count
  ```
- **Primary Targets:** `10.0.1.6` (115 events), `10.0.1.2` (115 events), `10.0.1.9` (113 events).

---

### Panel 5: Event Velocity Timechart
- **Visualization Type:** Line Graph / Timechart
- **Screenshot:** [`screenshots/dashboard-panel-05.jpeg`](../screenshots/dashboard-panel-05.jpeg)
- **Security Purpose:** Monitors connection and attack velocity across time buckets to spot attack bursts and peak attack intervals.
- **SPL Query:**
  ```spl
  index=main 
  | timechart count by event_type
  ```

---

## How to Recreate This Dashboard in Splunk Web

1. Open your Splunk Enterprise web interface (`http://localhost:8000`).
2. Navigate to **Search & Reporting**.
3. In the top navigation bar, click **Dashboards** → **Create New Dashboard**.
4. Set Dashboard Title to: `Splunk SOC Security Dashboard`.
5. Select **Classic (Simple XML)** or **Dashboard Studio** (Grid layout).
6. Click **Add Panel** for each of the 5 panels above:
   - Paste the corresponding SPL query.
   - Select the specified visualization (Single Value, Pie Chart, Bar Chart, Column Chart, Line Chart).
   - Set the Time Range to **All Time** (or the timestamp range matching the ingested dataset).
7. Save the dashboard and inspect panels against the reference screenshots in [`screenshots/`](../screenshots/).
