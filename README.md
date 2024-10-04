# Networking-and-Servers

# Task 1
#Deploy a website on localhost using either apache2 or Nginx. 
#Create a DNS name for this website as ‘awesomeweb’. 

Step 1: Install Nginx
sudo apt update
sudo apt install nginx -y
sudo systemctl status nginx
sudo systemctl start nginx

Step 2: Create Your Website
sudo mkdir -p /var/www/awesomeweb
sudo nano /var/www/awesomeweb/index.html

Step 3: Set Up Nginx Server Block
sudo nano /etc/nginx/sites-available/awesomeweb

Step 4: Enable the Server Block
sudo ln -s /etc/nginx/sites-available/awesomeweb /etc/nginx/sites-enabled/

Test the configuration for syntax errors:
sudo nginx -t

Step 5: Configure DNS Name on Localhost
sudo nano /etc/hosts
map awesomeweb to IP address


