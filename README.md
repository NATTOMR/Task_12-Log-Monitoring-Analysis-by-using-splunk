# Task_12-Log-Monitoring-Analysis
🔍 Splunk Log Analysis & Incident Detection Project
📌 Project Overview

This project focuses on log analysis and incident detection using Splunk only. The goal is to simulate a real-world SOC (Security Operations Center) task where logs are ingested, analyzed, correlated, and turned into actionable security insights.

By completing this project, you will demonstrate hands-on experience with Splunk fundamentals, SIEM concepts, and security monitoring — ideal for a cybersecurity portfolio.

🎯 Objectives

Understand different log types

Analyze authentication-related logs

Identify failed login attempts

Detect anomalies and suspicious behavior

Correlate security events

Learn SIEM fundamentals using Splunk

Create alerts

Document findings in a professional report

🛠 Tools Used

Splunk Enterprise / Splunk Free (Primary & only tool)

⚠️ No external tools (Linux CLI, Event Viewer, etc.) are used. All analysis is done inside Splunk.

📂 Log Sources

You may use any one of the following:

Linux authentication logs (auth.log)

Windows Security Event Logs

Sample logs from Splunk (recommended for beginners)

Recommended Sample Data

tutorialdata.zip (Splunk official sample data)

Windows Security Logs (Event IDs 4624, 4625)

⚙️ Project Setup
1️⃣ Install Splunk

Download Splunk Free or Splunk Enterprise Trial

Start Splunk Web Interface: http://localhost:8000

2️⃣ Upload Logs

Go to Settings → Add Data → Upload

Select log files

Assign a source type (e.g., linux_secure, WinEventLog:Security)

Index: main

🔎 Analysis Tasks (Step-by-Step)
1️⃣ Understand Log Types

Identify fields such as:

user

src_ip

action

status

EventCode

Example SPL:

index=main | stats count by sourcetype
2️⃣ Analyze Authentication Logs

Focus on login-related events.

index=main (login OR authentication)
3️⃣ Identify Failed Logins
index=main (failed OR failure)
| stats count by user, src_ip
| sort -count
4️⃣ Detect Anomalies

Detect brute-force or suspicious behavior.

index=main failed
| stats count by src_ip
| where count > 5
5️⃣ Correlate Events

Correlate failed logins followed by successful logins.

index=main
| transaction user maxspan=10m
| search failed success
6️⃣ SIEM Basics in Splunk

Use Indexes for log storage

Use Search Processing Language (SPL)

Apply Time-based analysis

index=main | timechart count
7️⃣ Create Alerts

Example: Alert for multiple failed logins.

index=main failed
| stats count by src_ip
| where count > 10

Save as Alert

Trigger condition: If result > 0

Action: Log event / Email (optional)

8️⃣ Document Findings

Capture:

Screenshots of searches

SPL queries used

Security insights

📄 Deliverables
✅ Log Analysis Report

Include:

Objective

Log sources

Key SPL queries

Detected incidents

Screenshots

Mitigation recommendations

🏁 Final Outcome

By completing this project, you gain:

Hands-on Splunk experience

Incident detection skills

SIEM fundamentals

Portfolio-ready cybersecurity project
