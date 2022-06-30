import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By


class InformacionCliente():
    ingresaTarjeta = "#NUMERO_TARJETA"
    seleTarjetaID = "NUMERO_TARJETA"
    ingresoanioID="FECHA_VENC_ANNO"
    ingresoanioXPHAT="//option[contains(text(),'2031')]"
    #ingresaAnioVenCss = "#FECHA_VENC_ANNO"
    # ingresaAnioVenID="FECHA_VENC_MES"
    ingresaMesven = "FECHA_VENC_MES"
    ingresa_Mes_XPHAT="//option[contains(text(),'10')]"
    ingresaNombreTarjeta = "#NOMBRE_TARJETA"
    ingresaCvv = "#CODIGO_SEGURIDAD"
    ingresaCorreo = "#EMAIL"
    cuotas = "#CUOTAS"
    TipoIdentificacion = "#TIPO_DOCUMENTO"
    NumeroIdentificacion = "#NUMERO_DOCUMENTO"
    NumeroTelefono = "#TELEFONO"

    def __init__(self, driver):
        self.driver = driver

    def SetSelecciontarjeta(self):
        self.driver.find_element(By.CSS_SELECTOR, self.ingresaTarjeta).click()
        time.sleep(5)

    def SetingresoNumeroTarjeta(self, nrotarjeta):
        tarjeta = self.driver.find_element(By.ID, self.seleTarjetaID)
        tarjeta.send_keys(nrotarjeta)
        time.sleep(10)
        self.driver.execute_script("validaTarjeta(); $('#NUMERO_TARJETA').valid();")


    def Setdesplegaranio(self):
        sel= self.driver.find_element(By.ID, self.ingresoanioID)
        sel.click()
        #time.sleep(10)

    def Setlistafecha(self):
     #try:
      Anio_seleccion = self.driver.find_element(By.XPATH, self.ingresoanioXPHAT)
      Anio_seleccion.click()
      print("Lo selecciono")
      #time.sleep(1000)

          #"""for _an in Anio_seleccion:
            #print(_an.text)
            #if _an.text == '2031':
             #   _an.click()"""

     #except NoSuchElementException:
         #print("No lo encontro")