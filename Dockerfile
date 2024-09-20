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
    firefox-esr \
    --no-install-recommends

# Instalar Geckodriver
RUN GECKO_DRIVER_VERSION=0.33.0 \
    && wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GECKO_DRIVER_VERSION/geckodriver-v$GECKO_DRIVER_VERSION-linux64.tar.gz \
    && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin \
    && rm /tmp/geckodriver.tar.gz

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar tu código al contenedor
COPY . /app
WORKDIR /app

# Comando para ejecutar tu script
CMD ["python", "loginDescarga.py"]
