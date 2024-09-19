from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Configuración de Chrome en modo 'headless' (sin interfaz gráfica)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Especifica la ruta a tu chromedriver
driver = webdriver.Chrome(options=chrome_options)

# Navega a la web que deseas automatizar
driver.get('https://www.llfspuertoreal.es/es/admin/users/database/full.com')

# Espera hasta que aparezca el elemento que necesitas (por ejemplo, un botón)
try:
    # Ejemplo: Esperar a que se cargue el modal y seleccionar los parámetros
    wait = WebDriverWait(driver, 10)
    modal = wait.until(EC.visibility_of_element_located((By.ID, "id-del-modal")))

    # realiza el LOGIN
    userInput = driver.find_element(By.ID, 'ion-input-0')
    userInput.click()  # Seleccionar un parámetro
    userInput.send_keys("adminInformatico")
    
    passInput = driver.find_element(By.ID, 'ion-input-0')
    passInput.click()  # Seleccionar un parámetro
    passInput.send_keys("J22/05/1995")
    

    # Enviar formulario o hacer click en el botón que genera el correo
    enviar_boton = driver.find_element(By.CLASS_NAME, '.clupik-button.main')
    enviar_boton.click()

    print("Interacción con la web completada, esperando el correo...")
except Exception as e:
    print(f"Ocurrió un error durante la automatización: {e}")
finally:
    driver.quit()
