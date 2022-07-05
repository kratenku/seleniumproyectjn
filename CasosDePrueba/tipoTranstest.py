import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from pageObjects.tipoTrans import TipoTrans
from pageObjects.FormaPago import SelFormaPago
from pageObjects.ConfirmaPago import InformacionCliente
#import sys
#sys.path.append("C:\Users\jhon.salazar\Documents\pythonpractiques\pythonProject2\CasosDePrueba")


class PruebaUno(unittest.TestCase):
    urlAcceso="https://pruebasclaro.maxgp.com.co:9443/index.php?view=vistas/personal/claro/newclaro/inicio.php&id_objeto=#no-back-button"
    #postpago=""
    i="Pago de Facturas"
    #pf="Tarjeta de Crédito - Débito"
    primervalor = "solicitud"
    segundovalor = "solicitud"
    respuesta = "La solicitud paso"
    confirmap = "claro"
    #confirmas = "oportunidad"
    respuestaConfirma = "Esta en la vista de oportunidad confirmacion"
    numerocuenta=3115046028
    nrotarjeta=4111111111111111
    #_an = "2031"
    numerocvv=777
    nombreTarj="APPROVED"
    documento=1234190750
    celularNum=3007392184
    correo="kratenku@gmail.com"
    driver = webdriver.Chrome(ChromeDriverManager().install())


    @classmethod
    def setUp(cls):
        cls.driver.get(cls.urlAcceso)
        cls.driver.maximize_window()
        #cls.driver.get_screenshot_as_file("C:\\Users\\jhon.salazar\\Documents\\pythonpractiques\\pythonProject2\\screenshots\\prueba.png")

    def test_TipotransIngresoNumero(self):
        tp=TipoTrans(self.driver)
        tp.setSelect()
        tp.setLista(self.i)
        time.sleep(5)
        tp.setTipotrans()
        tp.setINgresoCuenta(self.numerocuenta)
        #Continuar con la transacción y assercciones que permiten buscar valores en pantalla
        tp.setcontinuarFormapago()
        #Llena la información del cliente en la vista de confirmación de pago


        if self.primervalor:
            self.assertEqual(self.primervalor, self.segundovalor, self.respuesta)
            print("Error de petición")

        else:
             self.assertEqual(self.confirmap, self.driver.title, self.respuestaConfirma)
             print("Permitio continuar a vista de confirmación")

        fp=SelFormaPago(self.driver)
        fp.setDespleForma()
        fp.setDespleFormaPago()
        #time.sleep(10)
        fp.setLlenarCaptcha()
        time.sleep(15)
        fp.setContinuarConfirmacion()

    #def test_LlenarFormularioPago(self):

        #clase que llefa desde ConfirmaPago para llenar el fórmulario
        icl=InformacionCliente(self.driver)
        icl.SetSelecciontarjeta()
        icl.SetingresoNumeroTarjeta(self.nrotarjeta)
        icl.Setdesplegaranio()
        icl.Setlistafecha()
        icl.SetlistaMes()
        icl.SetSelMes()
        icl.SetSelCvv()
        icl.SetIngresaCvv(self.numerocvv)
        icl.SetSelCuota()
        #icl.SetIngCuota()
        icl.SetSelNombre()
        icl.SetIngresaNombre(self.nombreTarj)
        icl.SetTipoDoc()
        icl.SetselDoc()
        icl.SetInDoc()
        icl.SetNumDocumento(self.documento)
        icl.SetIngresarCelular()
        icl.SetIngresarCelularNum(self.celularNum)
        icl.SetSeleccionaCorreo()
        icl.SetIngresaCorreo(self.correo)
        icl.SetEnviaConfirmacion()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Prueba completa")


if __name__ == "__main__":
    unittest.main()


