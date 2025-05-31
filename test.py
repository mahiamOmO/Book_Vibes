from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/")

    wait = WebDriverWait(driver, 10)

    try:
        # Login
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, "user"))).send_keys("hasan")
        wait.until(EC.visibility_of_element_located((By.NAME, "pass"))).send_keys("hasan")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        print("✅ Logged in successfully.")

        # Add books to cart
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Books"))).click()
        time.sleep(2)
        add_buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Add to cart')]")
        if len(add_buttons) >= 2:
            add_buttons[0].click()
            time.sleep(1)
            add_buttons[1].click()
            time.sleep(1)
            print("✅ Added 2 books to cart.")
        else:
            print("❌ Not enough books found.")
            return

        # Go to eBooks section and read the first book
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Ebook"))).click()
        time.sleep(2)
        ebook_links = driver.find_elements(By.LINK_TEXT, "View Details")

        if ebook_links:
            ebook_links[0].click()
            print("✅ Opened first Ebook to read.")
        else:
            print("❌ No eBooks available to read.")
            return

        time.sleep(3)  # Allow time to view the book

        # Attempt to log out with fallback support
        print("🔎 Available links before logout:")
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            print(" -", link.text.strip())

        try:
            # Try exact match first
            logout_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign Out")))
            logout_link.click()
            print("✅ Logged out successfully.")
        except:
            try:
                # Fallback: partial match (e.g., "Logout", "Sign Out")
                logout_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Log')]")))
                logout_link.click()
                print("✅ Logged out using fallback XPath.")
            except Exception as logout_error:
                print("❌ Logout link not found or clickable:", logout_error)

        time.sleep(2)

    except Exception as e:
        print(f"❌🙆‍♀️ Test failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
