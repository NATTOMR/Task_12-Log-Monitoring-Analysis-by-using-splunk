
# 🔍 Splunk Log Analysis & Incident Detection Project

# 📌 Project Overview

This project focuses on log analysis and incident detection using Splunk only. The goal is to simulate a real-world SOC (Security Operations Center) task where logs are ingested, analyzed, correlated, and turned into actionable security insights.

By completing this project, you will demonstrate hands-on experience with Splunk fundamentals, SIEM concepts, and security monitoring — ideal for a cybersecurity portfolio.

# 🎯 Objectives
- How to install splunk in kali
- How to create splunk dashboard
- Learn SIEM fundamentals using Splunk
- Understand different log types
- Analyze authentication-related logs
- Identify failed login attempts
- Detect anomalies and suspicious behavior
- Correlate security events
- Create alerts
- Document findings in a professional report

# 🛠 Tools Used

- Splunk Enterprise / Splunk Free (Primary & only tool)

- ⚠️ No external tools (Linux CLI, Event Viewer, etc.) are used. All analysis is done inside Splunk.

## 📂 Log Sources

You may use any one of the following:

- Linux authentication logs (auth.log)

- Windows Security Event Logs

- Sample logs from Splunk (recommended for beginners)

- Recommended Sample Data

- tutorialdata.zip (Splunk official sample data)

- Windows Security Logs (Event IDs 4624, 4625)

## ⚙️ Project Setup

1️⃣ Install Splunk

1. Download link
   - `https://www.splunk.com/en_us/download/previous-releases.html`
   
3. 1️⃣ Download Splunk (Linux .deb)
   -  `wget -O splunk-9.2.4-c103a21bb11d-linux-2.6-amd64.deb "https://download.splunk.com/products/splunk/releases/9.2.4/linux/splunk-9.2.4-c103a21bb11d-linux-2.6-amd64.deb"`
   
5. 2️⃣ Install Splunk
   `sudo dpkg -i splunk.deb`
   - If you get dependency errors: `sudo apt --fix-broken install -y`

6. 3️⃣ Start Splunk
 `sudo /opt/splunk/bin/splunk start`
- ✔ Accept the license
- ✔ Set admin username & password
  
![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/splunk%20start.png)

8. 4️⃣ Enable Splunk at Boot (recommended)
  `sudo /opt/splunk/bin/splunk enable boot-start`

10. 5️⃣ Access Splunk Web
    - Open your browser:  `http://localhost:8000`
      
12. 6️⃣ Check Splunk Status (optional)
    `sudo /opt/splunk/bin/splunk status`


![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/splunk%20dashboard.png)

  

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

## Step : Add More Panels

Repeat the process to build a complete dashboard.

---

### Example 1: Login Attempts (Auth Logs)

**SPL Query**
``spl
`index=* sourcetype=linux_secure OR sourcetype=linux_auth
| stats count by user`

- Save → Save As Dashboard Panel

- Choose Existing Dashboard

- Select Kali Security Dashboard

## 2️⃣ Upload Logs

<HEAD
Go to Settings → Add Data → Upload

- Select log files

- Assign a source type (e.g., linux_secure, WinEventLog:Security)

![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/new%20dashboard-1.jpeg)
![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/new%20dashboard-2.jpeg)
![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/new%20dashboard-3.jpeg)
![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/new%20dashboard-4.jpeg)
![image](https://github.com/NATTOMR/Task_12-Log-Monitoring-Analysis-by-using-splunk/blob/main/images/new%20dashboard-5.jpeg)

# 🔎 Analysis Tasks (Step-by-Step)
 1️⃣ Understand Log Types

### Identify fields such as:

- user

- src_ip

- action

- status

- EventCode

1. Example SPL:

`index=main | stats count by sourcetype`
2. 2️⃣ Analyze Authentication Logs

`Focus on login-related events.`
>>>>>>> 19702be3823c286dea16f42566c9df2434ac0b14

`index=main `
(login OR authentication)

<<<<<<< HEAD
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
=======
- Go to Settings → Add Data → Upload

- Select log files

- Assign a source type (e.g., linux_secure, WinEventLog:Security)

Index: main

# 🔎 Analysis Tasks (Step-by-Step)
 1️⃣ Understand Log Types

### Identify fields such as:

- user

- src_ip

- action

- status

- EventCode

1. Example SPL:

`index=main | stats count by sourcetype`
2. 2️⃣ Analyze Authentication Logs

`Focus on login-related events.`
>>>>>>> 2d12d3007859112b25b31432091bb1a6e7faa2d5

index=main (login OR authentication)
3️⃣ Identify Failed Logins
index=main (failed OR failure)
=======
3. 3️⃣ Identify Failed Logins
   
`index=main (failed OR failure)
>>>>>>> 19702be3823c286dea16f42566c9df2434ac0b14
| stats count by user, src_ip
| sort -count`

4. 4️⃣ Detect Anomalies

Detect brute-force or suspicious behavior.

`index=main failed
| stats count by src_ip
| where count > 5`

5. 5️⃣ Correlate Events

Correlate failed logins followed by successful logins.

`index=main
| transaction user maxspan=10m
| search failed success`

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


# 📄 Deliverables
# ✅ Log Analysis Report

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
