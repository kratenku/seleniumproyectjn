import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By


class InformacionCliente():
    ingresaTarjeta = "#NUMERO_TARJETA"
    seleTarjetaID = "NUMERO_TARJETA"
    ingresoanioID="FECHA_VENC_ANNO"
    ingresoanioXPHAT="//option[contains(text(),'2031')]"
    ingresaMesven = "FECHA_VENC_MES"
    ingresa_Mes_XPHAT="//option[contains(text(),'10')]"
    seleccionaCvv_css="#CODIGO_SEGURIDAD"
    ingresaCvv = "CODIGO_SEGURIDAD"
    cuotas = "CUOTAS"
    ingresaNombreTarjeta = "#NOMBRE_TARJETA"
    nombreTarjeta = "NOMBRE_TARJETA"
    TipoIdentificacion = "TIPO_DOCUMENTO"
    SelTIpoIdentificacion="//option[contains(text(),'C.C. (Cédula de Ciudadanía)')]"
    NumeroIdentificacion = "#NUMERO_DOCUMENTO"
    Identificacion="NUMERO_DOCUMENTO"
    NumeroTelefono = "#TELEFONO"
    IngresoTel="TELEFONO"
    ingresaCorreo = "#EMAIL"
    correoIngresa="EMAIL"
    EnviaConfirmacion="#mySubmit_"


    def __init__(self, driver):
        self.driver = driver

    def SetSelecciontarjeta(self):
        self.driver.find_element(By.CSS_SELECTOR, self.ingresaTarjeta).click()
        #time.sleep(5)

    def SetingresoNumeroTarjeta(self, nrotarjeta):
        tarjeta = self.driver.find_element(By.ID, self.seleTarjetaID)
        tarjeta.send_keys(nrotarjeta)
        #time.sleep(10)
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

    def SetlistaMes(self):
        selmes=self.driver.find_element(By.ID, self.ingresaMesven)
        selmes.click()
        #time.sleep(0)

    def SetSelMes(self):
      #try:
        mes_seleccion=self.driver.find_element(By.XPATH, self.ingresa_Mes_XPHAT)
        mes_seleccion.click()
        print("Selecciono el mes")
        #time.sleep(5)

      #except NoSuchElementException:
       # pass

    def SetSelCvv(self):
        cick_cvv=self.driver.find_element(By.CSS_SELECTOR, self.seleccionaCvv_css)
        cick_cvv.click()


    def SetIngresaCvv(self,numerocvv):
        in_cvv=self.driver.find_element(By.ID, self.ingresaCvv)
        in_cvv.send_keys(numerocvv)
        #time.sleep(7)

    def SetSelCuota(self):

        sel_cuota=Select(self.driver.find_element(By.ID, self.cuotas))
        sel_cuota.select_by_value('1')
        #sel_cuota.click()

        #for cu in sel_cuota:
         #   print(cu.text)
          #  if cu.text == '1':
           #     cu.click()
                #time.sleep(10)

    #def SetIngCuota(self):
        #in_cuota=self.driver.find_element(By.CSS_SELECTOR, self.ingresoCuotas_css)
        #in_cuota.click()
        #print("Selecciono el valor")


    def SetSelNombre(self):
        sel_nom=self.driver.find_element(By.CSS_SELECTOR, self.ingresaNombreTarjeta)
        sel_nom.click()


    def SetIngresaNombre(self,nombreTarj):
        ing_nombre=self.driver.find_element(By.ID, self.nombreTarjeta)
        ing_nombre.send_keys(nombreTarj)
        #time.sleep(3)

    def SetTipoDoc(self):
        tipo_doc=self.driver.find_element(By.ID,self.TipoIdentificacion)
        tipo_doc.click()
        #time.sleep(10)

    def SetselDoc(self):
        tipocel=self.driver.find_element(By.XPATH, self.SelTIpoIdentificacion)
        tipocel.click()
        #time.sleep(10)


    def SetInDoc(self):
        ingresa=self.driver.find_element(By.CSS_SELECTOR, self.NumeroIdentificacion)
        ingresa.click()
        #time.sleep(10)

    def SetNumDocumento(self, documento):
        ingresaNum=self.driver.find_element(By.ID, self.Identificacion)
        ingresaNum.send_keys(documento)
        #time.sleep(10)

    def SetIngresarCelular(self):
        seleccionaTelefono=self.driver.find_element(By.CSS_SELECTOR, self.NumeroTelefono)
        seleccionaTelefono.click()

    def SetIngresarCelularNum(self, celularNum):
        numeroID=self.driver.find_element(By.ID, self.IngresoTel)
        numeroID.send_keys(celularNum)
        #time.sleep(10)

    def SetSeleccionaCorreo(self):
        SelCorreo=self.driver.find_element(By.CSS_SELECTOR, self.ingresaCorreo)
        SelCorreo.click()

    def SetIngresaCorreo(self, correo):
        correoPrueba=self.driver.find_element(By.ID, self.correoIngresa)
        correoPrueba.send_keys(correo)
        time.sleep(10)


    def SetEnviaConfirmacion(self):
        confirma=self.driver.find_element(By.CSS_SELECTOR, self.EnviaConfirmacion)
        confirma.click()
        time.sleep(10)