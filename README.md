<div align="center">

```
 ██████╗ ██╗████████╗    ███████╗██╗████████╗
██╔════╝ ██║╚══██╔══╝    ██╔════╝██║╚══██╔══╝
██║  ███╗██║   ██║       █████╗  ██║   ██║   
██║   ██║██║   ██║       ██╔══╝  ██║   ██║   
╚██████╔╝██║   ██║       ██║     ██║   ██║   
 ╚═════╝ ╚═╝   ╚═╝       ╚═╝     ╚═╝   ╚═╝  
```

### ⬇ Bulk Downloader — Dark Edition

![Python](https://img.shields.io/badge/Python-3.8%2B-red?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-e8401c?style=for-the-badge&logo=selenium&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-black?style=for-the-badge)
![AI Built](https://img.shields.io/badge/Built%20with-Claude%20AI-orange?style=for-the-badge&logo=anthropic&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

*Automate bulk downloads from multi-step pages with a sleek dark GUI*

</div>

---

## 🤖 About This Project

> **This entire project was built with [Claude](https://claude.ai) (Anthropic's AI).** The download engine, GUI design, tab management logic, file detection system, and this README — all generated through an iterative AI-assisted development session. No line of code was written by hand.

This tool automates the tedious process of downloading large batches of files from sites that require multiple button clicks per file (landing page → intermediate page → actual download). Instead of repeating those clicks hundreds of times manually, you give it a list of URLs and walk away.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🖥️ **Dark GUI** | Sleek `customtkinter` interface — no terminal required |
| 📋 **Batch Processing** | Feed it a `.txt` or `.csv` file with hundreds of URLs |
| 🔍 **Smart Detection** | Detects new files by name diff, not just file count |
| ⚙️ **Adjustable Timeouts** | Live sliders for every timing parameter |
| 📊 **Live Progress** | Real-time log, progress bar, and stats panel |
| 🌐 **Chrome Stays Open** | Browser remains alive after the script finishes |
| 🛡️ **Error Recovery** | Gracefully handles failed URLs and continues |

---

## 🖼️ How It Looks

```
┌─────────────────────────────────────────────────────────────────┐
│  [Avatar]  ⬇                    Configure & Launch    ● IDLE    │
│  GIT FIT                                                         │
│  BULK DOWNLOADER   ┌──────────────────────────────────────────┐ │
│                    │ LINKS FILE    [path/to/urls.txt] [Browse] │ │
│  TOTAL LINKS       │──────────────────────────────────────────│ │
│  0                 │ DOWNLOAD DIR  [C:\Downloads\]    [Browse] │ │
│                    └──────────────────────────────────────────┘ │
│  COMPLETED                                                       │
│  0                 PROGRESS                               0%     │
│                    ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  FAILED                                                          │
│  0                 ACTIVITY LOG                         [Clear] │
│                    [12:34:01] ▶ Found 42 links. Starting...     │
│  BUTTON TIMEOUT    [12:34:02] [1/42] https://example.com/...   │
│  ──────●────  20   [12:34:05]   ✔ First button clicked         │
│                    [12:34:07]   ✔ Switched to new tab           │
│  NEW TAB WAIT      [12:34:09]   ✔ Second button clicked        │
│  ──●────────  10   [12:34:12]   ✅ Saved: game.part01.rar      │
│                                                                  │
│  DOWNLOAD TIMEOUT            [⏹ STOP]  [▶ START DOWNLOAD]      │
│  ────────────●  120                                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ How It Works

```
Your URL list
     │
     ▼
┌─────────────┐
│  Page 1     │  ← Script navigates here, finds & clicks
│  [DOWNLOAD] │    the first download button
└──────┬──────┘
       │  opens new tab
       ▼
┌─────────────┐
│  Page 2     │  ← Switches to new tab, finds & clicks
│  [DOWNLOAD] │    the second download button
└──────┬──────┘
       │  triggers download
       ▼
┌─────────────┐
│  Chrome     │  ← Waits for .crdownload to disappear,
│  Downloads  │    then diffs folder to find new filename
└──────┬──────┘
       │
       ▼
  ✅ Saved: filename.rar
       │
       └──► Next URL →  repeat
```

The script uses **Selenium** to drive a real Chrome browser — it clicks exactly what a human would click, which means it bypasses JavaScript-rendered buttons, timers, and redirects that simple HTTP scrapers can't handle.

---

## 📦 Requirements

- **Python 3.8+**
- **Google Chrome** (must be installed)
- The following Python packages:

```bash
pip install selenium webdriver-manager customtkinter Pillow
```

> `webdriver-manager` automatically downloads the correct ChromeDriver for your Chrome version — no manual setup needed.

---

## 🚀 Installation & Usage

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/git-fit-downloader.git
cd git-fit-downloader
```

**2. Install dependencies**
```bash
pip install selenium webdriver-manager customtkinter Pillow
```

**3. Run the app**
```bash
python downloader_app.py
```

**4. In the GUI:**
- Click **Browse** next to `LINKS FILE` → select your `.txt` or `.csv` file
- Click **Browse** next to `DOWNLOAD DIR` → choose where files should be saved
- Adjust the sliders if needed (defaults work for most sites)
- Hit **▶ START DOWNLOAD** and watch the log

---

## 📝 Links File Format

**Plain text** (one URL per line):
```
https://example.com/download/file1
https://example.com/download/file2
https://example.com/download/file3
```

**CSV** (must have a `url` column):
```csv
url,name
https://example.com/download/file1,Game Part 1
https://example.com/download/file2,Game Part 2
```

Lines starting with `#` are ignored (useful for comments).

---

## 🎛️ Settings Reference

| Slider | Default | Description |
|---|---|---|
| **Button Timeout** | 20s | How long to wait for a download button to appear |
| **New Tab Wait** | 10s | How long to wait for a new tab to open after click |
| **Download Timeout** | 120s | Max time to wait for a file to finish downloading |
| **Delay / Link** | 3s | Pause between each URL (be respectful to servers) |

---

## 🏗️ Project Structure

```
git-fit-downloader/
│
├── downloader_app.py     # Main app — GUI + download engine
└── README.md             # This file
```

The entire project lives in a single Python file by design — easy to share, easy to run.

---

## ⚠️ Disclaimer

This tool is for **educational and personal use only**. It automates clicks that you would otherwise perform manually in a browser.

- Respect each website's Terms of Service
- Don't hammer servers — use the delay slider
- Only download content you have the right to download

---

## 🤝 Contributing

PRs welcome. If a site's button structure changes and the selectors break, open an issue with the URL pattern and I'll update the `find_download_button()` selectors.

---

## 🧠 Built With AI

This project was created through a conversation with **Claude Sonnet** (Anthropic). The development process involved:

- Iterative debugging of Selenium tab management
- Research into how download sites actually serve files (`window.open()` vs Chrome download manager)
- UI design in `customtkinter` with embedded assets
- Root-cause analysis of timing race conditions

> *"The original script works, so the GUI now runs exactly the same code, line by line, inside a thread."* — Claude, during one of many debugging sessions

---

<div align="center">

Made with ❤️ and 🤖 by **Zaid** + **Claude AI**

⭐ Star this repo if it saved you hours of clicking

</div>
