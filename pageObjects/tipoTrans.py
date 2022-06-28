from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class TipoTrans():
    # Lacalizador de elementos
    selectbox_select_css = "#select"
    lista_desplegable_tipotrans_css = ".opcion"
    ingresar_valor_xphat = "//tbody/tr[1]/td[1]/div[1]/label[1]/span[1]"
    numerocuentaID = "NumeroCelular"
    enviartipotrans_css = "#mySubmit_"

    def __init__(self,driver):
        self.driver=driver

    def setSelect(self):
        self.driver.find_element(By.CSS_SELECTOR,self.selectbox_select_css).click()

    def setLista(self,i):
        lista_desplegable_tipotrans = self.driver.find_elements(By.CSS_SELECTOR,self.lista_desplegable_tipotrans_css)
        #time.sleep(10)

        for i in lista_desplegable_tipotrans:
            print(i.text)
            if i.text == 'Pago de Facturas':
                i.click()
                #time.sleep(10)


    def setTipotrans(self):
       try:
        self.driver.find_element(By.XPATH,self.ingresar_valor_xphat).click()
        print("Selecciono tipo trans postpago")
        time.sleep(5)
       except NoSuchElementException:
           print("Selecciono tipo trans")

    def setINgresoCuenta(self,numerocuenta):
        nro=self.driver.find_elements(By.ID, self.numerocuentaID)
        nro[0].send_keys(numerocuenta)


    def setcontinuarFormapago(self):
        self.driver.find_element(By.CSS_SELECTOR,self.enviartipotrans_css).click()









