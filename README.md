# **Proyecto Cripter**

## **Descripción General**

Este proyecto contiene un conjunto de programas en Python para cifrar y descifrar mensajes. Incluye dos versiones de línea de comandos (Cripter.py y Cripter2.0.py) y una versión con una interfaz gráfica de usuario (With\_UI.py).

## **Cripter.py**

Esta es la versión básica del programa. Utiliza un método de cifrado similar al de un cifrado César personalizado para la encriptación y desencriptación. La "clave" se utiliza para crear un nuevo alfabeto, que luego se desplaza en función de la longitud de la clave.

### **Características**

* **Encriptación/Desencriptación Sencilla:** Cifra y descifra mensajes utilizando una clave.  
* **Interfaz de Línea de Comandos:** Fácil de usar directamente desde la terminal.

### **Cómo usar**

1. Ejecuta el programa desde la línea de comandos:  
   python Cripter.py

2. Sigue las instrucciones en pantalla para elegir entre encriptar, desencriptar o salir.

## **Cripter2.0.py**

Esta versión implementa el cifrado de Vigenère, un método de encriptación más robusto que el de la versión original Cripter.py. El programa utiliza un cuadrado de Vigenère para cifrar y descifrar mensajes con una palabra clave.

### **Características**

* **Cifrado de Vigenère:** Utiliza un cifrado de sustitución polialfabético clásico para una encriptación más fuerte.  
* **Interfaz de Línea de Comandos:** Al igual que Cripter.py, se ejecuta directamente desde la terminal.

### **Cómo usar**

1. Ejecuta el programa desde la línea de comandos:  
   python Cripter2.0.py

2. Sigue las instrucciones en pantalla. El programa repetirá automáticamente la clave para que coincida con la longitud del mensaje.

## **With\_UI.py**

Este programa proporciona una interfaz gráfica de usuario (GUI) para las funciones de encriptación y desencriptación de Cripter.py. Está construido con la biblioteca customtkinter, lo que ofrece una experiencia más amigable para el usuario que las versiones de línea de comandos.

### **Características**

* **Interfaz Gráfica:** Una interfaz moderna y fácil de usar con secciones separadas para encriptar y desencriptar.  
* **Modos Intercambiables:** Utiliza un botón segmentado para cambiar entre los modos "Encrypt" (Encriptar) y "Decrypt" (Desencriptar).  
* **Salida en Vivo:** Muestra el mensaje encriptado o desencriptado en un cuadro de texto.

### **Requisitos previos**

* Para ejecutar With\_UI.py, necesitas instalar la biblioteca customtkinter. Puedes instalarla usando pip:  
  pip install customtkinter

* El archivo With\_UI.py también depende de que Cripter.py se encuentre en el mismo directorio.

### **Cómo usar**

1. Asegúrate de tener customtkinter instalado y ambos archivos, With\_UI.py y Cripter.py, en la misma carpeta.  
2. Ejecuta el programa desde la línea de comandos:  
   python With\_UI.py

3. Usa la GUI para ingresar tu mensaje y clave, y luego haz clic en el botón "Encrypt" o "Decrypt".

4. Para utilizar el otro cifrado, cambia la segunda linea del codigo: "from Cripter import encrypt, decrypt" a "from Cripter 2.0 import encrypt, decrypt"
