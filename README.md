# Jiitak Project

## Overview
The Jiitak Project is a web application built with Python Flask, designed to interact with an AWS RDS MySQL database. This project showcases a complete CI/CD pipeline using Jenkins, along with containerization via Docker, deployment on AWS EC2, and a web server setup with Nginx. The project is also integrated with GitHub for version control and utilizes webhooks to trigger builds automatically.

## Technologies Used
- **Python**: Backend programming language.
- **Flask**: Lightweight web framework for building the application.
- **AWS RDS**: Managed relational database service for MySQL.
- **MySQL**: Database engine.
- **Docker**: Containerization tool to package the application.
- **Jenkins**: CI/CD server for automated builds and deployments.
- **Git**: Version control system.
- **GitHub**: Code hosting platform for version control and collaboration.
- **Nginx**: Web server for serving the application.
- **EC2**: Amazon Elastic Compute Cloud for hosting the application.

## Features
- User authentication and authorization.
- CRUD operations with the MySQL database.
- Dockerized application for easy deployment.
- Automated deployment pipeline using Jenkins.
- Webhook integration for automatic builds on code push to GitHub.

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Docker
- Jenkins
- AWS Account

## Accessing the Web Application
- url: http://13.200.27.78

## Steps to Set Up the Project

### 1. Update Package List and Upgrade Installed Packages
```bash
sudo apt update -y
sudo apt upgrade -y
```

### 2. Install Required Dependencies
Install Java runtime environment:
```bash
sudo apt install -y fontconfig openjdk-17-jre
```
Verify the Java installation:
```bash
java -version
```

### 3. Install Jenkins
#### Add Jenkins Key and Repository
```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/" | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
```

#### Install Jenkins
Update the package list and install Jenkins:
```bash
sudo apt update
sudo apt install -y jenkins
```

Enable Jenkins to start at boot:
```bash
sudo systemctl enable jenkins
```
Start the Jenkins service:
```bash
sudo systemctl start jenkins
```
Check Jenkins service status:
```bash
sudo systemctl status jenkins
```

Retrieve the initial admin password:
```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

### 4. Install Docker
Install Docker:
```bash
sudo apt install docker.io -y
```
Add the required users to the Docker group:
```bash
sudo usermod -aG docker ubuntu
sudo usermod -aG docker jenkins
```

Verify Jenkins’ group membership:
```bash
groups jenkins
```

Update permissions for the Docker socket:
```bash
sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock
```
Restart the Jenkins service:
```bash
sudo systemctl restart jenkins
```

### 5. Configure Nginx
#### Install Certbot and Nginx
```bash
sudo apt install certbot python3-certbot-nginx -y
```

#### Create and Configure Nginx Site
Create a symbolic link to the Nginx configuration file:
```bash
sudo ln -s /etc/nginx/sites-available/jyothis.com /etc/nginx/sites-enabled/jyothis.com
```

Edit the configuration file:
```bash
sudo nano /etc/nginx/sites-available/jyothis.com
```

#### Test and Reload Nginx Configuration
Test the Nginx configuration:
```bash
sudo nginx -t
```

Reload the Nginx service:
```bash
sudo systemctl reload nginx
```

---
