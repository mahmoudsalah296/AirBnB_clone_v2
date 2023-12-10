#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Mahmoud Salah" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html index.htm;
    add_header X-Served-By $HOSTNAME;

    location /redirect_me {
        return 301 https://github.com/mahmoudsalah296;
    }

    error_page 404 /404.html;
    location /404 {
        root /etc/nginx/html;
        internal;
    }

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    }
}" > /etc/nginx/sites-available/default

service nginx restart
