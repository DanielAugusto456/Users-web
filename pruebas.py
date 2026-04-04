from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import http.server
import threading
import socketserver
from datetime import datetime
import shutil

class PruebaIdex:
    # Variables de clase para el servidor
    httpd = None
    server_thread = None
    PORT = 8000
    
    @classmethod
    def iniciar_servidor(cls):
        os.chdir(r"C:\Users\marti\OneDrive - Instituto Tecnológico de Las Américas (ITLA)\Itla\Cuatrimestre 5\Programacion 3\Proyectos\Users web")
        
        cls.Handler = http.server.SimpleHTTPRequestHandler
        cls.httpd = socketserver.TCPServer(("", cls.PORT), cls.Handler)
        cls.server_thread = threading.Thread(target=cls.httpd.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()
    
    @classmethod
    def detener_servidor(cls):
        cls.httpd.shutdown()      
        cls.httpd.server_close() 
        cls.httpd = None 
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def abrir_html_local(self):
        self.driver.get(f"http://localhost:{self.PORT}/index.html")
        time.sleep(3)

    def llenar_login(self, nombre, contraseña):
        nombre_input = self.driver.find_element(By.ID, "txt_nombre")
        nombre_input.clear()
        nombre_input.send_keys(nombre)
        time.sleep(2)

        contraseña_input = self.driver.find_element(By.ID, "txt_contraseña")
        contraseña_input.clear()
        contraseña_input.send_keys(contraseña)
        time.sleep(2)

    def llenar_registro(self, nombre, correo, contraseña, confirmar_contraseña):
        nombre_input = self.driver.find_element(By.ID, "txt_name")
        nombre_input.clear()
        nombre_input.send_keys(nombre)
        time.sleep(2)

        correo_input = self.driver.find_element(By.ID, "txt_email")
        correo_input.clear()
        correo_input.send_keys(correo)
        time.sleep(2)

        contraseña_input = self.driver.find_element(By.ID, "txt_password")
        contraseña_input.clear()
        contraseña_input.send_keys(contraseña)
        time.sleep(2)

        confirmar_contraseña_input = self.driver.find_element(By.ID, "txt_confirm_password")
        confirmar_contraseña_input.clear()
        confirmar_contraseña_input.send_keys(confirmar_contraseña)
        time.sleep(2)

    def buscar_dashboard(self, nombre=""):
        busqueda_input = self.driver.find_element(By.ID, "txt_search")
        busqueda_input.clear()
        busqueda_input.send_keys(nombre)
        time.sleep(2)

        busqueda_btn = self.driver.find_element(By.ID, "btn_search")
        busqueda_btn.click()
        time.sleep(2)

    def llenar_form_dashboard(self, nombre, correo, contraseña, confirmar_contraseña):
        nombre_input = self.driver.find_element(By.ID, "txt_name")
        nombre_input.clear()
        nombre_input.send_keys(nombre)
        time.sleep(2)

        correo_input = self.driver.find_element(By.ID, "txt_email")
        correo_input.clear()
        correo_input.send_keys(correo)
        time.sleep(2)

        contraseña_input = self.driver.find_element(By.ID, "txt_password")
        contraseña_input.clear()
        contraseña_input.send_keys(contraseña)
        time.sleep(2)

        confirmar_contraseña_input = self.driver.find_element(By.ID, "txt_confirm_password")
        confirmar_contraseña_input.clear()
        confirmar_contraseña_input.send_keys(confirmar_contraseña)
        time.sleep(2)

    def dashboard_form_enviar(self):
        save_button = self.driver.find_element(By.ID, "btn_save")
        save_button.click()

    def actualizar_user_dashboard(self, nombre):
        actualizar_button = self.driver.find_element(By.ID, f"{nombre}update")
        actualizar_button.click()

    def eliminar_user_dashboard(self, nombre):
        eliminar_button = self.driver.find_element(By.ID, f"{nombre}delete")
        eliminar_button.click()

    def registro_enviar(self):
        registro_button = self.driver.find_element(By.ID, "btn_register")
        registro_button.click()

    def registro_salir(self):
        salir_button = self.driver.find_element(By.ID, "btn_exit")
        salir_button.click()

    def enviar_login(self):
        enviar_button = self.driver.find_element(By.ID, "btn_iniciar")
        enviar_button.click()

    def entrar_registro(self):
        registro_button = self.driver.find_element(By.ID, "btn_registrarse")
        registro_button.click()

    def manejar_alerta(self, aceptar=True):
        try:
            alert = self.wait.until(EC.alert_is_present())
            
            if aceptar:
                alert.accept() 
            else:
                alert.dismiss() 
                
        except Exception as e:
            return None
        
    def tomar_screenshot(self, nombre_archivo):
        ruta_completa = os.path.join(r"C:\Users\marti\OneDrive - Instituto Tecnológico de Las Américas (ITLA)\Itla\Cuatrimestre 5\Programacion 3\Proyectos\Users web\screenshots", f"{nombre_archivo}.png")
        self.driver.save_screenshot(ruta_completa)
        print(f"Screenshot guardado: {ruta_completa}")

    def cerrar_navegador(self):
        self.driver.quit()

if __name__ == '__main__':
    prueba = None;

    try:
        PruebaIdex.iniciar_servidor()
        
        prueba = PruebaIdex()
        prueba.abrir_html_local()
        time.sleep(5)

        # Probando Registro
        prueba.entrar_registro()
        time.sleep(2)

        # prueba negativa
        prueba.llenar_registro("Juanes", "Juanes@gmail.com", "Juan", "Juanes")
        time.sleep(1)

        prueba.tomar_screenshot("1.Prueba negativa de registro")
        
        prueba.registro_enviar()
        time.sleep(3)
        
        prueba.manejar_alerta()
        time.sleep(2)

        # Prueba feliz
        prueba.llenar_registro("Juanes", "Juanes@gmail.com", "Juan", "Juan")
        time.sleep(1)

        prueba.tomar_screenshot("2.Prueba feliz de registro")
        
        prueba.registro_enviar()
        time.sleep(3)
        
        prueba.manejar_alerta()
        time.sleep(2)

        # Probando el login
        print("Ejecutando caso de prueba...")
        # prueba negativa
        prueba.llenar_login("ihabdgsb", "ahhbsdhaa")
        time.sleep(1)

        prueba.tomar_screenshot("3.Prueba negativa de login")

        prueba.enviar_login()
        time.sleep(1)

        prueba.manejar_alerta()
        time.sleep(2)
        
        # Prueba feliz
        print("Ejecutando caso de prueba...")
        prueba.llenar_login("Daniel", "Daniel10")
        time.sleep(2)

        prueba.tomar_screenshot("4.Prueba feliz de login")

        prueba.enviar_login()
        time.sleep(2)

        prueba.manejar_alerta()
        time.sleep(2)

        # Probando el dashboard
        # busqueda completa
        prueba.buscar_dashboard()
        time.sleep(1)

        prueba.tomar_screenshot("5.Prueba de busqueda dashboard")

        # Busqueda especifica
        prueba.buscar_dashboard("Daniel")
        time.sleep(1)

        # Prueba de actualizacion de registro
        prueba.actualizar_user_dashboard("Daniel")
        time.sleep(1)

        prueba.manejar_alerta()
        time.sleep(1)

        prueba.llenar_form_dashboard("Daniel", "DanielMartineZapata@gmail.com", "Daniel10", "Daniel10")
        time.sleep(1)
        
        prueba.dashboard_form_enviar()
        time.sleep(1)

        prueba.manejar_alerta()
        time.sleep(1)

        prueba.buscar_dashboard("Daniel")
        time.sleep(2)

        prueba.tomar_screenshot("6.Prueba de guardado y actualizado, dashboard")

        # Prueba de elminar usuario
        prueba.buscar_dashboard("Juanes")
        time.sleep(2)

        prueba.eliminar_user_dashboard("Juanes")
        time.sleep(1)

        prueba.manejar_alerta()
        time.sleep(1)

        prueba.buscar_dashboard("Juanes")

        prueba.tomar_screenshot("7.Prueba de eliminado usuario, dashboard")
        time.sleep(2)

        prueba.cerrar_navegador()
        
    except Exception as e:
        print(f"Error durante las pruebas: {e}")
    
    finally:
        PruebaIdex.detener_servidor()