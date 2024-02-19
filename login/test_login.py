
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
import loginConstants as c

class Test_login():

  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(c.LOGIN_URL)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_epostaPasswordControl(self):
    loginButton=self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_XPATH)
    loginButton.click()
    warningMessage=self.driver.find_element(By.XPATH, c.WARNING_MESSAGE_XPATH)
    sleep(7)
    assert warningMessage.text == c.WARNING_MESSAGE



  @pytest.mark.parametrize("username,password,message", [
        (c.INVALID_EPOSTA, c.VALID_PASSWORD, c.POPUP_MESSAGE_NEGATIVE2),
        (c.VALID_EPOSTA, c.INVALID_PASSWORD,c.POPUP_MESSAGE_NEGATIVE),(c.INVALID_EPOSTA,c.INVALID_PASSWORD,c.POPUP_MESSAGE_NEGATIVE)])
    
  def test_invalidLogin(self,username,password,message):
        
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.EPOSTA_TEXT_BOX_XPATH)))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.PASSWORD_TEXT_BOX_XPATH)))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_XPATH)
        loginButton.click()
        popUpMessage=WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.POPUP_MESSAGE_CSS)))
        sleep(2)
        assert popUpMessage.text== message
        
        



  def test_validLogin(self):
   
    epostaTextBox=self.driver.find_element(By.XPATH, c.EPOSTA_TEXT_BOX_XPATH)
    epostaTextBox.send_keys(c.VALID_EPOSTA)
    passwordTextBox= self.driver.find_element(By.XPATH,c.PASSWORD_TEXT_BOX_XPATH)
    passwordTextBox.send_keys(c.VALID_PASSWORD)
    loginButton=self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_XPATH)
    loginButton.click()
    popUpMessage=WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.POPUP_MESSAGE_CSS)))
    sleep(2)
    assert popUpMessage.text==c.POPUP_MESSAGE_POSITIVE
    
    
   


