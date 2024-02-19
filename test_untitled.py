import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
import loginConstants as l
import personalInformationsConstants as p

class Test_personalInformations():
  
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(l.LOGIN_URL)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  
  def test_untitled(self):
    self.driver.get("https://tobeto.com/giris")
    self.driver.set_window_size(1552, 832)
    epostaTextBox=self.driver.find_element(By.XPATH, l.EPOSTA_TEXT_BOX_XPATH)
    epostaTextBox.send_keys(l.VALID_EPOSTA)
    passwordTextBox= self.driver.find_element(By.XPATH,l.PASSWORD_TEXT_BOX_XPATH)
    passwordTextBox.send_keys(l.VALID_PASSWORD)
    self.driver.find_element(By.CSS_SELECTOR, ".btn-close:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(3) > svg").click()
    self.driver.find_element(By.LINK_TEXT, "Profil Bilgileri").click()
    self.driver.find_element(By.NAME, "name").click()
    self.driver.find_element(By.NAME, "name").send_keys("esra")
    self.driver.find_element(By.NAME, "surname").click()
    self.driver.find_element(By.NAME, "surname").send_keys("akra")
    self.driver.find_element(By.ID, "phoneNumber").click()
    self.driver.find_element(By.ID, "phoneNumber").send_keys("0544 124 56 78")
    self.driver.find_element(By.NAME, "birthday").click()
    self.driver.find_element(By.NAME, "birthday").click()
    self.driver.find_element(By.NAME, "birthday").send_keys("1991-01-02")
    self.driver.find_element(By.NAME, "identifier").click()
    self.driver.find_element(By.NAME, "country").click()
    self.driver.find_element(By.NAME, "city").click()
    dropdown = self.driver.find_element(By.NAME, "city")
    dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
    self.driver.find_element(By.NAME, "district").click()
    dropdown = self.driver.find_element(By.NAME, "district")
    dropdown.find_element(By.XPATH, "//option[. = 'Beylikdüzü']").click()
    self.driver.execute_script("window.scrollTo(0,399.20001220703125)")
    self.driver.find_element(By.NAME, "address").click()
    self.driver.find_element(By.NAME, "address").send_keys("hürriyet")
    self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(12) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(12) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(12) > .form-control").send_keys("bahar mevsimini çok severim.bana herşeyin güzel olacağını hatırlatır.yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyybtk")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    self.driver.close()
  
