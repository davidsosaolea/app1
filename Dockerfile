# Usa la imagen base de Python
FROM python:3.10.6

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el contenido actual al contenedor en /app
COPY . /app

# Instala las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación cuando se inicia el contenedor
CMD ["python", "app.py"]
