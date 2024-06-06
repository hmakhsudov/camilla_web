# frontend/Dockerfile
FROM node:14

WORKDIR /app

# Установка конкретной версии npm
RUN npm install -g npm@6

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

EXPOSE 8080

CMD ["npm", "run", "serve"]
