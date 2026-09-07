# 🏗️ SOC Lab Architecture & Data Flow

This document details the environment architecture and data flow for **P1 — Splunk SOC Home Lab & Log Analysis**, serving as the foundation for the [Splunk SOC & Threat Hunting Portfolio](https://github.com/NATTOMR/splunk-soc-threat-hunting-lab).

---

## Architecture Implementation Status

- **Splunk Enterprise SIEM:** ✅ **IMPLEMENTED** (Single-instance deployment on Kali Linux).
- **Direct JSON Log Ingestion:** ✅ **IMPLEMENTED** (1,200 structured SSH telemetry events).
- **Interactive Security Dashboards:** ✅ **IMPLEMENTED** (5-panel operational dashboard).
- **Universal Forwarder Layer:** ⚪ **PLANNED** (Decoupled forwarder pipeline scheduled for P2/P3).
- **Adversary Attack Simulation:** ⚪ **PLANNED** (Active Kali Linux adversary tooling in P4).

---

## Conceptual Architecture

```mermaid
flowchart TD
    subgraph DataSources["Data Telemetry Layer"]
        D1["Structured SSH Logs
(data/ssh_logs.json)"]
        D2["Linux Auth Logs
(/var/log/auth.log)"]
    end

    subgraph Ingestion["Ingestion Engine"]
        M1["Direct Splunk Web Upload
(index=main, sourcetype=_json)"]
        UF["Splunk Universal Forwarder
(Planned for P2/P3)"]
    end

    subgraph SIEM["Splunk Enterprise Engine (Kali Linux)"]
        IDX["Splunk Indexer & Search Head
(Port 8000 Web UI)"]
        SPL["SPL Analytics Engine
(Queries 01-06)"]
    end

    subgraph Visualization["SOC Operations"]
        DASH["5-Panel SOC Security Dashboard"]
        REP["Log Analysis Report & Forensic Findings"]
    end

    D1 --> M1
    D2 -. Future Ingestion .-> UF
    M1 --> IDX
    UF -. Port 9997 .-> IDX
    IDX --> SPL
    SPL --> DASH
    SPL --> REP
```

![Lab Architecture](../screenshots/lab-architecture.jpg)

---

## Component Specifications

| Component | Role | Version / Config | Status |
|---|---|---|:---:|
| **Splunk Enterprise** | Central SIEM engine & web console | `9.2.4` (Linux x86_64) | **IMPLEMENTED** |
| **Host Workstation** | Operating system host | Kali Linux (Kernel 6.x) | **IMPLEMENTED** |
| **Ingestion Target** | Storage index | `index=main` | **IMPLEMENTED** |
| **Sourcetype Parsing** | Field extraction schema | `_json` / `linux_secure` | **IMPLEMENTED** |
| **Universal Forwarder** | Endpoint log shipping agent | Splunk UF 9.x | **PLANNED** |
| **VirtualBox Network** | Isolated virtualization network | Host-Only / NAT Network | **IMPLEMENTED** |
