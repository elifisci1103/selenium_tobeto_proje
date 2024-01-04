
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
import registerConstants as r

class Test_register():

  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(r.REGISTER_URL)
    self.driver.maximize_window
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_register_eposta_control(self):
   
    epostaTextBox= self.driver.find_element(By.XPATH, r.EPOSTA_TEXT_BOX_XPATH)
    epostaTextBox.send_keys(r.FALSE_EPOSTA)
    epostaWarning=self.driver.find_element(By.XPATH, r.EPOSTA_WARNING_XPATH)
    assert epostaWarning.text == r.EPOSTA_WARNING_MESSAGE
   
  def test_register_eposta_control2(self):
   
    epostaTextBox= self.driver.find_element(By.XPATH, r.EPOSTA_TEXT_BOX_XPATH)
    epostaTextBox.send_keys(r.VALID_EPOSTA)
    epostaTextBox.clear()
    sleep(5)
    epostaTextBox.send_keys(" ")
    sleep(5)
    epostaWarning=self.driver.find_element(By.XPATH, r.EPOSTA_WARNING_MESSAGE2_XPATH)
    assert epostaWarning.text == r.EPOSTA_WARNING_MESSAGE2

    
  def test_register(self,):
  
    nameTextBox=self.driver.find_element(By.XPATH, r.NAME_TEXT_BOX_XPATH)
    nameTextBox.send_keys(r.REGISTER_NAME)
    lastnameTextBox=self.driver.find_element(By.XPATH, r.LAST_NAME_TEXT_BOX_XPATH)
    lastnameTextBox.send_keys(r.REGISTER_LAST_NAME)
    epostaTextBox=self.driver.find_element(By.XPATH, r.EPOSTA_TEXT_BOX_XPATH)
    epostaTextBox.send_keys(r.REGISTER_EPOSTA)
    passwordTextBox=self.driver.find_element(By.XPATH, r.PASSWORD_TEXT_BOX_XPATH)
    passwordTextBox.send_keys(r.REGISTER_PASSWORD)
    passwordAgainTextBox=self.driver.find_element(By.NAME, r.PASSWORD_AGAIN_TEXT_BOX_NAME)
    passwordAgainTextBox.send_keys(r.REGISTER_PASSWORD)
    sleep(2)
    self.driver.execute_script("window.scrollTo(0,400)") 
    registerButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,r.REGISTER_BUTTON_XPATH)))
    registerButton.click()

  def test_success_register(self):
    
    Test_register.test_register(self)
    sleep(3)
    registerText=self.driver.find_element(By.XPATH, r.REGISTER_TEXT_XPATH)
    assert registerText.text == r.REGISTER_TEXT
    
   

  def test_telephoneNumber_length(self):

    Test_register.test_success_register(self)

    contactCheckBox= self.driver.find_element(By.XPATH, r.CONTACT_XPATH)
    contactCheckBox.click()
    memberShipCheckBox=self.driver.find_element(By.XPATH, r.MEMBERSHIP_XPATH)
    memberShipCheckBox.click()
    emailConfirmationCheckBox=self.driver.find_element(By.XPATH,r.EMAIL_CONFIRMATION_XPATH)
    emailConfirmationCheckBox.click()
    phoneConfirmationCheckBox=self.driver.find_element(By.XPATH, r.PHONE_CONFIRMATION_XPATH)
    phoneConfirmationCheckBox.click()
    phoneNumberTextBox=self.driver.find_element(By.ID, r.PHONE_NUMBER_ID)
    phoneNumberTextBox.send_keys(r.INVALID_PHONE_NUMBER)
    sleep(3)
    iframe=self.driver.find_element(By.XPATH,r.IFRAME_XPATH)
    self.driver.switch_to.frame(iframe)
    captcha=self.driver.find_element(By.XPATH,r.CAPTCHA_XPATH)
    captcha.click()
    self.driver.switch_to.default_content()
    continueButton=self.driver.find_element(By.XPATH, r.CONTINUE_BUTTON_XPATH)
    continueButton.click()
    warningMessage=self.driver.find_element(By.CSS_SELECTOR, r.PHONE_WARNING_MESSAGE_CSS)
    assert warningMessage.text == r.PHONE_WARNING_MESSAGE


  def test_registered_membership(self):
    
    nameTextBox=self.driver.find_element(By.XPATH, r.NAME_TEXT_BOX_XPATH)
    nameTextBox.send_keys(r.REGISTER_NAME)
    lastnameTextBox=self.driver.find_element(By.XPATH, r.LAST_NAME_TEXT_BOX_XPATH)
    lastnameTextBox.send_keys(r.REGISTER_LAST_NAME)
    epostaTextBox=self.driver.find_element(By.XPATH, r.EPOSTA_TEXT_BOX_XPATH)
    epostaTextBox.send_keys(r.VALID_EPOSTA)
    passwordTextBox=self.driver.find_element(By.XPATH, r.PASSWORD_TEXT_BOX_XPATH)
    passwordTextBox.send_keys(r.REGISTER_PASSWORD)
    passwordAgainTextBox=self.driver.find_element(By.NAME, r.PASSWORD_AGAIN_TEXT_BOX_NAME)
    passwordAgainTextBox.send_keys(r.REGISTER_PASSWORD)
    sleep(2)
    self.driver.execute_script("window.scrollTo(0,400)") 
    registerButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,r.REGISTER_BUTTON_XPATH)))
    registerButton.click()
    contactCheckBox= self.driver.find_element(By.XPATH, r.CONTACT_XPATH)
    contactCheckBox.click()
    memberShipCheckBox=self.driver.find_element(By.XPATH, r.MEMBERSHIP_XPATH)
    memberShipCheckBox.click()
    emailConfirmationCheckBox=self.driver.find_element(By.XPATH,r.EMAIL_CONFIRMATION_XPATH)
    emailConfirmationCheckBox.click()
    phoneConfirmationCheckBox=self.driver.find_element(By.XPATH, r.PHONE_CONFIRMATION_XPATH)
    phoneConfirmationCheckBox.click()
    phoneNumberTextBox=self.driver.find_element(By.ID, r.PHONE_NUMBER_ID)
    phoneNumberTextBox.send_keys(r.VALID_PHONE_NUMBER)
    sleep(3)
    iframe=self.driver.find_element(By.XPATH,r.IFRAME_XPATH)
    self.driver.switch_to.frame(iframe)
    captcha=self.driver.find_element(By.XPATH,r.CAPTCHA_XPATH)
    captcha.click()
    self.driver.switch_to.default_content()
    continueButton=self.driver.find_element(By.XPATH, r.CONTINUE_BUTTON_XPATH)
    continueButton.click()
    sleep(6)
    warningMessage=self.driver.find_element(By.XPATH,"//div[@class='toast-body']")
    assert warningMessage.text == "• Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır."