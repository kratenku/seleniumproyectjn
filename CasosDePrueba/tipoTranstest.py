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
    nrotarjeta="4111111111111"
    driver=webdriver.Chrome(ChromeDriverManager().install())


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
        time.sleep(20)

        #metodo que llefa desde ConfirmaPago para llenar el fórmulario
        icl=InformacionCliente(self.driver)
        icl.ingresoNumeroTarjeta(self.nrotarjeta)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Prueba completa")


if __name__ == "__main__":
    unittest.main()


