# 🌐 Complete Guide to Embedding Your Dashboard (EN/中文)

---

**Languages:** [**English**](#-english-version) | [**中文**](#-中文版)

---

## 🇬🇧 English Version

### 📋 Table of Contents

1.  [Comparison of Embedding Options](#1-comparison-of-embedding-options)
2.  [Recommended Method: Streamlit Cloud + iFrame](#2-recommended-method-streamlit-cloud--iframe)
3.  [Full Implementation Steps](#3-full-implementation-steps)
4.  [Embedding Code Examples](#4-embedding-code-examples)
5.  [Advanced Optimizations](#5-advanced-optimizations)
6.  [Frequently Asked Questions (FAQ)](#6-frequently-asked-questions-faq)

---

### 1. Comparison of Embedding Options

#### ✅ Recommended Method 1: Streamlit Cloud + iFrame (Easiest)

**Workflow**:
```
Deploy Dashboard to Streamlit Cloud
    ↓
Get a public URL (https://xxx.streamlit.app)
    ↓
Embed into your website using an <iframe>
```

**Pros**:
- ✅ **Free** (via Streamlit Community Cloud)
- ✅ **Extremely Fast Deployment** (under 5 minutes)
- ✅ **Automatic HTTPS**
- ✅ **Syncs with GitHub for Updates**
- ✅ **No Server Maintenance Required**

**Cons**:
- ⚠️ Includes Streamlit branding watermark
- ⚠️ URL is a `*.streamlit.app` subdomain
- ⚠️ Resource limitations (CPU/RAM)

**Best for**: Personal portfolios, blogs, small project showcases.

---

#### ✅ Recommended Method 2: Self-Hosted Server + iFrame (Full Control)

**Workflow**:
```
Deploy Dashboard to your own server (VPS/Cloud)
    ↓
Configure a custom domain (e.g., dashboard.yoursite.com)
    ↓
Embed into your website using an <iframe>
```

**Pros**:
- ✅ **Full Control** (no branding)
- ✅ **Custom Domain**
- ✅ **No Resource Limits**
- ✅ **Data Privacy**

**Cons**:
- ❌ Requires a server ($5-10/month)
- ❌ Requires technical maintenance
- ❌ Longer deployment time

**Best for**: Commercial projects, internal enterprise tools, data-sensitive applications.

---

#### ❌ Not Recommended: Exporting as Static HTML

**Issues**:
- Streamlit is a dynamic, interactive application and cannot be fully exported as a single HTML file.
- Interactive components like PyGWalker require a backend to function.
- Features like filters and real-time updates will not work.

---

### 2. Recommended Method: Streamlit Cloud + iFrame

> **I highly recommend this method** because you can deploy and embed your dashboard in under 5 minutes!

**Why choose this method?**
1.  **Zero Cost**: Streamlit Cloud is completely free for the community tier.
2.  **Zero Maintenance**: No need to buy a server or configure environments.
3.  **Automatic Updates**: Push code to GitHub, and the dashboard updates automatically.
4.  **Professional & Reliable**: A stable and reliable cloud service provided by the Streamlit team.

---

### 3. Full Implementation Steps

#### Step 1: Prepare Your GitHub Repository
```bash
# Navigate to your dashboard directory
cd /path/to/your/superstore_dashboard

# Initialize Git (if you haven't already)
git init

# Add all files
git add .

# Make your first commit
git commit -m "Initial commit: Superstore Sales Dashboard"

# Create a new repository on GitHub (visit github.com/new)
# Recommended repository name: superstore-sales-dashboard

# Link the remote repository (replace with your username)
git remote add origin https://github.com/YOUR_USERNAME/superstore-sales-dashboard.git

# Push your code
git branch -M main
git push -u origin main
```

---

#### Step 2: Deploy to Streamlit Cloud
1.  **Visit Streamlit Cloud**
    -   Go to [share.streamlit.io](https://share.streamlit.io/).
    -   Log in with your GitHub account.
2.  **Create a New App**
    -   Click **"New app"**.
    -   Select your repository: `YOUR_USERNAME/superstore-sales-dashboard`.
    -   Main file path: `superstore_dashboard.py`.
    -   App URL (custom): `superstore-sales-dashboard` or `yourname-sales-dashboard`.
3.  **Deploy**
    -   Click **"Deploy!"**.
    -   Wait 2-3 minutes for the deployment to complete.
4.  **Get Your Public URL**
    ```
    https://superstore-sales-dashboard.streamlit.app
    ```

---

#### Step 3: Embed on Your Website
Choose the method that best fits your website type.

---

### 4. Embedding Code Examples

#### Method A: Full-Screen Standalone Page (Recommended for Portfolios)
**Create a file**: `dashboard.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Superstore Sales Dashboard | Data Analytics Portfolio</title>
    <meta name="description" content="An interactive sales data visualization dashboard built with Streamlit + Plotly.">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Arial', sans-serif; background: #F5F7FA; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header h1 { font-size: 24px; font-weight: 600; }
        .header .nav { display: flex; gap: 30px; }
        .header .nav a { color: white; text-decoration: none; font-size: 16px; transition: opacity 0.3s; }
        .header .nav a:hover { opacity: 0.8; }
        .dashboard-container { width: 100%; height: calc(100vh - 80px); overflow: hidden; }
        iframe { width: 100%; height: 100%; border: none; display: block; }
        .loading { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; font-size: 18px; color: #666; }
        .loading::after { content: '...'; animation: dots 1.5s infinite; }
        @keyframes dots { 0%, 20% { content: '.'; } 40% { content: '..'; } 60%, 100% { content: '...'; } }
        @media (max-width: 768px) {
            .header { flex-direction: column; gap: 15px; padding: 15px 20px; }
            .header h1 { font-size: 20px; }
            .header .nav { gap: 15px; font-size: 14px; }
            .dashboard-container { height: calc(100vh - 120px); }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>📊 Superstore Sales Dashboard</h1>
        <nav class="nav">
            <a href="/">Home</a>
            <a href="/projects">Projects</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    <main class="dashboard-container">
        <div class="loading">Loading Dashboard</div>
        <iframe 
            src="https://superstore-sales-dashboard.streamlit.app/?embed=true"
            title="Superstore Sales Dashboard"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            onload="document.querySelector('.loading').style.display='none'">
        </iframe>
    </main>
</body>
</html>
```
**How to use**:
- Place this file in your website directory as `/dashboard.html`.
- Access it at `https://yourwebsite.com/dashboard.html`.

---

#### Method B: Embed in a Section of an Existing Page
**Use case**: Part of a blog post or portfolio project page.
```html
<section class="portfolio-item">
    <h2>📊 Superstore Sales Dashboard</h2>
    <p>An interactive sales data visualization and analytics platform built with Streamlit + Plotly.</p>
    
    <div style="width: 100%; height: 800px; margin: 30px 0; position: relative; background: #F5F7FA; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
        <iframe 
            src="https://superstore-sales-dashboard.streamlit.app/?embed=true"
            style="width: 100%; height: 100%; border: none;"
            title="Sales Dashboard"
            loading="lazy">
        </iframe>
    </div>
    
    <div style="margin-top: 20px; padding: 20px; background: #E3F2FD; border-left: 4px solid #1565C0; border-radius: 5px;">
        <h3 style="color: #1565C0; margin-bottom: 10px;">💡 Project Highlights</h3>
        <ul style="color: #37474F; line-height: 1.8;">
            <li>📈 7+ interactive charts (Plotly)</li>
            <li>🗺️ US geographic distribution heatmap</li>
            <li>🎨 Drag-and-drop custom analysis with PyGWalker</li>
            <li>🌐 Tri-lingual support (English / Traditional Chinese / Simplified Chinese)</li>
            <li>📱 Fully responsive design for mobile devices</li>
        </ul>
    </div>
    
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://superstore-sales-dashboard.streamlit.app" 
           target="_blank" 
           style="display: inline-block; padding: 12px 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-decoration: none; border-radius: 25px; font-weight: 600;">
            🚀 Open Full Version in New Tab
        </a>
    </div>
</section>
```

---

#### Method C: Embed in a WordPress Site
**Steps**:
1.  Log in to your WordPress dashboard.
2.  Edit a page or post.
3.  Add a **"Custom HTML"** block.
4.  Paste the following code:
```html
<div style="width: 100%; height: 800px; margin: 30px 0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
    <iframe 
        src="https://superstore-sales-dashboard.streamlit.app/?embed=true"
        style="width: 100%; height: 100%; border: none;"
        title="Sales Dashboard">
    </iframe>
</div>
```

---

#### Method D: Embed in a React / Next.js Site
**Component Code**:
```jsx
// components/DashboardEmbed.jsx
import React from 'react';

const DashboardEmbed = () => {
  return (
    <div className="dashboard-wrapper">
      <h2>📊 Superstore Sales Dashboard</h2>
      <div className="dashboard-iframe-container">
        <iframe
          src="https://superstore-sales-dashboard.streamlit.app/?embed=true"
          title="Superstore Sales Dashboard"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
        />
      </div>
      
      <style jsx>{`
        .dashboard-wrapper { max-width: 1400px; margin: 0 auto; padding: 40px 20px; }
        .dashboard-wrapper h2 { font-size: 28px; color: #1565C0; margin-bottom: 20px; text-align: center; }
        .dashboard-iframe-container { position: relative; width: 100%; height: 800px; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
        iframe { width: 100%; height: 100%; border: none; }
        @media (max-width: 768px) { .dashboard-iframe-container { height: 600px; } }
      `}</style>
    </div>
  );
};

export default DashboardEmbed;
```

---

### 5. Advanced Optimizations

#### 1. Hide Streamlit Menu & Footer
In `superstore_dashboard.py`, add the following (skip if already present):
```python
# Hide default Streamlit elements
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
```

#### 2. Control via URL Parameters
You can add parameters to the iFrame's `src`:
```html
<!-- Embed mode (hides the top toolbar) -->
src="https://your-dashboard.streamlit.app/?embed=true"

<!-- Disable scrolling -->
src="https://your-dashboard.streamlit.app/?embed=true&embed_options=disable_scrolling"

<!-- Set a custom theme -->
src="https://your-dashboard.streamlit.app/?embed=true&theme=light"
```

---

### 6. Frequently Asked Questions (FAQ)

**Q1: Why is the iFrame blank?**
**Possible reasons**:
- The dashboard is still deploying (initial deployment on Streamlit Cloud takes 2-3 minutes).
- The URL is incorrect.
- The browser is blocking the cross-origin iFrame.
**Solutions**:
```bash
# 1. Visit the dashboard URL directly to confirm it works
open https://your-dashboard.streamlit.app

# 2. Check the browser console (F12) for errors.
# 3. Ensure the URL includes the ?embed=true parameter.
```

**Q2: How to fix the iFrame height?**
**Solutions**:
```html
<!-- Fixed height -->
<iframe style="height: 800px;"></iframe>

<!-- Viewport height (90% of screen height) -->
<iframe style="height: 90vh;"></iframe>

<!-- Dynamic height (advanced) -->
<iframe id="dashboard-iframe" style="min-height: 800px;"></iframe>
```

---
<br>

## 🇨🇳 中文版

### 📋 目录

1.  [方案对比](#方案对比)
2.  [推荐方案：Streamlit Cloud + iFrame](#推荐方案streamlit-cloud--iframe)
3.  [完整实施步骤](#完整实施步骤)
4.  [嵌入代码示例](#嵌入代码示例)
5.  [高级优化](#高级优化)
6.  [常见问题](#常见问题-faq)

---

### 1. 方案对比

#### ✅ 推荐方案 1：Streamlit Cloud + iFrame 嵌入（最简单）
**流程**：
```
Dashboard 部署到 Streamlit Cloud
    ↓
获得公开链接 (https://xxx.streamlit.app)
    ↓
使用 <iframe> 嵌入到个人网站
```
**优点**：
- ✅ **免费** (通过 Streamlit Community Cloud)
- ✅ **极快部署** (5 分钟内完成)
- ✅ **自动 HTTPS**
- ✅ **与 GitHub 同步更新**
- ✅ **无需服务器运维**
**缺点**：
- ⚠️ 有 Streamlit 品牌水印
- ⚠️ URL 是 `*.streamlit.app` 子域名
- ⚠️ 有资源限制 (CPU/RAM)
**适用场景**：个人作品集、博客、小型项目展示。

---

#### ✅ 推荐方案 2：自托管服务器 + iFrame（完全控制）
**流程**：
```
Dashboard 部署到自己的服务器 (VPS/云服务器)
    ↓
配置自定义域名 (例如: dashboard.yoursite.com)
    ↓
使用 <iframe> 嵌入到个人网站
```
**优点**：
- ✅ **完全控制** (无品牌水印)
- ✅ **自定义域名**
- ✅ **无资源限制**
- ✅ **数据隐私保护**
**缺点**：
- ❌ 需要服务器 ($5-10/月)
- ❌ 需要技术维护
- ❌ 部署时间较长
**适用场景**：商业项目、企业内部工具、对数据隐私有要求的应用。

---

#### ❌ 不推荐方案：导出静态 HTML
**问题**：
- Streamlit 是一个动态交互应用，无法完整导出为单个 HTML 文件。
- PyGWalker 等交互组件需要后端支持才能运行。
- 过滤器和实时更新等功能会失效。

---

### 2. 推荐方案：Streamlit Cloud + iFrame

> **我强烈推荐这个方案**，因为您可以在 5 分钟内完成部署并嵌入网站！

**为什么选择这个方案？**
1.  **零成本**：Streamlit Cloud 的社区版完全免费。
2.  **零运维**：无需购买服务器或配置环境。
3.  **自动更新**：推送代码到 GitHub，Dashboard 会自动更新。
4.  **专业可靠**：由 Streamlit 官方团队提供的稳定云服务。

---

### 3. 完整实施步骤

#### 第一步：准备 GitHub 仓库
```bash
# 进入您的 Dashboard 目录
cd /path/to/your/superstore_dashboard

# 初始化 Git（如果尚未初始化）
git init

# 添加所有文件
git add .

# 提交首次 commit
git commit -m "Initial commit: Superstore Sales Dashboard"

# 在 GitHub 上创建新仓库（访问 github.com/new）
# 仓库名建议：superstore-sales-dashboard

# 连接远程仓库（请替换为您的用户名）
git remote add origin https://github.com/YOUR_USERNAME/superstore-sales-dashboard.git

# 推送代码
git branch -M main
git push -u origin main
```

---

#### 第二步：部署到 Streamlit Cloud
1.  **访问 Streamlit Cloud**
    -   打开 [share.streamlit.io](https://share.streamlit.io/)
    -   使用您的 GitHub 账号登录
2.  **创建新应用**
    -   点击 **"New app"**
    -   选择仓库：`YOUR_USERNAME/superstore-sales-dashboard`
    -   Main file path (主文件路径)：`superstore_dashboard.py`
    -   App URL (应用链接，可自定义)：`superstore-sales-dashboard` 或 `yourname-sales-dashboard`
3.  **部署**
    -   点击 **"Deploy!"**
    -   等待 2-3 分钟完成部署
4.  **获得您的公开链接**
    ```
    https://superstore-sales-dashboard.streamlit.app
    ```

---

#### 第三步：嵌入到您的个人网站
根据您的网站类型，选择对应的嵌入方案。

---

### 4. 嵌入代码示例

#### 方案 A：全屏独立页面（推荐用于作品集）
**创建文件**：`dashboard.html`
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Superstore 销售仪表板 | 数据分析作品</title>
    <meta name="description" content="一个基于 Streamlit + Plotly 构建的交互式销售数据可视化 Dashboard。">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Arial', 'Helvetica', sans-serif; background: #F5F7FA; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header h1 { font-size: 24px; font-weight: 600; }
        .header .nav { display: flex; gap: 30px; }
        .header .nav a { color: white; text-decoration: none; font-size: 16px; transition: opacity 0.3s; }
        .header .nav a:hover { opacity: 0.8; }
        .dashboard-container { width: 100%; height: calc(100vh - 80px); overflow: hidden; }
        iframe { width: 100%; height: 100%; border: none; display: block; }
        .loading { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; font-size: 18px; color: #666; }
        .loading::after { content: '...'; animation: dots 1.5s infinite; }
        @keyframes dots { 0%, 20% { content: '.'; } 40% { content: '..'; } 60%, 100% { content: '...'; } }
        @media (max-width: 768px) {
            .header { flex-direction: column; gap: 15px; padding: 15px 20px; }
            .header h1 { font-size: 20px; }
            .header .nav { gap: 15px; font-size: 14px; }
            .dashboard-container { height: calc(100vh - 120px); }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>📊 Superstore 销售仪表板</h1>
        <nav class="nav">
            <a href="/">首页</a>
            <a href="/projects">项目</a>
            <a href="/about">关于我</a>
            <a href="/contact">联系方式</a>
        </nav>
    </header>
    <main class="dashboard-container">
        <div class="loading">正在加载仪表板</div>
        <iframe 
            src="https://superstore-sales-dashboard.streamlit.app/?embed=true"
            title="Superstore Sales Dashboard"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            onload="document.querySelector('.loading').style.display='none'">
        </iframe>
    </main>
</body>
</html>
```
**使用方式**：
- 将此文件作为 `/dashboard.html` 放在您的网站目录中。
- 通过 `https://yourwebsite.com/dashboard.html` 访问。

---

#### 方案 B：嵌入到现有页面的某个区域
**适用场景**：个人博客文章、作品集页面的一个部分。
```html
<section class="portfolio-item">
    <h2>📊 Superstore 销售仪表板</h2>
    <p>一个基于 Streamlit + Plotly 构建的交互式销售数据可视化分析平台。</p>
    
    <div style="width: 100%; height: 800px; margin: 30px 0; position: relative; background: #F5F7FA; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
        <iframe 
            src="https://superstore-sales-dashboard.streamlit.app/?embed=true"
            style="width: 100%; height: 100%; border: none;"
            title="销售仪表板"
            loading="lazy">
        </iframe>
    </div>
    
    <div style="margin-top: 20px; padding: 20px; background: #E3F2FD; border-left: 4px solid #1565C0; border-radius: 5px;">
        <h3 style="color: #1565C0; margin-bottom: 10px;">💡 项目亮点</h3>
        <ul style="color: #37474F; line-height: 1.8;">
            <li>📈 7+ 种交互式图表 (Plotly)</li>
            <li>🗺️ 美国地理分布热力图</li>
            <li>🎨 使用 PyGWalker 进行拖拽式自定义分析</li>
            <li>🌐 三语言支持 (English / 繁體中文 / 简体中文)</li>
            <li>📱 完全响应式设计，完美适配移动端</li>
        </ul>
    </div>
    
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://superstore-sales-dashboard.streamlit.app" 
           target="_blank" 
           style="display: inline-block; padding: 12px 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-decoration: none; border-radius: 25px; font-weight: 600;">
            🚀 在新标签页打开完整版
        </a>
    </div>
</section>
```

---

#### 方案 C：在 WordPress 网站中嵌入
**步骤**：
1.  登录您的 WordPress 后台。
2.  编辑一个页面或文章。
3.  添加一个 **"自定义 HTML"** 模块。
4.  粘贴以下代码：
```html
<div style="width: 100%; height: 800px; margin: 30px 0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
    <iframe 
        src="https://superstore-sales-dashboard.streamlit.app/?embed=true"
        style="width: 100%; height: 100%; border: none;"
        title="销售仪表板">
    </iframe>
</div>
```

---

#### 方案 D：在 React / Next.js 网站中嵌入
**组件代码**：
```jsx
// components/DashboardEmbed.jsx
import React from 'react';

const DashboardEmbed = () => {
  return (
    <div className="dashboard-wrapper">
      <h2>📊 Superstore 销售仪表板</h2>
      <div className="dashboard-iframe-container">
        <iframe
          src="https://superstore-sales-dashboard.streamlit.app/?embed=true"
          title="Superstore Sales Dashboard"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
        />
      </div>
      
      <style jsx>{`
        .dashboard-wrapper { max-width: 1400px; margin: 0 auto; padding: 40px 20px; }
        .dashboard-wrapper h2 { font-size: 28px; color: #1565C0; margin-bottom: 20px; text-align: center; }
        .dashboard-iframe-container { position: relative; width: 100%; height: 800px; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
        iframe { width: 100%; height: 100%; border: none; }
        @media (max-width: 768px) { .dashboard-iframe-container { height: 600px; } }
      `}</style>
    </div>
  );
};

export default DashboardEmbed;
```

---

### 5. 高级优化

#### 1. 隐藏 Streamlit 菜单和页脚
在 `superstore_dashboard.py` 中添加以下代码 (如果已有则跳过):
```python
# 隐藏 Streamlit 默认元素
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
```

#### 2. 通过 URL 参数控制
您可以在 iFrame 的 `src` 属性中添加参数：
```html
<!-- 嵌入模式 (隐藏顶部工具栏) -->
src="https://your-dashboard.streamlit.app/?embed=true"

<!-- 禁用滚动 -->
src="https://your-dashboard.streamlit.app/?embed=true&embed_options=disable_scrolling"

<!-- 设置自定义主题 -->
src="https://your-dashboard.streamlit.app/?embed=true&theme=light"
```

---

### 6. 常见问题 (FAQ)

**Q1: 为什么 iFrame 显示空白？**
**可能原因**:
- Dashboard 还在部署中 (Streamlit Cloud 首次部署需 2-3 分钟)。
- URL 地址错误。
- 浏览器阻止了跨域 iFrame。
**解决方案**:
```bash
# 1. 直接访问 Dashboard URL 确认其是否正常工作
open https://your-dashboard.streamlit.app

# 2. 检查浏览器控制台 (F12) 是否有错误信息。
# 3. 确保 URL 中包含 ?embed=true 参数。
```

**Q2: 如何修复 iFrame 高度不合适的问题？**
**解决方案**:
```html
<!-- 固定高度 -->
<iframe style="height: 800px;"></iframe>

<!-- 视口高度 (屏幕高度的 90%) -->
<iframe style="height: 90vh;"></iframe>

<!-- 使用 JavaScript 动态调整高度 (高级) -->
<iframe id="dashboard-iframe" style="min-height: 800px;"></iframe>
```

---

