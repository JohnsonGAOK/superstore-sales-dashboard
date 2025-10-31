# 🌐 Dashboard 嵌入个人网站完整指南

## 📋 目录

1. [方案对比](#方案对比)
2. [推荐方案：Streamlit Cloud + iFrame](#推荐方案streamlit-cloud--iframe)
3. [完整实施步骤](#完整实施步骤)
4. [嵌入代码示例](#嵌入代码示例)
5. [高级优化](#高级优化)
6. [常见问题](#常见问题)

---

## 方案对比

### ✅ 推荐方案 1：Streamlit Cloud + iFrame 嵌入（最简单）

**流程**：
```
Dashboard 部署到 Streamlit Cloud
    ↓
获得公开链接 (https://xxx.streamlit.app)
    ↓
使用 <iframe> 嵌入到个人网站
```

**优点**：
- ✅ **免费** (Streamlit Community Cloud)
- ✅ **极快部署** (5分钟完成)
- ✅ **自动 HTTPS**
- ✅ **GitHub 同步更新**
- ✅ **无需服务器运维**

**缺点**：
- ⚠️ 有 Streamlit 品牌水印
- ⚠️ URL 是 `*.streamlit.app`
- ⚠️ 有资源限制 (CPU/RAM)

**适用场景**：个人作品集、博客、小型项目展示

---

### ✅ 推荐方案 2：自托管服务器 + iFrame（完全控制）

**流程**：
```
Dashboard 部署到自己的服务器 (VPS/云服务器)
    ↓
配置域名 (dashboard.yoursite.com)
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

**适用场景**：商业项目、企业内部使用、需要数据隐私

---

### ❌ 不推荐方案：导出静态 HTML

**问题**：
- Streamlit 是动态交互应用，无法完整导出为单个 HTML
- PyGWalker 等交互组件需要后端支持
- 过滤器和实时更新功能会失效

---

## 推荐方案：Streamlit Cloud + iFrame

> **我强烈推荐这个方案**，因为您可以在 5 分钟内完成部署并嵌入网站！

### 为什么选择这个方案？

1. **零成本** - Streamlit Cloud 完全免费
2. **零运维** - 无需购买服务器，无需配置环境
3. **自动更新** - 推送代码到 GitHub，Dashboard 自动更新
4. **专业可靠** - Streamlit 官方提供的云服务，稳定可靠

---

## 完整实施步骤

### 第一步：准备 GitHub 仓库

```bash
# 进入 Dashboard 目录
cd /Users/gaozikai/Documents/cursor来做数据可视化/AI员工关系/superstore_dashboard

# 初始化 Git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: Superstore Sales Dashboard"

# 在 GitHub 上创建新仓库（访问 github.com/new）
# 仓库名建议：superstore-sales-dashboard

# 连接远程仓库（替换为您的用户名）
git remote add origin https://github.com/YOUR_USERNAME/superstore-sales-dashboard.git

# 推送代码
git branch -M main
git push -u origin main
```

---

### 第二步：部署到 Streamlit Cloud

1. **访问 Streamlit Cloud**
   - 打开 [share.streamlit.io](https://share.streamlit.io/)
   - 使用 GitHub 账号登录

2. **创建新应用**
   - 点击 **"New app"**
   - 选择仓库：`YOUR_USERNAME/superstore-sales-dashboard`
   - Main file path：`superstore_dashboard.py`
   - App URL（自定义）：`superstore-sales-dashboard` 或 `yourname-sales-dashboard`

3. **部署**
   - 点击 **"Deploy!"**
   - 等待 2-3 分钟完成部署

4. **获得公开链接**
   ```
   https://superstore-sales-dashboard.streamlit.app
   ```

---

### 第三步：嵌入到个人网站

根据您的网站类型选择对应方案：

---

## 嵌入代码示例

### 方案 A：全屏独立页面（推荐用于作品集）

**创建文件**：`dashboard.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Superstore Sales Dashboard | 数据分析作品</title>
    <meta name="description" content="基于 Streamlit + Plotly 的交互式销售数据可视化 Dashboard">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', 'Helvetica', sans-serif;
            background: #F5F7FA;
        }
        
        /* 顶部导航栏（可选） */
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            font-size: 24px;
            font-weight: 600;
        }
        
        .header .nav {
            display: flex;
            gap: 30px;
        }
        
        .header .nav a {
            color: white;
            text-decoration: none;
            font-size: 16px;
            transition: opacity 0.3s;
        }
        
        .header .nav a:hover {
            opacity: 0.8;
        }
        
        /* Dashboard 容器 */
        .dashboard-container {
            width: 100%;
            height: calc(100vh - 80px);
            overflow: hidden;
        }
        
        /* iFrame 样式 */
        iframe {
            width: 100%;
            height: 100%;
            border: none;
            display: block;
        }
        
        /* 加载提示 */
        .loading {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            font-size: 18px;
            color: #666;
        }
        
        .loading::after {
            content: '...';
            animation: dots 1.5s infinite;
        }
        
        @keyframes dots {
            0%, 20% { content: '.'; }
            40% { content: '..'; }
            60%, 100% { content: '...'; }
        }
        
        /* 响应式设计 */
        @media (max-width: 768px) {
            .header {
                flex-direction: column;
                gap: 15px;
                padding: 15px 20px;
            }
            
            .header h1 {
                font-size: 20px;
            }
            
            .header .nav {
                gap: 15px;
                font-size: 14px;
            }
            
            .dashboard-container {
                height: calc(100vh - 120px);
            }
        }
    </style>
</head>
<body>
    <!-- 顶部导航栏（可选） -->
    <header class="header">
        <h1>📊 Superstore Sales Dashboard</h1>
        <nav class="nav">
            <a href="/">首页</a>
            <a href="/projects">项目</a>
            <a href="/about">关于我</a>
            <a href="/contact">联系方式</a>
        </nav>
    </header>
    
    <!-- Dashboard 主体 -->
    <div class="dashboard-container">
        <div class="loading">Loading Dashboard</div>
        <iframe 
            src="https://superstore-sales-dashboard.streamlit.app/?embed=true"
            title="Superstore Sales Dashboard"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            onload="document.querySelector('.loading').style.display='none'">
        </iframe>
    </div>
</body>
</html>
```

**使用方式**：
- 放在您的网站目录：`/dashboard.html`
- 访问：`https://yourwebsite.com/dashboard.html`

---

### 方案 B：嵌入到现有页面的某个区域

**适用场景**：个人博客文章、作品集页面的一部分

```html
<!-- 在您的网页中添加以下代码 -->

<section class="portfolio-item">
    <h2>📊 Superstore Sales Dashboard</h2>
    <p>基于 Streamlit + Plotly 构建的交互式销售数据可视化分析平台</p>
    
    <!-- Dashboard 嵌入区域 -->
    <div style="width: 100%; height: 800px; margin: 30px 0; position: relative; background: #F5F7FA; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
        <iframe 
            src="https://superstore-sales-dashboard.streamlit.app/?embed=true"
            style="width: 100%; height: 100%; border: none;"
            title="Sales Dashboard"
            loading="lazy">
        </iframe>
    </div>
    
    <!-- Dashboard 说明 -->
    <div style="margin-top: 20px; padding: 20px; background: #E3F2FD; border-left: 4px solid #1565C0; border-radius: 5px;">
        <h3 style="color: #1565C0; margin-bottom: 10px;">💡 项目亮点</h3>
        <ul style="color: #37474F; line-height: 1.8;">
            <li>📈 7+ 种交互式图表（Plotly）</li>
            <li>🗺️ 美国地理分布热力图</li>
            <li>🎨 PyGWalker 拖拽式自定义分析</li>
            <li>🌐 三语言支持（English / 繁體中文 / 简体中文）</li>
            <li>📱 响应式设计，完美适配移动端</li>
        </ul>
    </div>
    
    <!-- 查看完整版链接 -->
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

### 方案 C：WordPress 网站嵌入

**步骤**：

1. 登录 WordPress 后台
2. 编辑页面/文章
3. 切换到 **"自定义 HTML"** 块
4. 粘贴以下代码：

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

### 方案 D：React / Next.js 网站嵌入

**组件代码**：

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
        .dashboard-wrapper {
          width: 100%;
          max-width: 1400px;
          margin: 0 auto;
          padding: 40px 20px;
        }
        
        .dashboard-wrapper h2 {
          font-size: 28px;
          color: #1565C0;
          margin-bottom: 20px;
          text-align: center;
        }
        
        .dashboard-iframe-container {
          position: relative;
          width: 100%;
          height: 800px;
          border-radius: 10px;
          overflow: hidden;
          box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        
        iframe {
          width: 100%;
          height: 100%;
          border: none;
        }
        
        @media (max-width: 768px) {
          .dashboard-iframe-container {
            height: 600px;
          }
        }
      `}</style>
    </div>
  );
};

export default DashboardEmbed;
```

---

## 高级优化

### 1. **隐藏 Streamlit 菜单和水印**

在 `superstore_dashboard.py` 中添加（已有可跳过）：

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

---

### 2. **URL 参数控制**

您可以在 iFrame 的 `src` 中添加参数：

```html
<!-- 嵌入模式（隐藏顶部工具栏） -->
src="https://your-dashboard.streamlit.app/?embed=true"

<!-- 禁用滚动 -->
src="https://your-dashboard.streamlit.app/?embed=true&embed_options=disable_scrolling"

<!-- 自定义主题 -->
src="https://your-dashboard.streamlit.app/?embed=true&theme=light"
```

---

## 常见问题

### Q1: iFrame 显示空白？

**可能原因**：
- Dashboard 还在部署中（Streamlit Cloud 首次部署需 2-3 分钟）
- URL 地址错误
- 浏览器阻止了跨域 iFrame

**解决方案**：
```bash
# 1. 直接访问 Dashboard URL 确认是否正常
https://your-dashboard.streamlit.app

# 2. 检查浏览器控制台（F12）是否有错误
# 3. 确保 URL 包含 ?embed=true 参数
```

---

### Q2: iFrame 高度不合适？

**解决方案**：

```html
<!-- 固定高度 -->
<iframe style="height: 800px;"></iframe>

<!-- 视口高度 -->
<iframe style="height: 90vh;"></iframe>

<!-- 动态高度（推荐） -->
<iframe id="dashboard-iframe" style="min-height: 800px;"></iframe>
```

---

## 🎯 下一步行动清单

### ✅ 立即执行（5 分钟）
- [ ] 在 GitHub 创建仓库并推送代码
- [ ] 在 Streamlit Cloud 部署 Dashboard
- [ ] 获得公开链接并测试访问

### ✅ 嵌入网站（10 分钟）
- [ ] 选择嵌入方案（独立页面 / 页面区域）
- [ ] 复制对应的 HTML 代码
- [ ] 替换 Dashboard URL
- [ ] 测试移动端和桌面端显示

### ✅ 优化提升（可选）
- [ ] 添加项目说明和技术亮点
- [ ] 添加"在新窗口打开"按钮
- [ ] 配置自定义域名（如需要）
- [ ] 添加访问统计（Google Analytics）

---

## 🚀 快速开始命令

```bash
# 1. 推送代码到 GitHub
cd /Users/gaozikai/Documents/cursor来做数据可视化/AI员工关系/superstore_dashboard
git init
git add .
git commit -m "Add Superstore Dashboard"
git remote add origin https://github.com/YOUR_USERNAME/superstore-dashboard.git
git push -u origin main

# 2. 访问 Streamlit Cloud 部署
open https://share.streamlit.io/

# 3. 部署完成后，使用 iFrame 嵌入
# 复制本文档中的 HTML 代码，替换 Dashboard URL 即可！
```

---

<div align="center">

**🎉 祝您嵌入成功！**

*让您的 Dashboard 在个人网站上闪耀*

</div>

