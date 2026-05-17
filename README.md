# ⚡ GIT FIT — Bulk Downloader ⚡

![UI Preview](https://img.shields.io/badge/UI-CustomTkinter-orange?style=for-the-badge) ![Automation](https://img.shields.io/badge/Engine-Selenium-blue?style=for-the-badge) ![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge)

**GIT FIT** is a high-performance, automated bulk downloader wrapped in a sleek Dark Mode UI. Designed specifically to navigate multi-step redirect sites (like repack hosters), it automates the tedious process of opening links, finding the download buttons, waiting for redirects, and managing the file streams.

You can run it instantly as a standalone `.exe` or dive into the `.py` source code to see how it ticks.

---

## 🚀 Quick Start (For Users)

Don't want to mess with Python, pip, or dependencies? I've got you covered.

1. Go to the **Releases** tab and download `GIT_FIT.exe`.
2. Double-click the executable (no installation required).
3. **Select your Links File:** Feed it a `.txt` or `.csv` file containing one URL per line.
4. **Select your Output Folder:** Choose where you want the files saved.
5. Hit **▶ START DOWNLOAD**.

The app will launch an automated Chrome instance, methodically work through your list, and safely handle the downloads. You can monitor the live progress and activity logs right in the app. 

*Note: The first time you run the `.exe`, it may take a few seconds to unpack the runtime environment.*

---

## 🛠️ Under the Hood (For Developers)

If you're a Python dev, this script solves several notorious browser automation headaches. Here is how the engine works:

### 1. The Automation Engine (Selenium)
The core relies on `selenium` and `webdriver-manager`. Instead of headless mode (which often triggers bot-protection blocks), GIT FIT uses a **Persistent Detached Session**:
* It opens a primary "dummy" tab (Google) to keep the browser instance alive.
* It spawns a dedicated **Worker Tab** to navigate the URLs.
* **Smart Element Hunting:** It doesn't rely on a single CSS class. It tries multiple XPATHs and selectors (like `translate()` functions for case-insensitive matching) to hunt down elusive download buttons.

### 2. Memory & Tab Management
One of the biggest issues with bulk downloading is memory leaks from opening 100+ tabs. 
* GIT FIT strictly enforces a **2-Tab Maximum**. 
* Once a file initiates the `.crdownload` or `.part` stream, the script waits for the stream to finish, then instantly destroys the temporary download tab, routing control back to the Worker Tab. 

### 3. Windows Path Normalization (The Tkinter Bug)
There is a notorious bug where Tkinter UI dialogs return paths with forward slashes (`C:/Downloads`), which causes Chrome's Windows binary to instantly fail downloads. The script utilizes `os.path.normpath()` to forcefully convert all paths to native Windows backslashes before passing them to the webdriver preferences.

### 4. Self-Healing Dependencies
If you run the `.py` file raw, the script includes a `try/except` bootstrap block. If it detects you are missing `customtkinter` or `Pillow`, it silently invokes `subprocess` to `pip install` them on the fly before launching the UI.

---

## 🤖 AI Co-Authored

This project is a testament to human-AI collaboration. The core architecture, GUI design, and complex debugging (specifically solving Chrome's Safe Browsing detached-session flags and the Tkinter slash-path bug) were developed in partnership with AI. 

By leveraging AI, we were able to rapidly iterate on the Selenium window-handling logic, optimize the UI threading, and squash obscure OS-level bugs that normally take hours to track down.

---

## ⚙️ How to run from Source

If you want to tweak the code, clone the repo and run:

```bash
# Clone the repository
git clone [https://github.com/yourusername/git-fit-downloader.git](https://github.com/yourusername/git-fit-downloader.git)
cd git-fit-downloader

# Run the script (it will auto-install customtkinter and Pillow if missing)
# You will need to manually install selenium:
pip install selenium webdriver-manager

python git_fit.py
