# frontend/Dockerfile
FROM node:14

WORKDIR /app

# Обновление npm до последней версии
RUN npm install -g npm@latest

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

EXPOSE 8080

CMD ["npm", "run", "serve"]
