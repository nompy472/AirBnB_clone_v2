#!/usr/bin/env bash
# Setting up the web servers for the deployment of web_static

# Installing Nginx if not already installed
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Creating necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Creating a fake HTML file for testing
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html

# Creating or recreating the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Setting ownership recursively to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Updating Nginx configuration with alias
config_update=$(cat << 'EOF'
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
EOF
)
sudo sed -i "38i\\$config_update" /etc/nginx/sites-available/default

# Restarting Nginx
sudo service nginx restart