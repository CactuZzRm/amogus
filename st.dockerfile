# Используем базовый образ Python
FROM python:3.11-slim

# Установка локалей
RUN apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8

# Установка переменных окружения
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Создаем директорию для приложения
WORKDIR /app

# Копируем файлы приложения
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска приложения
CMD ["gunicorn", "main:app"]
