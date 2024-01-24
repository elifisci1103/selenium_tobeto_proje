
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
import navbarConstants as n
import loginConstants as l

class Test_mainPageNavbar():
  
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(n.LOGIN_URL)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_mainPage(self):
    
    
   emailTextBox= self.driver.find_element(By.XPATH,l.EPOSTA_TEXT_BOX_XPATH)
   emailTextBox.send_keys(l.VALID_EPOSTA)
   passwordTextBox=self.driver.find_element(By.XPATH, l.VALID_PASSWORD)
   passwordTextBox.send_keys(l.VALID_PASSWORD)
   loginButton=self.driver.find_element(By.XPATH, l.LOGIN_BUTTON_XPATH)
   loginButton.click()
   mainPage=self.driver.find_element(By.LINK_TEXT, n.MAIN_PAGE_LINKTEXT)
   mainPage.click()
   assert self.driver.current_url==n.MAIN_PAGE_URL_

  





    self.driver.find_element(By.LINK_TEXT, "Profilim").click()
    element = self.driver.find_element(By.LINK_TEXT, "Profilim")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Değerlendirmeler").click()
    element = self.driver.find_element(By.LINK_TEXT, "Değerlendirmeler")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Katalog").click()
    element = self.driver.find_element(By.LINK_TEXT, "Katalog")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.LINK_TEXT, "Takvim")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Takvim").click()
    element = self.driver.find_element(By.LINK_TEXT, "Takvim")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "İstanbul Kodluyor").click()
    self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(3) > svg").click()
    self.driver.close()
  
