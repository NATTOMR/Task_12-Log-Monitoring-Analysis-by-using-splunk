# 🔍 Splunk Log Analysis & Incident Detection Project

---

## 📌 Project Overview

This project focuses on **log analysis and incident detection using Splunk only**.  
It simulates a real-world **SOC (Security Operations Center)** workflow where logs are ingested, analyzed, correlated, visualized, and transformed into actionable security insights.

This project demonstrates hands-on experience with:
- Splunk fundamentals
- SIEM concepts
- Security monitoring & incident detection  
Ideal for a **cybersecurity portfolio / academic submission**.

---

## 🎯 Objectives

- Install Splunk in Kali Linux
- Upload and analyze logs using Splunk
- Create security dashboards
- Learn SIEM fundamentals
- Understand different log types
- Analyze authentication-related logs
- Identify failed login attempts
- Detect anomalies and suspicious behavior
- Correlate security events
- Create alerts
- Document findings professionally

---

## 🛠 Tools Used

- **Splunk Enterprise / Splunk Free** (Primary & only tool)

⚠️ No external tools (Linux CLI, Event Viewer, etc.) are used.  
All analysis is done **inside Splunk only**.

---

## 📂 Log Sources

You may use any one of the following:

- Linux authentication logs (`auth.log`)
- Windows Security Event Logs
- Splunk sample logs (recommended for beginners)

### Recommended Sample Data
- `tutorialdata.zip` (Official Splunk sample data)
- Windows Security Logs (Event IDs: 4624, 4625)

---

## ⚙️ Project Setup

### 1️⃣ Install Splunk in Kali Linux

#### Download Splunk
``bash
wget -O splunk-9.2.4-linux.deb https://download.splunk.com/products/splunk/releases/9.2.4/linux/splunk-9.2.4-c103a21bb11d-linux-2.6-amd64.deb

   
5. 2️⃣ Install Splunk
   `sudo dpkg -i splunk.deb`
   - If you get dependency errors: `sudo apt --fix-broken install -y`

6. 3️⃣ Start Splunk
 `sudo /opt/splunk/bin/splunk start`
- ✔ Accept the license
- ✔ Set admin username & password
  
![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/splunk%20start.png)

7. 4️⃣ Enable Splunk at Boot (recommended)
  `sudo /opt/splunk/bin/splunk enable boot-start`

8. 5️⃣ Access Splunk Web
    - Open your browser:  `http://localhost:8000`
      
9. 6️⃣ Check Splunk Status (optional)
    `sudo /opt/splunk/bin/splunk status`


![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/splunk%20dashboard.png)

  # 📥 Upload Logs to Splunk

1. Go to Settings → Add Data
2.  Select Upload
3.  Choose log files
4.   Assign appropriate Source Type

- linux_auth

- linux_secure

- WinEventLog:Security

![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/new%20dashboard-1.jpeg)
![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/new%20dashboard-2.jpeg)
![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/new%20dashboard-3.jpeg)
![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/new%20dashboard-4.jpeg)
![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/new%20dashboard-5.jpeg)

# How to create splunk dashboard

# Kali Security Dashboard (Splunk)

This guide explains how to create and manage a basic **Splunk dashboard** in a Kali Linux VM

<<<<<<< HEAD
<<<<<<< HEAD
Go to Settings → Add Data → Upload
=======
---

## Option A: Create a New Dashboard

- **Dashboard Title:** Kali Security Dashboard  
- **Description:** Monitoring logs in Kali Linux  
- **Dashboard ID:** Auto-filled by Splunk  
- **Permissions:** Private (for now)

Click **Save**

## 🎉 Your first dashboard is created!

---

## Step : View Your Dashboard

1. Click **Dashboards**
2. Open **Kali Security Dashboard**
3. You will see your first panel

---

## Add Panels to Dashboard
Panel 1: Login Attempts (Auth Logs)
`index=* sourcetype=linux_secure OR sourcetype=linux_auth
| stats count by user`


- Visualization: Bar Chart / Table

- Save → Save As Dashboard Panel

- Select Existing Dashboard

- Choose Kali Security Dashboard

## Panel 2: Top Source IPs
`index=* | stats count by src_ip | sort -count`


- Visualization: Table / Bar Chart

- Save to same dashboard


## 🔎 Analysis Tasks (Step-by-Step)

### 1️⃣ Understand Log Types

Before analyzing data in Splunk, it is important to understand the types of logs available in Kali Linux and what security information they provide.

#### Common Log Types

- **Authentication Logs**
  - `linux_auth`, `linux_secure`
  - Tracks login attempts, SSH access, sudo usage
  - Useful for detecting brute-force attacks and unauthorized access

- **System Logs**
  - `syslog`
  - Records system events, errors, service activity
  - Useful for troubleshooting and system monitoring

- **Audit Logs**
  - `linux_audit`
  - Tracks executed commands, file access, privilege escalation
  - Useful for insider threat detection and forensic analysis

- **Network / Firewall Logs**
  - May include logs from iptables, UFW, Suricata, or Zeek
  - Useful for detecting suspicious IPs and malicious traffic

- **Splunk Internal Logs**
  - `_internal`
  - Monitors Splunk’s own health and performance
  - Useful for SIEM reliability and troubleshooting

---

### 2️⃣ Identify High-Value Security Events

Focus on events that indicate potential threats:

- Failed login attempts
- Repeated access from the same IP
- Unauthorized command execution
- Sudden spikes in log volume
- Errors or warnings in system logs

---

### 3️⃣ Run Basic Analysis Queries

#### Failed SSH Login Analysis
``spl
`index=* "Failed password"
| stats count by src_ip`


## User Login Activity
`index=* sourcetype=linux_auth
| stats count by user`

## Command Execution Monitoring
`index=* sourcetype=linux_audit
| stats count by comm`

6. 6️⃣ SIEM Basics in Splunk

- Use Indexes for log storage

- Use Search Processing Language (SPL)

- Apply Time-based analysis

`index=main | timechart count`

7. 7️⃣ Create Alerts

Example: Alert for multiple failed logins.

`index=main failed
| stats count by src_ip
| where count > 10`

- Save as Alert

- Trigger condition: If result > 0

- Action: Log event / Email (optional)

# 📊 Final Dashboard Output
![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/splung%20dashboard.jpeg)
# 📄 Deliverables

# ✅ Log Analysis Report

- Include:

- Objective
- 
- Log sources

- Key SPL queries

- Detected incidents

- Screenshots

- Mitigation recommendations

# 🏁 Final Outcome

By completing this project, you gain:

- Hands-on Splunk experience

- Incident detection skills

- SIEM fundamentals

---

## 👤 Author

**Natto Muni Chakma**  
B.Tech (Computer Science & Engineering)  
Cybersecurity & SIEM Enthusiast  

- 💻 Interested in Security Operations Center (SOC)
- 🔍 Log Analysis & Incident Detection
- 🛡️ SIEM, Splunk, Network & System Security

📫 GitHub: https://github.com/NATTOMR  

---

## 📚 References

1. **Splunk Official Documentation**  
   https://docs.splunk.com

2. **Splunk Search Processing Language (SPL) Reference**  
   https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual

3. **Splunk Dashboard Studio Guide**  
   https://docs.splunk.com/Documentation/Splunk/latest/DashStudio/AboutDashboardStudio

4. **Linux Authentication Logs (auth.log)**  
   https://man7.org/linux/man-pages/man5/syslog.conf.5.html

5. **SOC & SIEM Concepts**  
   https://www.splunk.com/en_us/solutions/siem.html

6. **MITRE ATT&CK Framework (Attack Techniques Reference)**  
   https://attack.mitre.org

---

