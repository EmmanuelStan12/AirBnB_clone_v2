#!/usr/bin/env bash
# This scripts does some commands to server

sudo apt-get -y update
sudo apt-get -y install nginx
echo "Packages updated"
echo

# configure the firewall
sudo ufw allow 'Nginx HTTP'
echo "Allowed HTTP incoming connections"
echo

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "<html>
	<head></head>
	<body>Holberton School</body>
	</html" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '38i\\t location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart NGINX
sudo service nginx restart
