envsubst '$SERVICE_NAME' < /tmp/index.html.template > /tmp/index.html
nginx -g 'daemon off;'