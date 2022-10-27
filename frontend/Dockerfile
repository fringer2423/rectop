FROM node:17-alpine

WORKDIR /usr/src/app/frontend

COPY ./package*.json .

COPY . .

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]