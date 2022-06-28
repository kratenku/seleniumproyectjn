from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from random import uniform, randint
from time import sleep, time


class SelFormaPago():
    despliegaOpcionpago_Css="#select"
    opcionPago_css=".opcion"
    captchaXphat="//body/section[1]/div[1]/div[3]/div[1]/div[8]/form[1]/div[9]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/iframe[1]"
    enviaconfirmacion="#mySubmit_"


    def __init__(self,driver):
          self.driver=driver


    def setDespleForma(self):
          self.driver.find_element(By.CSS_SELECTOR,self.despliegaOpcionpago_Css).click()



    def setDespleFormaPago(self):
        Selección_Formapago = self.driver.find_elements(By.CSS_SELECTOR,self.opcionPago_css)

        for pf in Selección_Formapago:
            print(pf.text)
            if pf.text == 'Tarjeta de Crédito - Débito':
               pf.click()



    def setLlenarCaptcha(self):
      try:
        self.driver.find_element(By.XPATH,self.captchaXphat).click()

      except NoSuchElementException:
          print("Controlado")


    def setContinuarConfirmacion(self):
        self.driver.find_element(By.CSS_SELECTOR,self.enviaconfirmacion).click()