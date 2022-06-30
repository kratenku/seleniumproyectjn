import time

from selenium.webdriver.common.by import By

class InformacionCliente():

    ingresaTarjeta="#NUMERO_TARJETA"
    ingresaAnioVen="#FECHA_VENC_ANNO"
    ingresaMesven="#FECHA_VENC_MES"
    ingresaNombreTarjeta="#NOMBRE_TARJETA"
    ingresaCvv="#CODIGO_SEGURIDAD"
    ingresaCorreo="#EMAIL"
    cuotas="#CUOTAS"
    TipoIdentificacion="#TIPO_DOCUMENTO"
    NumeroIdentificacion="#NUMERO_DOCUMENTO"
    NumeroTelefono="#TELEFONO"


    def __init__(self,driver):
        self.driver=driver


    def ingresoNumeroTarjeta(self,nrotarjeta):

        self.driver.execute_script("validaTarjeta(); $('#NUMERO_TARJETA').valid();")
        tarjeta=self.driver.find_element(By.ID,self.ingresaTarjeta)
        tarjeta[0].send_key(nrotarjeta)
        time.sleep(10)

