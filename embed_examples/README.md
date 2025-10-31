# 📦 Dashboard 嵌入示例文件

本文件夹包含将 Superstore Dashboard 嵌入个人网站的 HTML 示例代码。

---

## 📁 文件说明

### 1. `fullscreen.html` - 全屏独立页面

**适用场景**：
- 作为网站的独立页面（如 `/dashboard` 路由）
- 作品集项目展示
- 完全沉浸式数据分析体验

**特点**：
- ✅ 顶部导航栏（可自定义）
- ✅ 全屏 iFrame 嵌入
- ✅ 加载动画和超时提示
- ✅ 响应式设计

**使用方式**：
```bash
# 1. 将文件放到网站目录
cp fullscreen.html /path/to/your/website/dashboard.html

# 2. 修改 iFrame 的 src 地址
# 开发环境（本地）：src="http://localhost:8501/?embed=true"
# 生产环境（Streamlit Cloud）：src="https://your-app.streamlit.app/?embed=true"

# 3. 访问页面
https://yourwebsite.com/dashboard.html
```

---

### 2. `section_embed.html` - 页面区域嵌入

**适用场景**：
- 个人博客文章
- 作品集页面的一部分
- 项目介绍页面

**特点**：
- ✅ 完整的项目介绍内容
- ✅ 技术栈展示
- ✅ 项目亮点和技术实现说明
- ✅ Dashboard 嵌入区域（高度 800px）
- ✅ "在新窗口打开"按钮

**使用方式**：
```bash
# 1. 复制 HTML 代码段到您的网页
# 2. 或直接使用完整页面

# 3. 修改 iFrame src 地址
# 4. 根据需要调整内容和样式
```

---

## 🔧 配置步骤

### Step 1: 选择部署方式

#### 选项 A：本地开发（测试用）
```bash
# 确保 Dashboard 正在运行
cd /Users/gaozikai/Documents/cursor来做数据可视化/AI员工关系/superstore_dashboard
./start.sh

# iFrame src 地址
src="http://localhost:8501/?embed=true"
```

#### 选项 B：Streamlit Cloud（推荐生产环境）
```bash
# 1. 部署到 Streamlit Cloud（参考 EMBED_GUIDE.md）
# 2. 获得公开链接，如：
https://superstore-sales-dashboard.streamlit.app

# 3. iFrame src 地址
src="https://superstore-sales-dashboard.streamlit.app/?embed=true"
```

#### 选项 C：自托管服务器
```bash
# 部署到自己的服务器（参考 DEPLOYMENT_GUIDE.md）
# iFrame src 地址
src="https://dashboard.yourcompany.com/?embed=true"
```

---

### Step 2: 修改 HTML 文件

在任一示例文件中找到以下行：

```html
<iframe 
    src="http://localhost:8501/?embed=true"
    title="Superstore Sales Dashboard">
</iframe>
```

**替换为您的 Dashboard 地址**：

```html
<!-- 本地开发 -->
src="http://localhost:8501/?embed=true"

<!-- Streamlit Cloud -->
src="https://YOUR_APP_NAME.streamlit.app/?embed=true"

<!-- 自托管 -->
src="https://dashboard.yoursite.com/?embed=true"
```

---

### Step 3: 测试嵌入效果

```bash
# 1. 在浏览器中打开 HTML 文件
open fullscreen.html

# 2. 检查是否正常显示
# 3. 测试响应式布局（F12 -> 设备模拟器）
# 4. 测试交互功能（过滤器、图表缩放）
```

---

## 🎨 自定义样式

### 修改导航栏颜色（fullscreen.html）

```css
.header {
    /* 原始：紫色渐变 */
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    
    /* 蓝色主题 */
    background: linear-gradient(135deg, #1565C0 0%, #0D47A1 100%);
    
    /* 绿色主题 */
    background: linear-gradient(135deg, #43A047 0%, #2E7D32 100%);
    
    /* 橙色主题 */
    background: linear-gradient(135deg, #FB8C00 0%, #EF6C00 100%);
}
```

---

### 修改 Dashboard 高度（section_embed.html）

```css
.dashboard-embed {
    /* 默认高度 */
    height: 800px;
    
    /* 更高（适合内容多的 Dashboard） */
    height: 1000px;
    
    /* 视口高度（自适应屏幕） */
    height: 90vh;
}
```

---

### 修改容器宽度

```css
.container {
    /* 默认最大宽度 */
    max-width: 1200px;
    
    /* 更宽（适合大屏） */
    max-width: 1400px;
    
    /* 全宽 */
    max-width: 100%;
}
```

---

## 📱 响应式测试

### 移动端（< 768px）
- ✅ 导航栏堆叠显示
- ✅ Dashboard 高度调整为 600px
- ✅ 技术栈标签换行显示

### 平板（768px - 1024px）
- ✅ 2列布局
- ✅ Dashboard 保持 800px 高度

### 桌面（> 1024px）
- ✅ 完整宽度显示
- ✅ 所有功能正常

---

## 🔗 URL 参数说明

### `?embed=true`
**作用**：启用嵌入模式
- 隐藏 Streamlit 顶部菜单
- 优化 iFrame 显示效果
- **必须添加**，否则显示效果不佳

### `&theme=light` / `&theme=dark`
**作用**：指定主题（需 Streamlit 配置支持）
```html
src="https://your-app.streamlit.app/?embed=true&theme=light"
```

---

## ⚠️ 常见问题

### Q1: iFrame 显示"拒绝连接"

**原因**：浏览器阻止了跨域 iFrame（本地开发常见）

**解决**：
```bash
# 1. 确保 Dashboard 正在运行
curl http://localhost:8501

# 2. 检查 Streamlit 配置（.streamlit/config.toml）
[server]
enableCORS = false
enableXsrfProtection = false

# 3. 重启 Dashboard
```

---

### Q2: iFrame 显示空白

**可能原因**：
1. Dashboard URL 错误
2. Dashboard 未启动
3. 网络连接问题

**调试步骤**：
```bash
# 1. 在新标签页直接打开 Dashboard URL
# 2. 打开浏览器控制台（F12）查看错误
# 3. 检查 iFrame src 地址是否正确
```

---

### Q3: 移动端显示效果不好

**优化方案**：
```html
<!-- 添加响应式 CSS -->
<style>
@media (max-width: 768px) {
    .dashboard-embed {
        height: 600px;  /* 降低高度 */
    }
    
    iframe {
        min-width: 100%;
        overflow-x: auto;  /* 允许横向滚动 */
    }
}
</style>
```

---

## 🚀 快速开始

### 本地测试（1 分钟）

```bash
# 1. 启动 Dashboard
cd /Users/gaozikai/Documents/cursor来做数据可视化/AI员工关系/superstore_dashboard
./start.sh

# 2. 打开示例文件
open embed_examples/fullscreen.html

# 3. 在浏览器中查看效果
```

---

### 生产部署（5 分钟）

```bash
# 1. 部署到 Streamlit Cloud（参考 EMBED_GUIDE.md）
# 2. 获得公开链接
# 3. 修改 HTML 中的 iFrame src
# 4. 将 HTML 上传到您的网站服务器
# 5. 完成！
```

---

## 📞 需要帮助？

如有任何问题，请参考：
- **完整嵌入指南**：`EMBED_GUIDE.md`
- **部署文档**：`DEPLOYMENT_GUIDE.md`
- **项目说明**：`README.md`

---

<div align="center">

**✨ 祝您嵌入成功！**

*让数据可视化在您的网站上大放异彩*

</div>

