# ⬡ PHANTOM - Red Team Operations Suite


**A professional Red Team Operations GUI tool built for the Cyber Warfare.**  
Covers the full offensive lifecycle - from payload generation to post-exploitation and evasion.

</div>

---


---

## 🎯 What is PHANTOM?

PHANTOM is a **Python/PyQt5 GUI tool** that centralizes all Red Team operations into one sleek interface.  
Built as a  project for **Cyber Warfare**.

It covers the full offensive attack chain:

```
[Payload Generation] → [Shell Delivery] → [AV Evasion] → [Post-Exploitation] → [Persistence]
```

---

## 🗂️ Modules Covered

| # |  Module | PHANTOM Tab |
|---|---|---|
| 3 | Advanced Payloads I | ⚡ Payload Crafter |
| 4 | Advanced Payloads II | 🔐 Encoder / Obfuscator |
| 5 | Hands-On Exploitation | 🔗 Shell Generator |
| 7 | Post-Exploitation (Windows) | 🪟 Post-Ex · WIN |
| 8 | Post-Exploitation (Linux) | 🐧 Post-Ex · Linux |
| 10 | Evasion Techniques | 👻 Evasion Techniques |

---

## ⚙️ Features

### ⚡ Tab 1 — Payload Crafter (msfvenom Builder)
- Supports **6 platforms**: Windows x64/x86, Linux x64/x86, Android, macOS, Python
- **20+ payload types**: Meterpreter TCP/HTTPS, Shell, VNC, Bind, PowerShell
- Full **format selection**: exe, dll, elf, php, ps1, hta, raw, base64, and more
- **Encoder support**: shikata_ga_nai, xor_dynamic, powershell_base64, and more
- Auto-generates the complete **msfvenom command** + **Metasploit multi/handler listener**
- One-click copy buttons

### 🔗 Tab 2 — Reverse Shell Generator
- **13 shell types**: Bash, Python3, Python2, PHP, Perl, Ruby, Netcat, PowerShell, PowerShell B64, Socat, Golang, Java, Netcat OpenBSD
- Dynamic LHOST/LPORT injection — updates all shells in real time
- **ALL SHELLS** button — generates every shell type at once
- Auto-generates `nc -lvnp` catch listener

### 🔐 Tab 3 — Encoder / Obfuscator
- **12 operations**: Base64 Encode/Decode, URL Encode/Decode, Hex Encode/Decode, XOR Encode, PowerShell B64, ROT-13, Reverse String, To Hex Shellcode, Strip Whitespace
- Configurable **XOR key** (hex)
- **SWAP I/O** — flips input/output for chained operations

### 🪟 Tab 4 — Post-Exploitation · Windows
**7 categories, 40+ commands:**
- System Recon — systeminfo, hotfixes, installed software
- Users & Privileges — whoami /all, domain users, UAC config
- Network — ipconfig, ARP, netstat, firewall rules
- Processes & Services — tasklist, scheduled tasks, startup programs
- Persistence — Run keys, schtasks, boot services
- Credential Access — Mimikatz (logonpasswords, NTLM hashes, DCSync), LSASS dump, WiFi passwords
- Lateral Movement — PSExec, WMI, Pass-the-Hash, RDP enable

### 🐧 Tab 5 — Post-Exploitation · Linux
**6 categories, 35+ commands:**
- System Recon — uname, CPU, memory, disk, mounts
- Users & Privileges — id, sudo -l, SUID/SGID binaries, capabilities
- Network — ip a, ss -tulpn, iptables, hosts file
- Processes & Cron — ps auxf, crontab, systemd services
- Credential Access — /etc/shadow, SSH keys, bash history, git credentials
- Persistence — bashrc backdoor, cron backdoor, SSH authorized keys, systemd service

### 👻 Tab 6 — Evasion Techniques
**4 categories, 16+ techniques with code:**
- **AMSI Bypass**: AmsiUtils Patch, Context Null Patch, DLL Unhooking, ETW Patch
- **AV Evasion**: Base64 encoding, XOR obfuscation, Sleep-based sandbox evasion, Process Hollowing, Reflective DLL Injection
- **Living Off The Land**: certutil, mshta, regsvr32 (Squiblydoo), wmic XSL, bitsadmin
- **Network Evasion**: DNS Tunneling (dnscat2), HTTPS Meterpreter, Malleable C2

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/itaybechor389-sudo/phantom.git
cd phantom

# Install dependencies
pip install PyQt5 --break-system-packages

# Run
python3 phantom.py
```

**Requirements:**
- Python 3.8+
- PyQt5
- Kali Linux (recommended) or any Linux/Windows with Python

---


---

## 📁 Project Structure

```
phantom/
│
├── phantom.py          # Main application — all tabs, GUI, logic
├── README.md           # This file
└── screenshots/        # GUI screenshots for README
    ├── payload.png
    ├── shell.png
    ├── encoder.png
    ├── postex_win.png
    ├── postex_linux.png
    └── evasion.png
```

---

## 🔬 Technical Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| GUI Framework | PyQt5 (QMainWindow, QTabWidget, QSplitter) |
| Styling | Custom QSS (Qt Style Sheets) — dark cyber theme |
| Data | Pure Python dicts — no external DB |
| Clipboard | QApplication.clipboard() |
| Timers | QTimer for button feedback |

---

## ⚠️ Disclaimer

> **For authorized penetration testing and educational purposes only.**  
> This tool was developed as a course project for Cyber Warfare ZX310 at John Bryce / ThinkCyber Cyberium Academy.  
> All testing was performed in a controlled lab environment on machines I own and have explicit permission to test.  
> The author takes no responsibility for misuse of this tool.

---

## 👨‍💻 Author

**Itay Bechor**  

---

<div align="center">


</div>
