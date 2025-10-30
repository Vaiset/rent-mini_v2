FROM node:20-alpine as build
WORKDIR /app
COPY frontend/package.json /app/package.json
RUN npm i --no-audit --no-fund
COPY frontend /app
RUN npm run build

FROM nginx:1.27-alpine
COPY --from=build /app/dist /usr/share/nginx/html
