FROM nginx:alpine

RUN apk add --no-cache gettext

COPY ./app/index.html /usr/share/nginx/html/index.html.template
COPY ./app/styles.css /usr/share/nginx/html/styles.css
COPY start.sh /start.sh
RUN chmod +x /start.sh

ENV SERVICE_NAME="Docker"

EXPOSE 80
CMD [ "/start.sh" ]