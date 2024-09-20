FROM python:3.9-slim

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    libx11-6 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libxtst6 \
    fonts-liberation \
    xdg-utils \
    libpangocairo-1.0-0 \
    libvulkan1 \
    libxkbcommon0 \
    curl \ 
    --no-install-recommends

# Instalar dependencias
RUN apt-get update && apt-get install -y wget unzip curl

# Instalar Chrome versión 114
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

# Descargar e instalar ChromeDriver versión 114
RUN CHROME_DRIVER_VERSION=114.0.5735.90 \
    && wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar tu código al contenedor
COPY . /app

WORKDIR /app

# Comando para ejecutar tu script
CMD ["python", "loginDescarga.py"]
