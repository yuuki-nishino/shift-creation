FROM node:17.5.0
RUN mkdir -p /code

ENV NODE_ENV=development
WORKDIR /code

RUN yarn install
RUN yarn add @nuxtjs/axios

RUN npm install -g npm
RUN npm install vue-google-charts
RUN npm i

WORKDIR /code

EXPOSE 3030