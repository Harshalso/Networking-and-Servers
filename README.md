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

# Task 2
1. Create the Python script in any directory and run it.
2. Set up subdomains using Nginx by creating separate server blocks.
3. Modify /etc/hosts to map subdomains to localhost (127.0.0.1).
4. Test subdomain access in the browser.
5. Run the Python script to automatically check the subdomain statuses and display 
   them in a table.

# Task 3
Process Summary:
Installed VirtualBox and set up Ubuntu 22.04 as a VM.
Installed Nginx on the Ubuntu VM and verified its functionality.
Scanned the VM using Nmap from the host machine.

Output:
Starting Nmap ( https://nmap.org ) at 2024-10-04 06:22 UTC
Nmap scan report for 172.23.144.10
Host is up (0.00031s latency).
Not shown: 996 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

