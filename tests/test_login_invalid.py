from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Tarayıcıyı başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Login sayfasına git
driver.get("https://the-internet.herokuapp.com/login")

# Yanlış kullanıcı adı ve şifre gir
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("wronguser")
password_input.send_keys("wrongpassword")

# Giriş düğmesine tıkla
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Kısa bir süre bekle
time.sleep(2)

# Hata mesajını bul
error_message = driver.find_element(By.ID, "flash")

# Hata mesajı doğru mu?
if "Your username is invalid!" in error_message.text:
    print("Test BAŞARILI: Hata mesajı göründü.")
else:
    print("Test BAŞARISIZ: Hata mesajı görünmedi veya beklenen metin yok.")

# Test sonucu ekran görüntüsü al
driver.save_screenshot("test-sonucu.png")

# Tarayıcıyı kapat
driver.quit()
