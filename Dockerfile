# Usa una imagen ligera de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expón el puerto 8080 (necesario para Cloud Run)
EXPOSE 8080

# Comando para ejecutar tu app Flask
CMD ["python", "app.py"]
