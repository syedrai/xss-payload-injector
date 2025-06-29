# xss-payload-injector
Simple Python XSS payload injector for DVWA and basic web pentesting.
# XSS Payload Injector

## 🚀 Description

This is a simple **Python automation script** to demonstrate how to inject **Reflected XSS payloads** into a vulnerable web application such as **DVWA** (Damn Vulnerable Web App).  
It sends test payloads, captures responses, and saves them as HTML files for analysis.

---

## ⚙️ How it works

1. **Target:** The script targets the `xss_r` (Reflected XSS) page in DVWA by default.  
2. **Cookies:** You must provide a valid `PHPSESSID` and security level.  
3. **Payloads:** A list of common XSS payloads is injected into the `name` parameter.  
4. **Responses:** The script saves the HTML response for each payload so you can verify whether the payload executes in the browser.

---

## ✅ Requirements

- Python 3  
- `requests` library

Install dependencies:

```bash
pip install requests

Usage
Edit config in payload_injector.py:

TARGET_URL — your DVWA or test lab URL.

COOKIES — set your PHPSESSID and security level.

HEADERS — adjust if needed.

Run the script:python payload_injector.py


Open the output .html files:

Check the files in your browser to see if the payload executed.
Disclaimer
For Educational Purposes Only
This script is for learning web security in a legal and controlled environment (like DVWA).
Do not use against any system you do not own or do not have explicit permission to test.
The author takes no responsibility for any misuse.

Author
Syed Raihaan
Feel free to fork, adapt, and experiment!
How to use this file**

1. Save all of the above text in a file named `README.md` in your project folder.  
2. Open a terminal and push it to GitHub:
   bash
   git add README.md
   git commit -m "Add README with usage, steps and disclaimer"
   git push
