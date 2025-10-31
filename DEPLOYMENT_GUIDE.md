# 🌐 部署指南 | Deployment Guide

本文档详细说明如何将 Superstore Sales Dashboard 部署到生产环境,并嵌入到公司官网。

---

## 📋 目录 | Table of Contents

1. [本地部署](#1-本地部署--local-deployment)
2. [Streamlit Community Cloud (免费)](#2-streamlit-community-cloud-免费推荐)
3. [嵌入到公司官网](#3-嵌入到公司官网)
4. [Docker 容器化部署](#4-docker-容器化部署)
5. [云服务器部署](#5-云服务器部署aws-gcp-azure)
6. [自定义域名配置](#6-自定义域名配置)
7. [安全性与访问控制](#7-安全性与访问控制)

---

## 1. 本地部署 | Local Deployment

### 快速启动 (推荐)
```bash
cd superstore_dashboard
chmod +x start.sh
./start.sh
```

### 手动启动
```bash
# 激活虚拟环境
source venv/bin/activate

# 启动应用
streamlit run superstore_dashboard.py --server.port 8501
```

### 自定义端口
```bash
streamlit run superstore_dashboard.py --server.port 8888
```

---

## 2. Streamlit Community Cloud (免费,推荐)

**最适合**: 作品集展示、客户Demo、初创公司

### 步骤

#### Step 1: 准备GitHub仓库
```bash
# 在GitHub上创建新仓库 (例: superstore-dashboard)

# 初始化Git
cd superstore_dashboard
git init
git add .
git commit -m "Initial commit: Superstore Sales Dashboard"

# 连接远程仓库
git remote add origin https://github.com/YOUR_USERNAME/superstore-dashboard.git
git branch -M main
git push -u origin main
```

#### Step 2: 部署到Streamlit Cloud
1. 访问 [share.streamlit.io](https://share.streamlit.io/)
2. 使用GitHub账号登录
3. 点击 "New app"
4. 选择您的仓库: `YOUR_USERNAME/superstore-dashboard`
5. 设置:
   - **Main file path**: `superstore_dashboard.py`
   - **App URL** (自定义): `your-company-sales-dashboard`
6. 点击 "Deploy!"

#### Step 3: 等待部署完成 (约2-3分钟)
部署完成后,您将获得一个公开链接:
```
https://your-company-sales-dashboard.streamlit.app
```

### 优点
✅ **完全免费** (每月有一定配额)  
✅ **自动HTTPS** (安全加密)  
✅ **GitHub同步** (推送代码自动更新)  
✅ **无需运维** (Streamlit官方管理)

### 缺点
❌ 有Streamlit品牌水印  
❌ 有资源限制 (CPU/内存)  
❌ URL是 `*.streamlit.app` 域名

---

## 3. 嵌入到公司官网

### 方法 A: iFrame 嵌入 (最简单)

**适用场景**: 已有官网,想快速添加Dashboard页面

#### HTML代码
```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>销售数据分析 | Your Company</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }
        .dashboard-container {
            width: 100%;
            height: 100vh;
            overflow: hidden;
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <!-- 替换为您的Dashboard链接 -->
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

#### 集成到现有网站 (WordPress/Wix/Squarespace)
```html
<!-- 在页面中添加以下代码块 -->
<div style="width: 100%; height: 800px;">
    <iframe 
        src="https://your-dashboard.streamlit.app/?embed=true"
        style="width: 100%; height: 100%; border: none; border-radius: 10px;"
        title="Sales Dashboard">
    </iframe>
</div>
```

### 方法 B: 导航链接

在官网导航栏添加一个链接:
```html
<nav>
    <a href="https://www.yourcompany.com">首页</a>
    <a href="https://www.yourcompany.com/about">关于我们</a>
    <a href="https://your-dashboard.streamlit.app" target="_blank">数据分析</a>
    <a href="https://www.yourcompany.com/contact">联系我们</a>
</nav>
```

### 方法 C: 弹出窗口

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

## 4. Docker 容器化部署

**适用场景**: 需要在自己的服务器上运行,保证数据隐私

### Dockerfile
在项目根目录创建 `Dockerfile`:

```dockerfile
# 使用官方Python基础镜像
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

# 安装Python依赖
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

### docker-compose.yml
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

### 构建与运行
```bash
# 构建镜像
docker build -t superstore-dashboard .

# 运行容器
docker run -d -p 8501:8501 --name dashboard superstore-dashboard

# 或使用 docker-compose
docker-compose up -d
```

### 访问
```
http://YOUR_SERVER_IP:8501
```

---

## 5. 云服务器部署(AWS, GCP, Azure)

### 以 AWS EC2 为例

#### Step 1: 创建EC2实例
- **AMI**: Ubuntu 22.04 LTS
- **实例类型**: t3.small (2 vCPU, 2GB RAM)
- **安全组**: 开放 8501 端口

#### Step 2: 连接到服务器
```bash
ssh -i your-key.pem ubuntu@YOUR_EC2_IP
```

#### Step 3: 安装依赖
```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装Python和Git
sudo apt install python3-pip python3-venv git -y

# 克隆代码
git clone https://github.com/YOUR_USERNAME/superstore-dashboard.git
cd superstore-dashboard

# 创建虚拟环境并安装依赖
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Step 4: 使用 systemd 设置开机自启

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

#### Step 5: 配置Nginx反向代理 (可选,推荐)

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

重启Nginx:
```bash
sudo systemctl restart nginx
```

---

## 6. 自定义域名配置

### 场景: 将 `dashboard.yourcompany.com` 指向Dashboard

#### Step 1: 添加DNS记录
在您的域名服务商 (例如: GoDaddy, Cloudflare) 添加 A 记录:

```
类型: A
主机: dashboard
值: YOUR_SERVER_IP
TTL: 自动
```

#### Step 2: 配置SSL证书 (Let's Encrypt)
```bash
# 安装Certbot
sudo apt install certbot python3-certbot-nginx -y

# 获取证书
sudo certbot --nginx -d dashboard.yourcompany.com

# 自动续期
sudo certbot renew --dry-run
```

#### Step 3: 更新Nginx配置
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

## 7. 安全性与访问控制

### 添加基础认证 (HTTP Basic Auth)

#### 方法 A: Nginx层面
```bash
# 创建密码文件
sudo apt install apache2-utils -y
sudo htpasswd -c /etc/nginx/.htpasswd admin
```

Nginx配置:
```nginx
location / {
    auth_basic "Restricted Access";
    auth_basic_user_file /etc/nginx/.htpasswd;
    
    proxy_pass http://localhost:8501;
    # ... 其他配置
}
```

#### 方法 B: Streamlit应用层面

安装 `streamlit-authenticator`:
```bash
pip install streamlit-authenticator
```

在 `superstore_dashboard.py` 开头添加:
```python
import streamlit_authenticator as stauth

# 用户配置
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

if authentication_status == False:
    st.error('Username/password is incorrect')
    st.stop()
elif authentication_status == None:
    st.warning('Please enter your username and password')
    st.stop()

# ... 其余Dashboard代码
```

---

## 📊 部署方案对比

| 方案 | 成本 | 难度 | 速度 | 自定义度 | 推荐场景 |
|-----|------|------|------|---------|---------|
| **Streamlit Cloud** | 免费 | ⭐ | 最快 | 低 | 作品集、Demo |
| **iFrame嵌入** | 免费 | ⭐ | 极快 | 中 | 快速集成 |
| **Docker本地** | 免费 | ⭐⭐⭐ | 中 | 高 | 内部使用 |
| **AWS/GCP/Azure** | $10-50/月 | ⭐⭐⭐⭐ | 中 | 极高 | 生产环境 |
| **自定义域名+SSL** | $15-80/月 | ⭐⭐⭐⭐⭐ | 慢 | 极高 | 企业级 |

---

## ✅ 部署检查清单

部署前确认:
- [ ] 所有依赖已列在 `requirements.txt`
- [ ] 数据文件路径正确
- [ ] 敏感信息 (密码、API密钥) 使用环境变量
- [ ] 防火墙/安全组已开放必要端口
- [ ] SSL证书已配置 (生产环境)
- [ ] 已测试移动端响应式布局
- [ ] 已添加访问控制 (如需要)

---

## 🆘 常见部署问题

### Q1: Streamlit Cloud部署后显示"Error loading app"
**A**: 检查 `requirements.txt` 是否包含所有依赖,确保Python版本兼容 (建议3.8-3.10)。

### Q2: iFrame嵌入后显示空白
**A**: 确保Dashboard URL包含 `?embed=true` 参数,且官网与Dashboard同为HTTPS或HTTP。

### Q3: Docker容器无法访问
**A**: 检查端口映射 (`-p 8501:8501`) 和防火墙设置 (`sudo ufw allow 8501`)。

### Q4: Nginx反向代理后WebSocket连接失败
**A**: 确保Nginx配置包含 `proxy_set_header Upgrade` 和 `Connection "upgrade"`。

---

## 📞 需要帮助?

如果在部署过程中遇到任何问题,欢迎联系技术支持。

---

<div align="center">

**🚀 祝您部署顺利!**

*Make Your Dashboard Live, Empower Your Business*

</div>

