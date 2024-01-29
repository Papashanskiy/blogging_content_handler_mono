# Используем официальный образ Node.js
FROM node:14

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем файлы package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем все файлы из текущей директории в /app
COPY . .

# Собираем приложение для production с минимизацией
RUN npm run build

# Определяем, какой порт должен быть открыт в контейнере
EXPOSE 8080

# Команда, которая будет запущена при старте контейнера
CMD ["npm", "run", "serve"]
