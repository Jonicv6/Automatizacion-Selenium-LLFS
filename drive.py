from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Autenticación con Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Autenticación local
drive = GoogleDrive(gauth)

# Subir el archivo XLS a Google Drive
file_drive = drive.CreateFile({'title': 'archivo.xls', 'parents': [{'id': 'ID_de_la_carpeta'}]})
file_drive.SetContentFile('archivo.xls')
file_drive.Upload()
print("Archivo subido correctamente")
