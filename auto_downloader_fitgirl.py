"""
Auto Downloader Script (Persistent Google Tab)

Requirements:
    You need python installed on your computer
    and also install the selenium and webdriver-manager by running this command 
    pip install selenium webdriver-manager 
    in cmd or terminal

    after that you should acces the python file directory in cmd or terminal  by running this command :
    cd C:\Users\ZAID\Documents (this is just an example cause i have the python file here)
    and then run this command 
    python auto_downloader fitgirl.py



Mostly at the end of the downloading the script will say that 0 files were downloaded but dont worry they are downloaded


"""

import csv
import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



LINKS_FILE    = r"" #put the file directory between the quotes " " ,exemple "C:\Users\ZAID\Documents\all-url.txt"
DOWNLOAD_DIR  = r"" #put the directory where you want the files to be downloaded

# How long to wait for buttons to appear (seconds)
BUTTON_WAIT_TIMEOUT = 20

# How long to wait for new tab to open (seconds)
NEW_TAB_WAIT = 20

# How long to wait for download to finish (seconds)
DOWNLOAD_WAIT_TIMEOUT = 120

# Pause between each link (be respectful to the server)
DELAY_BETWEEN_LINKS = 3




def read_links(filepath: str) -> list:
    links = []
    ext = Path(filepath).suffix.lower()
    with open(filepath, "r", encoding="utf-8") as f:
        if ext == ".csv":
            reader = csv.DictReader(f)
            for row in reader:
                url = row.get("url", "").strip()
                if url:
                    links.append(url)
        else:
            for line in f:
                url = line.strip()
                if url and not url.startswith("#"):
                    links.append(url)
    return links


def is_downloading(download_dir: str) -> bool:
    return any(
        f.endswith(".crdownload") or f.endswith(".part")
        for f in os.listdir(download_dir)
    )


def wait_for_download(download_dir: str, timeout: int = 120) -> bool:
    """Wait until in-progress download files (.crdownload) disappear."""
    start = time.time()
    time.sleep(3)  # give Chrome a moment to start the download
    while time.time() - start < timeout:
        if not is_downloading(download_dir):
            return True
        time.sleep(1)
    return False


def count_files(download_dir: str) -> int:
    return len([f for f in os.listdir(download_dir) if not f.endswith(".crdownload")])


def build_driver(download_dir: str) -> webdriver.Chrome:
    os.makedirs(download_dir, exist_ok=True)

    options = Options()
    
    # ── THIS KEEPS CHROME OPEN AFTER THE SCRIPT ENDS ──
    options.add_experimental_option("detach", True)
    
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    })

    # Allow popups/new tabs — important for the redirect to work
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    return driver


def click_with_js(driver, element):
    """Click using JavaScript — more reliable for Vue.js buttons."""
    driver.execute_script("arguments[0].click();", element)


def find_download_button(driver, timeout=20):
    """Try multiple selectors to find the download button."""
    selectors = [
        "button.link-button.gay-button",
        "button.link-button",
        "button.gay-button",
        (By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'download')]"),
    ]
    for selector in selectors:
        try:
            if isinstance(selector, tuple):
                btn = WebDriverWait(driver, timeout).until(
                    EC.element_to_be_clickable(selector)
                )
            else:
                btn = WebDriverWait(driver, timeout).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
            return btn
        except Exception:
            continue
    return None


def main():
    links = read_links(LINKS_FILE)
    if not links:
        print("❌ No links found. Check your LINKS_FILE path and format.")
        return

    print(f"✅ Found {len(links)} links.")
    print(f"📁 Downloads will save to: {DOWNLOAD_DIR}\n")

    driver = build_driver(DOWNLOAD_DIR)
    
    # ── INITIALIZE GOOGLE TAB AND WORKER TAB ──
    driver.get("https://www.google.com")
    google_tab = driver.current_window_handle
    print("🌐 Opened persistent Google tab.")

    # Open a new tab specifically for downloading so Google remains untouched
    driver.switch_to.new_window('tab')
    worker_tab = driver.current_window_handle
    
    success, failed = 0, []

    for i, url in enumerate(links, start=1):
        print(f"[{i}/{len(links)}] Visiting: {url}")
        try:
            # Always ensure we are working inside the worker tab
            driver.switch_to.window(worker_tab)
            original_tabs = driver.window_handles[:]
            driver.get(url)

            # ── STEP 1: Find and click the first button ──
            btn = find_download_button(driver, BUTTON_WAIT_TIMEOUT)
            if not btn:
                raise Exception("Download button not found on first page")

            click_with_js(driver, btn)
            print(f"        ✔ First button clicked, waiting for new tab...")

            # ── STEP 2: Wait for a new tab to open ──
            try:
                WebDriverWait(driver, NEW_TAB_WAIT).until(
                    lambda d: len(d.window_handles) > len(original_tabs)
                )
                # Switch to the new tab (the one that isn't Google or the worker tab)
                new_tab = [t for t in driver.window_handles if t not in original_tabs][0]
                driver.switch_to.window(new_tab)
                print(f"        ✔ Switched to new tab: {driver.current_url}")
            except Exception:
                print(f"        ℹ No new tab opened, staying on same page...")

            # ── STEP 3: Click the download button on the new page ──
            files_before = count_files(DOWNLOAD_DIR)
            btn2 = find_download_button(driver, BUTTON_WAIT_TIMEOUT)
            if not btn2:
                raise Exception("Download button not found on second page")

            click_with_js(driver, btn2)
            print(f"        ✔ Second button clicked, waiting for download...")

            # ── STEP 4: Wait for download to complete ──
            if wait_for_download(DOWNLOAD_DIR, DOWNLOAD_WAIT_TIMEOUT):
                files_after = count_files(DOWNLOAD_DIR)
                if files_after > files_before:
                    print(f"        ✅ Download complete!")
                else:
                    print(f"        ⚠ No new file detected — may have already existed.")
                success += 1
            else:
                print(f"        ⚠ Download timed out after {DOWNLOAD_WAIT_TIMEOUT}s.")
                failed.append(url)

            # ── STEP 5: Close new tab, go back to worker tab ──
            if len(driver.window_handles) > 2: # Keep Google tab + Worker tab open
                driver.close()
                driver.switch_to.window(worker_tab)

        except Exception as e:
            print(f"        ✗ Error: {e}")
            failed.append(url)
            # Clean up extra tabs if something went wrong, making sure to leave 2 (Google + Worker)
            while len(driver.window_handles) > 2:
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
            driver.switch_to.window(worker_tab)

        if i < len(links):
            time.sleep(DELAY_BETWEEN_LINKS)

    # ── CLEANUP: Close worker tab and leave Google open ──
    driver.switch_to.window(worker_tab)
    driver.close()
    driver.switch_to.window(google_tab)
    
    # REMOVED driver.quit() so the browser stays open!

    print(f"\n{'─'*50}")
    print(f"✅ Done! {success}/{len(links)} files downloaded successfully.")
    print("🌐 Chrome is detached and the Google tab has been left open for you.")
    if failed:
        print(f"\n❌ Failed URLs ({len(failed)}):")
        for url in failed:
            print(f"   - {url}")


if __name__ == "__main__":
    main()