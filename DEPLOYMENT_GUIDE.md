# 🌐 Deployment Guide (EN/中文)

This document provides detailed instructions on how to deploy the Superstore Sales Dashboard to a production environment and embed it into a company website.

---

**Languages:** [**English**](#-english-version) | [**中文**](#-中文版)

---

## English Version

### 📋 Table of Contents

1.  [Local Deployment](#1-local-deployment)
2.  [Streamlit Community Cloud (Free, Recommended)](#2-streamlit-community-cloud-free-recommended)
3.  [Embedding in a Company Website](#3-embedding-in-a-company-website)
4.  [Docker Containerization](#4-docker-containerization)
5.  [Cloud Server Deployment (AWS, GCP, Azure)](#5-cloud-server-deployment-aws-gcp-azure)
6.  [Custom Domain Configuration](#6-custom-domain-configuration)
7.  [Security & Access Control](#7-security--access-control)

---

### 1. Local Deployment

#### Quick Start (Recommended)
```bash
cd superstore_dashboard
chmod +x start.sh
./start.sh
```

#### Manual Start
```bash
# Activate the virtual environment
source venv/bin/activate

# Launch the app
streamlit run superstore_dashboard.py --server.port 8501
```

#### Custom Port
```bash
streamlit run superstore_dashboard.py --server.port 8888
```

---

### 2. Streamlit Community Cloud (Free, Recommended)

**Best for**: Portfolio showcases, client demos, startups.

#### Steps

**Step 1: Prepare your GitHub Repository**
```bash
# Create a new repository on GitHub (e.g., superstore-dashboard)

# Initialize Git in your local project
cd superstore_dashboard
git init
git add .
git commit -m "Initial commit: Superstore Sales Dashboard"

# Connect to the remote repository
git remote add origin https://github.com/YOUR_USERNAME/superstore-dashboard.git
git branch -M main
git push -u origin main
```

**Step 2: Deploy to Streamlit Cloud**
1.  Visit [share.streamlit.io](https://share.streamlit.io/).
2.  Log in with your GitHub account.
3.  Click "New app".
4.  Select your repository: `YOUR_USERNAME/superstore-dashboard`.
5.  Configure the settings:
    -   **Main file path**: `superstore_dashboard.py`
    -   **App URL** (custom): `your-company-sales-dashboard`
6.  Click "Deploy!".

**Step 3: Wait for Deployment (approx. 2-3 minutes)**
Once deployed, you will get a public link:
```
https://your-company-sales-dashboard.streamlit.app
```

#### Advantages
✅ **Completely Free** (with a monthly quota)
✅ **Automatic HTTPS** (secure encryption)
✅ **GitHub Sync** (pushing code triggers auto-updates)
✅ **Zero Maintenance** (managed by the Streamlit team)

#### Disadvantages
❌ Streamlit branding watermark
❌ Resource limitations (CPU/Memory)
❌ URL is a `*.streamlit.app` subdomain

---

### 3. Embedding in a Company Website

#### Method A: iFrame Embedding (Easiest)

**Use case**: You already have a website and want to quickly add a dashboard page.

**HTML Code**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sales Analytics | Your Company</title>
    <style>
        body { margin: 0; padding: 0; font-family: Arial, sans-serif; }
        .dashboard-container { width: 100%; height: 100vh; overflow: hidden; }
        iframe { width: 100%; height: 100%; border: none; }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <!-- Replace with your dashboard URL -->
        <iframe 
            src="https://your-company-sales-dashboard.streamlit.app/?embed=true"
            title="Sales Dashboard"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
        </iframe>
    </div>
</body>
</html>
```

**Integration with Existing Sites (WordPress/Wix/Squarespace)**
```html
<!-- Add the following code block to your page -->
<div style="width: 100%; height: 800px;">
    <iframe 
        src="https://your-dashboard.streamlit.app/?embed=true"
        style="width: 100%; height: 100%; border: none; border-radius: 10px;"
        title="Sales Dashboard">
    </iframe>
</div>
```

#### Method B: Navigation Link
Add a link to your website's navigation bar:
```html
<nav>
    <a href="https://www.yourcompany.com">Home</a>
    <a href="https://www.yourcompany.com/about">About Us</a>
    <a href="https://your-dashboard.streamlit.app" target="_blank">Data Analytics</a>
    <a href="https://www.yourcompany.com/contact">Contact</a>
</nav>
```

#### Method C: Popup Window
```html
<button onclick="openDashboard()">View Sales Analytics</button>

<script>
function openDashboard() {
    window.open(
        'https://your-dashboard.streamlit.app',
        'Dashboard',
        'width=1400,height=900,menubar=no,toolbar=no,location=no'
    );
}
</script>
```

---

### 4. Docker Containerization

**Use case**: Running on your own server to ensure data privacy.

#### Dockerfile
Create a `Dockerfile` in the project root:
```dockerfile
# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Start command
ENTRYPOINT ["streamlit", "run", "superstore_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### docker-compose.yml
```yaml
version: '3.8'

services:
  dashboard:
    build: .
    container_name: superstore_dashboard
    ports:
      - "8501:8501"
    volumes:
      - ./superstore_data.csv:/app/superstore_data.csv
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
    restart: unless-stopped
```

#### Build and Run
```bash
# Build the image
docker build -t superstore-dashboard .

# Run the container
docker run -d -p 8501:8501 --name dashboard superstore-dashboard

# Or use docker-compose
docker-compose up -d
```

#### Access
```
http://YOUR_SERVER_IP:8501
```

---

### 5. Cloud Server Deployment (AWS, GCP, Azure)

#### Example using AWS EC2

**Step 1: Create an EC2 Instance**
- **AMI**: Ubuntu 22.04 LTS
- **Instance Type**: t3.small (2 vCPUs, 2GB RAM)
- **Security Group**: Open port 8501

**Step 2: Connect to the Server**
```bash
ssh -i your-key.pem ubuntu@YOUR_EC2_IP
```

**Step 3: Install Dependencies**
```bash
# Update the system
sudo apt update && sudo apt upgrade -y

# Install Python and Git
sudo apt install python3-pip python3-venv git -y

# Clone the code
git clone https://github.com/YOUR_USERNAME/superstore-dashboard.git
cd superstore-dashboard

# Create a virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Step 4: Set up Auto-start with systemd**
Create a service file at `/etc/systemd/system/dashboard.service`:
```ini
[Unit]
Description=Superstore Sales Dashboard
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/superstore-dashboard
Environment="PATH=/home/ubuntu/superstore-dashboard/venv/bin"
ExecStart=/home/ubuntu/superstore-dashboard/venv/bin/streamlit run superstore_dashboard.py --server.port 8501 --server.headless true

[Install]
WantedBy=multi-user.target
```
Start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable dashboard
sudo systemctl start dashboard
sudo systemctl status dashboard
```

**Step 5: Configure Nginx as a Reverse Proxy (Optional, Recommended)**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```
Restart Nginx:
```bash
sudo systemctl restart nginx
```

---

### 6. Custom Domain Configuration

**Scenario**: Pointing `dashboard.yourcompany.com` to your dashboard.

**Step 1: Add a DNS Record**
In your domain provider's settings (e.g., GoDaddy, Cloudflare), add an A record:
```
Type: A
Host: dashboard
Value: YOUR_SERVER_IP
TTL: Automatic
```

**Step 2: Configure SSL Certificate (Let's Encrypt)**
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain the certificate
sudo certbot --nginx -d dashboard.yourcompany.com

# Test auto-renewal
sudo certbot renew --dry-run
```

**Step 3: Update Nginx Configuration**
Certbot will automatically update your Nginx config to look like this:
```nginx
server {
    listen 443 ssl http2;
    server_name dashboard.yourcompany.com;

    ssl_certificate /etc/letsencrypt/live/dashboard.yourcompany.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/dashboard.yourcompany.com/privkey.pem;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

---

### 7. Security & Access Control

#### Adding Basic Authentication

**Method A: At the Nginx Level**
```bash
# Create a password file
sudo apt install apache2-utils -y
sudo htpasswd -c /etc/nginx/.htpasswd admin
```
Nginx config:
```nginx
location / {
    auth_basic "Restricted Access";
    auth_basic_user_file /etc/nginx/.htpasswd;
    
    proxy_pass http://localhost:8501;
    # ... other proxy settings
}
```

**Method B: At the Streamlit App Level**
Install `streamlit-authenticator`:
```bash
pip install streamlit-authenticator
```
Add this to the beginning of `superstore_dashboard.py`:
```python
import streamlit_authenticator as stauth

# User configuration
names = ['John Doe', 'Jane Smith']
usernames = ['jdoe', 'jsmith']
passwords = ['password1', 'password2']

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    'some_cookie_name',
    'some_signature_key',
    cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login('Login', 'main')

if not authentication_status:
    st.error('Username/password is incorrect' if username else 'Please enter your username and password')
    st.stop()

# ... rest of the dashboard code
st.write(f'Welcome *{name}*')
# ...
```

---

### 📊 Deployment Options Comparison

| Option              | Cost         | Difficulty | Speed    | Customization | Recommended Use Case    |
|---------------------|--------------|------------|----------|---------------|-------------------------|
| **Streamlit Cloud** | Free         | ⭐          | Fastest  | Low           | Portfolio, Demo         |
| **iFrame Embed**    | Free         | ⭐          | Very Fast| Medium        | Quick Integration       |
| **Docker (Local)**  | Free         | ⭐⭐⭐       | Medium   | High          | Internal Use            |
| **AWS/GCP/Azure**   | $10-50/month | ⭐⭐⭐⭐     | Medium   | Very High     | Production Environment  |
| **Custom Domain**   | $15-80/month | ⭐⭐⭐⭐⭐   | Slow     | Very High     | Enterprise-grade        |

---

### ✅ Deployment Checklist

Before deploying, confirm:
- [ ] All dependencies are listed in `requirements.txt`.
- [ ] Data file paths are correct.
- [ ] Sensitive info (passwords, API keys) is managed via environment variables.
- [ ] The necessary ports are open in the firewall/security group.
- [ ] An SSL certificate is configured for production.
- [ ] The mobile responsive layout has been tested.
- [ ] Access control is implemented if needed.

---

### 🆘 Common Deployment Issues

**Q1: Streamlit Cloud shows "Error loading app".**
**A**: Check if `requirements.txt` includes all dependencies and ensure Python version compatibility (3.8-3.10 recommended).

**Q2: iFrame embed appears blank.**
**A**: Ensure the dashboard URL includes the `?embed=true` parameter and that both the website and dashboard use HTTPS.

**Q3: Docker container is inaccessible.**
**A**: Check port mapping (`-p 8501:8501`) and firewall settings (`sudo ufw allow 8501`).

**Q4: WebSocket connection fails behind Nginx reverse proxy.**
**A**: Make sure the Nginx config includes `proxy_set_header Upgrade` and `Connection "upgrade"`.

---

### 📞 Need Help?

If you encounter any issues during deployment, feel free to contact technical support.

---

<div align="center">

**🚀 Happy Deploying!**

*Make Your Dashboard Live, Empower Your Business*

</div>

---
<br>

## 🇨🇳 中文版

### 📋 目录

1.  [本地部署](#1-本地部署)
2.  [Streamlit Community Cloud (免费, 推荐)](#2-streamlit-community-cloud-免费-推荐)
3.  [嵌入到公司官网](#3-嵌入到公司官网)
4.  [Docker 容器化部署](#4-docker-容器化部署)
5.  [云服务器部署 (AWS, GCP, Azure)](#5-云服务器部署-aws-gcp-azure)
6.  [自定义域名配置](#6-自定义域名配置)
7.  [安全性与访问控制](#7-安全性与访问控制)

---

### 1. 本地部署

#### 快速启动 (推荐)
```bash
cd superstore_dashboard
chmod +x start.sh
./start.sh
```

#### 手动启动
```bash
# 激活虚拟环境
source venv/bin/activate

# 启动应用
streamlit run superstore_dashboard.py --server.port 8501
```

#### 自定义端口
```bash
streamlit run superstore_dashboard.py --server.port 8888
```

---

### 2. Streamlit Community Cloud (免费, 推荐)

**最适合**: 作品集展示、客户 Demo、初创公司。

#### 步骤

**第 1 步: 准备 GitHub 仓库**
```bash
# 在 GitHub 上创建新仓库 (例如: superstore-dashboard)

# 在本地项目中初始化 Git
cd superstore_dashboard
git init
git add .
git commit -m "Initial commit: Superstore Sales Dashboard"

# 连接远程仓库
git remote add origin https://github.com/YOUR_USERNAME/superstore-dashboard.git
git branch -M main
git push -u origin main
```

**第 2 步: 部署到 Streamlit Cloud**
1.  访问 [share.streamlit.io](https://share.streamlit.io/)。
2.  使用 GitHub 账号登录。
3.  点击 "New app"。
4.  选择您的仓库: `YOUR_USERNAME/superstore-dashboard`。
5.  配置设置:
    -   **Main file path**: `superstore_dashboard.py`
    -   **App URL** (自定义): `your-company-sales-dashboard`
6.  点击 "Deploy!"。

**第 3 步: 等待部署完成 (约 2-3 分钟)**
部署完成后，您将获得一个公开链接:
```
https://your-company-sales-dashboard.streamlit.app
```

#### 优点
✅ **完全免费** (每月有一定配额)
✅ **自动 HTTPS** (安全加密)
✅ **GitHub 同步** (推送代码自动更新)
✅ **无需运维** (Streamlit 官方管理)

#### 缺点
❌ 有 Streamlit 品牌水印
❌ 有资源限制 (CPU/内存)
❌ URL 是 `*.streamlit.app` 子域名

---

### 3. 嵌入到公司官网

#### 方法 A: iFrame 嵌入 (最简单)

**适用场景**: 已有官网，想快速添加 Dashboard 页面。

**HTML 代码**
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>销售数据分析 | 您的公司</title>
    <style>
        body { margin: 0; padding: 0; font-family: Arial, sans-serif; }
        .dashboard-container { width: 100%; height: 100vh; overflow: hidden; }
        iframe { width: 100%; height: 100%; border: none; }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <!-- 替换为您的 Dashboard 链接 -->
        <iframe 
            src="https://your-company-sales-dashboard.streamlit.app/?embed=true"
            title="销售仪表板"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
        </iframe>
    </div>
</body>
</html>
```

**集成到现有网站 (WordPress/Wix/Squarespace)**
```html
<!-- 在页面中添加以下代码块 -->
<div style="width: 100%; height: 800px;">
    <iframe 
        src="https://your-dashboard.streamlit.app/?embed=true"
        style="width: 100%; height: 100%; border: none; border-radius: 10px;"
        title="销售仪表板">
    </iframe>
</div>
```

#### 方法 B: 导航链接
在官网导航栏添加一个链接:
```html
<nav>
    <a href="https://www.yourcompany.com">首页</a>
    <a href="https://www.yourcompany.com/about">关于我们</a>
    <a href="https://your-dashboard.streamlit.app" target="_blank">数据分析</a>
    <a href="https://www.yourcompany.com/contact">联系我们</a>
</nav>
```

#### 方法 C: 弹出窗口
```html
<button onclick="openDashboard()">查看销售分析</button>

<script>
function openDashboard() {
    window.open(
        'https://your-dashboard.streamlit.app',
        'Dashboard',
        'width=1400,height=900,menubar=no,toolbar=no,location=no'
    );
}
</script>
```

---

### 4. Docker 容器化部署

**适用场景**: 在自己的服务器上运行，保证数据隐私。

#### Dockerfile
在项目根目录创建 `Dockerfile`:
```dockerfile
# 使用官方 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8501

# 健康检查
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# 启动命令
ENTRYPOINT ["streamlit", "run", "superstore_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### docker-compose.yml
```yaml
version: '3.8'

services:
  dashboard:
    build: .
    container_name: superstore_dashboard
    ports:
      - "8501:8501"
    volumes:
      - ./superstore_data.csv:/app/superstore_data.csv
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
    restart: unless-stopped
```

#### 构建与运行
```bash
# 构建镜像
docker build -t superstore-dashboard .

# 运行容器
docker run -d -p 8501:8501 --name dashboard superstore-dashboard

# 或使用 docker-compose
docker-compose up -d
```

#### 访问
```
http://您的服务器IP:8501
```

---

### 5. 云服务器部署 (AWS, GCP, Azure)

#### 以 AWS EC2 为例

**第 1 步: 创建 EC2 实例**
- **AMI**: Ubuntu 22.04 LTS
- **实例类型**: t3.small (2 vCPU, 2GB RAM)
- **安全组**: 开放 8501 端口

**第 2 步: 连接到服务器**
```bash
ssh -i your-key.pem ubuntu@您的EC2公网IP
```

**第 3 步: 安装依赖**
```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装 Python 和 Git
sudo apt install python3-pip python3-venv git -y

# 克隆代码
git clone https://github.com/YOUR_USERNAME/superstore-dashboard.git
cd superstore-dashboard

# 创建虚拟环境并安装依赖
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**第 4 步: 使用 systemd 设置开机自启**
创建服务文件 `/etc/systemd/system/dashboard.service`:
```ini
[Unit]
Description=Superstore Sales Dashboard
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/superstore-dashboard
Environment="PATH=/home/ubuntu/superstore-dashboard/venv/bin"
ExecStart=/home/ubuntu/superstore-dashboard/venv/bin/streamlit run superstore_dashboard.py --server.port 8501 --server.headless true

[Install]
WantedBy=multi-user.target
```
启动服务:
```bash
sudo systemctl daemon-reload
sudo systemctl enable dashboard
sudo systemctl start dashboard
sudo systemctl status dashboard
```

**第 5 步: 配置 Nginx 反向代理 (可选, 推荐)**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```
重启 Nginx:
```bash
sudo systemctl restart nginx
```

---

### 6. 自定义域名配置

**场景**: 将 `dashboard.yourcompany.com` 指向您的 Dashboard。

**第 1 步: 添加 DNS 记录**
在您的域名服务商 (例如: GoDaddy, Cloudflare) 添加 A 记录:
```
类型: A
主机: dashboard
值: 您的服务器IP
TTL: 自动
```

**第 2 步: 配置 SSL 证书 (Let's Encrypt)**
```bash
# 安装 Certbot
sudo apt install certbot python3-certbot-nginx -y

# 获取证书
sudo certbot --nginx -d dashboard.yourcompany.com

# 测试自动续期
sudo certbot renew --dry-run
```

**第 3 步: 更新 Nginx 配置**
Certbot 会自动更新您的 Nginx 配置，使其类似于:
```nginx
server {
    listen 443 ssl http2;
    server_name dashboard.yourcompany.com;

    ssl_certificate /etc/letsencrypt/live/dashboard.yourcompany.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/dashboard.yourcompany.com/privkey.pem;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

---

### 7. 安全性与访问控制

#### 添加基础认证

**方法 A: Nginx 层面**
```bash
# 创建密码文件
sudo apt install apache2-utils -y
sudo htpasswd -c /etc/nginx/.htpasswd admin
```
Nginx 配置:
```nginx
location / {
    auth_basic "Restricted Access";
    auth_basic_user_file /etc/nginx/.htpasswd;
    
    proxy_pass http://localhost:8501;
    # ... 其他代理设置
}
```

**方法 B: Streamlit 应用层面**
安装 `streamlit-authenticator`:
```bash
pip install streamlit-authenticator
```
在 `superstore_dashboard.py` 开头添加:
```python
import streamlit_authenticator as stauth

# 用户配置
names = ['张三', '李四']
usernames = ['zhangsan', 'lisi']
passwords = ['password123', 'password456']

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    'some_cookie_name', # Cookie 名称
    'some_signature_key', # 签名密钥
    cookie_expiry_days=30 # Cookie 有效期
)

name, authentication_status, username = authenticator.login('登录', 'main')

if not authentication_status:
    st.error('用户名或密码错误' if username else '请输入您的用户名和密码')
    st.stop()

# ... 其余 Dashboard 代码
st.write(f'欢迎 *{name}*')
# ...
```

---

### 📊 部署方案对比

| 方案                | 成本         | 难度   | 速度 | 自定义度 | 推荐场景       |
|---------------------|--------------|--------|------|----------|----------------|
| **Streamlit Cloud** | 免费         | ⭐      | 最快 | 低       | 作品集、Demo   |
| **iFrame 嵌入**     | 免费         | ⭐      | 极快 | 中       | 快速集成       |
| **Docker (本地)**   | 免费         | ⭐⭐⭐   | 中   | 高       | 内部使用       |
| **AWS/GCP/Azure**   | $10-50/月    | ⭐⭐⭐⭐ | 中   | 极高     | 生产环境       |
| **自定义域名**      | $15-80/月    | ⭐⭐⭐⭐⭐| 慢   | 极高     | 企业级         |

---

### ✅ 部署检查清单

部署前确认:
- [ ] 所有依赖已列在 `requirements.txt`。
- [ ] 数据文件路径正确。
- [ ] 敏感信息 (密码、API 密钥) 使用环境变量管理。
- [ ] 防火墙/安全组已开放必要端口。
- [ ] 已为生产环境配置 SSL 证书。
- [ ] 已测试移动端响应式布局。
- [ ] 已根据需要添加访问控制。

---

### 🆘 常见部署问题

**Q1: Streamlit Cloud 部署后显示 "Error loading app"**
**A**: 检查 `requirements.txt` 是否包含所有依赖，并确保 Python 版本兼容 (推荐 3.8-3.10)。

**Q2: iFrame 嵌入后显示空白**
**A**: 确保 Dashboard URL 包含 `?embed=true` 参数，且您的官网和 Dashboard 都使用 HTTPS。

**Q3: Docker 容器无法访问**
**A**: 检查端口映射 (`-p 8501:8501`) 和服务器防火墙设置 (`sudo ufw allow 8501`)。

**Q4: Nginx 反向代理后 WebSocket 连接失败**
**A**: 确保 Nginx 配置包含 `proxy_set_header Upgrade` 和 `Connection "upgrade"` 这两行。

---

### 📞 需要帮助?

如果在部署过程中遇到任何问题，欢迎联系技术支持。

---

<div align="center">

**🚀 祝您部署顺利!**

*让您的 Dashboard 上线，为您的业务赋能*

</div>

