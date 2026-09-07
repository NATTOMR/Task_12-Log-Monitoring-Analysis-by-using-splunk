# 🔍 Incident Investigation & Threat Analysis

This document summarizes the SOC investigation findings and forensic analysis conducted on the ingested telemetry in **Project P1**.

---

## Investigation Status

- **Log Volume Analyzed:** ✅ **IMPLEMENTED** (1,200 events).
- **Brute-Force Attack Triage:** ✅ **IMPLEMENTED** (Identified 5 top threat actor IPs).
- **Attack Progression Correlation:** ✅ **IMPLEMENTED** (Correlated failed logins preceding success).
- **Incident Report Documentation:** ✅ **IMPLEMENTED** (Published in `Log_Analysis_Report.md` / `Log_Analysis_Report.pdf`).

---

## Summary of Findings

| Metric / Category | Count | Percentage | Operational Impact |
|---|:---:|:---:|---|
| **Total Ingested Events** | 1,200 | 100.0% | Complete dataset scope |
| **Failed SSH Logins** | 305 | 25.42% | Credential guessing / incorrect passwords |
| **Multiple Failed Auth Attempts** | 303 | 25.25% | Automated high-frequency brute-force bursts |
| **Unauthenticated Probes** | 286 | 23.83% | Port 22 reconnaissance / banner grabbing |
| **Successful Logins** | 306 | 25.50% | Verified authentication sessions |
| **Total Malicious / Anomalous Ratio** | **608** | **50.67%** | Over half of all traffic represents attack activity |

---

## Threat Actor Profile & Triage

Statistical analysis of source IP addresses isolated five top offending hosts responsible for the majority of brute-force traffic:

1. **`10.0.0.25`**: 39 total connections, **31 malicious/failed** authentication attempts.
2. **`10.0.0.18`**: 32 total connections, **29 malicious/failed** authentication attempts.
3. **`10.0.0.46`**: 27 failed attempts.
4. **`10.0.0.22`**: 26 failed attempts.
5. **`10.0.0.48`**: 32 total connections, **26 failed** attempts.

### Targeted Infrastructure
Adversaries concentrated authentication attacks on internal jump servers:
- `10.0.1.6` (115 connections)
- `10.0.1.2` (115 connections)
- `10.0.1.9` (113 connections)

---

## Incident Timeline & Correlation Analysis

Using Splunk transaction correlation (`queries/05_failed_login_to_success_correlation.spl`):
```spl
index=main 
| transaction id.orig_h maxspan=15m 
| search auth_success=true AND (event_type="Failed SSH Login" OR event_type="Multiple Failed Authentication Attempts")
| table _time, id.orig_h, id.resp_h, duration, eventcount
```

Analysts identified instances where repeated failed authentication attempts were immediately followed by a successful login from the same source IP within a 15-minute window. In an enterprise SOC, this indicates:
- **Critical Severity Incident:** Credential discovery via brute force resulting in successful unauthorized access.
- **Recommended Response:** Immediate firewall block of source IP, terminating active SSH daemon sessions, and forcing an administrative password/SSH key reset for the compromised target account.
