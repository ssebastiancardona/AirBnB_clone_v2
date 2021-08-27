#!/usr/bin/env bash
# Install Nginx already installed

sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "\\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\tautoindex off;\n\t}\n" /etc/nginx/sites-available/default
service nginx restart
