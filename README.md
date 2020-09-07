
Ejecutable hecho en python que permite la comunicion de entre la impresora termina y el navegador
 
### Software Requerido ###
Python 2.7.10 version 32 bits / 64 bits

### Sistemas operativos compatibles 
Windows 7 windows 10 32/64 bits

### impresoras Certidicadas
 #####  SLK TS 400 (SEWOO)
 #####  SLK TL 202 (SEWOO)
 #####  TM-T88V Receipt (EPSON)

#instalacion de paquetes de pyhton 
- paso 1 actualizar pip
   ```bash
   pip install --upgrade pip
   ```

- paso 2 instalar flask
   ```bash
   pip install flask
   ```

- paso 3 instalar pywin32 (win32print)
   ```bash
   pip install pywin32
   ```

- paso 4 nstalar pyinstaller
   ```bash
   pip install pyinstaller
   ```

#tranformar scritp en archivo executable .exe
  ```bash
  pyinstaller --onefile --noconsole .\impresion-vertical.py
  ```


AL ejecutar esta linea de comando se crear el archivo "impresion-vertical.exe" dentro de la carpeta "dist"

# Ejecutar codigo en consola
  ```
  python impresion-vertical.py
  ```


