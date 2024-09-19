import time
import zipfile
import os
import shutil
from loginDescarga import webdriver

# Descargar archivo ZIP
download_dir = "/tmp"  # Koyeb no tiene almacenamiento persistente, así que usa una carpeta temporal
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_dir}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)

# Navegar y descargar
driver.get('url_del_correo_con_enlace')
download_button = driver.find_element_by_id("boton_descargar")  # Cambia esto según el selector correcto
download_button.click()

# Esperar hasta que el archivo se descargue
time.sleep(10)  # Aumenta si es necesario
driver.quit()

# Procesar el ZIP
zip_file_path = os.path.join(download_dir, "archivo.zip")
if os.path.exists(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(download_dir)

    # Suponiendo que el archivo XLS se llama 'archivo.xls'
    xls_file_path = os.path.join(download_dir, "archivo.xls")
    if os.path.exists(xls_file_path):
        # Aquí puedes proceder a subir el archivo XLS a Google Drive
        print("Archivo XLS extraído: ", xls_file_path)
