envsubst '$SERVICE_NAME' < /usr/share/nginx/html/index.html.template > /usr/share/nginx/html/index.html
nginx -g 'daemon off;'