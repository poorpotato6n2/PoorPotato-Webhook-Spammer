# <p align="center">🥔 PoorPotato Advanced Webhook Spammer 🥔</p>

<p align="center">
  <img src="https://cdn.discordapp.com/avatars/1274035679780929538/79421658ad87b1f136e4c3e10104e92b.png?size=4096" width="150" height="150" alt="PoorPotato Logo" style="border-radius: 50%; border: 3px solid #f1c40f;">
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"></a>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Developer-6n2._.-blue?style=for-the-badge" alt="Developer">
</p>

***

## 👑 About PoorPotato
**PoorPotato** is an elite, high-performance Discord webhook destruction engine. Coded by **6n2._.**, this system is engineered for maximum throughput and devastation. Built on a robust asynchronous architecture, it floods webhooks with surgical precision using advanced threading and proxy rotation to bypass rate limits and filters.

> **"System is Hot. 6n2._. on top."**

---

## 🚀 Advanced Features
- ⚡ **Multi-Threaded Engine:** Capable of running 500+ threads simultaneously for maximum volume.
- 🛡️ **Proxy Intelligence:** Advanced proxy support (User/Pass auth) with smart rotation and HTTP/2 fallback.
- 📡 **Ping System:** Optional `@everyone` toggle to maximize notification spam.
- 📊 **Live Statistics:** Real-time monitoring of Sent, Failed, Rate Limits, and Errors directly in the window title.
- 🔄 **Stability Mode:** Auto-recovers from connection drops and handles socket terminations gracefully.
- 🎨 **Colorama Branding:** Fully stylized terminal interface with custom ASCII PoorPotato art.

---

## 🛠️ Step-by-Step Installation

### Step 1: Install Python
You must have Python 3.8 or higher.
- **[Download Python Here](https://www.python.org/downloads/)**
- **IMPORTANT:** Check the box **"Add Python to PATH"** during the installation process.

### Step 2: Download the Files
Extract the source code and ensure the `pcore` folder is in the same directory as `main.py`.

### Step 3: Install Requirements
Open your Command Prompt or Terminal in the project folder and run:
```bash
pip install -r requirements.txt
```

### Step 4: Setup Files
- **`webhooks.txt`**: Add target webhook URLs (one per line).
- **`messages.txt`**: Add the messages to spam (one per line).
- **`proxies.txt`**: Add your proxies (Format: `ip:port` or `ip:port:user:pass`).

---

## ⚙️ Configuration Guide (`config.json`)

| Key | Description |
| :--- | :--- |
| `threads` | Number of concurrent spam threads (Recommended: 200-500). |
| `connect_timeout` | Max time (seconds) to wait for a proxy connection. |
| `ping_everyone` | If `true`, adds `@everyone` to the start of every message. |
| `use_proxies` | Set to `true` to enable `proxies.txt`. |
| `http2_enabled` | Set to `true` for speed, or `false` for maximum stability. |
| `keep_alive` | Reuses connections for higher speed (Recommended: `true`). |
| `retry_interval` | Time to wait before retrying after an error. |
| `show_errors` | Set to `true` to see detailed error logs in the console. |

---

## 🛠️ Troubleshooting

1. **`ModuleNotFoundError: No module named 'pcore'`**
   - **Fix:** Ensure the `pcore` folder exists and contains an `__init__.py` file.
2. **`429 Rate Limited`**
   - **Fix:** You are sending too fast. Increase `retry_interval` or add more high-quality proxies.
3. **`Client Init Failed`**
   - **Fix:** Your proxies might be dead or the format is wrong. Ensure format is `ip:port:user:pass`.
4. **`StreamClosedError` or HTTP/2 Errors**
   - **Fix:** Set `"http2_enabled": false` in `config.json`. Some proxies do not support HTTP/2.
5. **Script closes instantly**
   - **Fix:** Run via CMD/Terminal (`python main.py`) to see the specific error message.
6. **`400 Bad Request`**
   - **Fix:** Your message content might be empty or too long. Check `messages.txt`.
7. **JSONDecodeError**
   - **Fix:** You missed a comma or quote in `config.json`. Validate it at [JSONLint](https://jsonlint.com/).
8. **Proxies not loading / Zero proxies**
   - **Fix:** Ensure `use_proxies` is `true` and `proxies.txt` is not empty.
9. **`WinError 10060` / Connection Timeout**
   - **Fix:** Your internet or proxies are too slow. Increase `connect_timeout` to `20.0`.
10. **`UnicodeDecodeError`**
    - **Fix:** Ensure your text files (`messages.txt`) are saved with UTF-8 encoding.

---

## 🎮 How to Run
Once your targets are added and your config is set, ignite the engine:
```bash
python main.py
```

---

## 📂 File Structure
```yaml
PoorPotato/
├── main.py            # Modular Bootloader (By 6n2._.)
├── config.json        # System Settings
├── webhooks.txt       # Target list
├── messages.txt       # Spam content
├── proxies.txt        # Proxy list
├── requirements.txt   # Dependencies
└── pcore/             # The Core Engine
    ├── __init__.py    # Package Initializer
    ├── branding.py    # Elite ASCII Design
    ├── engine.py      # Spam Logic Handler
    ├── logger.py      # Event System
    ├── stats.py       # Statistics Manager
    └── utils.py       # Configuration Loader
```

---

## ⚠️ Disclaimer
This tool is for educational purposes only. Spamming webhooks is a violation of Discord's Terms of Service. **PoorPotato** is not responsible for any actions taken against your account or IP address.

***

<p align="center">
  <b>Developed by 6n2._.</b><br>
  <i>"PoorPotato: Making the Gateway look easy."</i>
</p>