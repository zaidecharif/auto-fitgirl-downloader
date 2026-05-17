# 🚀 Auto Downloader Script (Selenium)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)
![AI Generated](https://img.shields.io/badge/Code-AI_Generated-purple.svg)

> **🤖 Note:** This script was generated with the help of AI! It was built to automate the tedious process of clicking through multiple download links, handling pop-ups, and managing browser tabs.

This Python script reads a list of URLs from a text file or CSV, opens them in a persistent Google Chrome session, and automatically clicks the necessary buttons to download files. It smartly handles new tabs and waits for your downloads to finish before moving to the next link.

---

## 📋 Prerequisites

Before you can run this script, you need to have a few things set up on your computer:

1. **Python:** You must have Python installed. If you don't have it, download it from [python.org](https://www.python.org/downloads/). *(Make sure to check the box that says "Add Python to PATH" during installation).*
2. **Required Libraries:** You need to install the Selenium and Webdriver Manager packages.

Open your **Command Prompt (cmd)** or **Terminal** and run this command:
`pip install selenium webdriver-manager`

---

## ⚙️ Configuration

Before running the script, open the Python file (`auto_downloader_fitgirl.py`) in a text editor and update these two variables at the top of the script to match your computer:

`LINKS_FILE    = r"C:\Users\YourUsername\Documents\urls.txt"`
`DOWNLOAD_DIR  = r"C:\Users\YourUsername\Downloads\auto_downloads"`

---

## 💻 How to Run the Script

1. Open your **Command Prompt (cmd)** or **Terminal**.
2. Navigate to the folder where you saved the Python script using the `cd` (change directory) command. For example:
   `cd C:\Users\ZAID\Documents`
3. Once you are in the correct folder, run the script with this command:
   `python auto_downloader_fitgirl.py`
   *(Note: Make sure your file is named `auto_downloader_fitgirl.py` without spaces. If it has a space, rename it so it uses an underscore!)*

---

## ✨ Features

- **Persistent Browser:** Leaves a Google tab open so Chrome doesn't automatically quit when the script finishes.
- **Two-Click Flow:** Handles sites that require you to click a download button, switch to a new tab, and click a second download button.
- **Smart Waiting:** Detects `.crdownload` files to know exactly when a download finishes before moving to the next link.
- **Error Handling:** Automatically cleans up broken tabs if a link fails, ensuring the script keeps running.

---

## 🤝 Contributing
Feel free to fork this repository, make changes, and submit pull requests if you want to add new features or improve the script!
