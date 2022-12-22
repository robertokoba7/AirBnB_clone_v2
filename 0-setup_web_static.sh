#!/usr/bin/env bash
#A bash script that sets up my server for the deployment of web static

#sudo apt-get upadate
#sudo apt-get install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/
#adding a test string
echo "<h2> welcome </h2>" > /data/web_static/releases/test/index.html
echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        error_page 404 /404.html;
        location = /404.html {
                internal;
        }
        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        location /hbnb_static {
                alias /data/web_static/current/index.html;
        }
}" | sudo tee /etc/nginx/sites-available/default
#symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
#restarting nginx
sudo service nginx restart
