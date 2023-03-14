import csv
from pyicloud import PyiCloudService

# Ingrese las credenciales de iCloud y la clave de autenticación de dos factores.
apple_id = 'tu_apple_id'
password = 'tu_password'

# Crea una instancia de PyiCloudService.
api = PyiCloudService(apple_id, password)

# Verifica que la autenticación de dos factores está activada.
if not api.requires_2fa:
    print("La autenticación de dos factores no está activada en esta cuenta de iCloud.")
    exit(1)

# Obtiene el código de autenticación de dos factores.
auth_code = input("Ingrese el código de autenticación de dos factores: ")

# Inicia sesión en iCloud con el código de autenticación de dos factores.
if not api.authenticate_with_2fa(auth_code):
    print("Error de autenticación.")
    exit(1)

# Abre el archivo CSV con las notas.
with open('huawei.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    next(reader) # salta la primera fila que contiene los encabezados

    # Itera sobre cada fila del archivo CSV y crea una nota en iCloud.
    for row in reader:
        title = row[0]
        content = row[1]
        api.notes_create(title=title, content=content)

print("Notas creadas con éxito en iCloud.")
