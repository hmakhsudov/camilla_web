# frontend/Dockerfile
FROM node:14

WORKDIR /app

COPY package*.json ./

# Использование npm ci для установки зависимостей
RUN npm ci

COPY . .

RUN npm run build

EXPOSE 8080

CMD ["npm", "run", "serve"]
