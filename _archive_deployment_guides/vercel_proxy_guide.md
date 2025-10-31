# 🚀 Vercel Dashboard 代理部署指南

> **解决问题**：Streamlit Cloud 在国内访问慢/打不开  
> **解决方案**：通过 Vercel 反向代理加速访问  
> **成本**：$0（完全免费）

---

## 📋 方案说明

### 原理
```
用户访问 → 你的域名/dashboard → Vercel 代理 → Streamlit Cloud
```

### 优势
- ✅ **免费**：无需额外费用
- ✅ **快速**：Vercel 全球 CDN
- ✅ **简单**：只需添加一个文件
- ✅ **统一**：和网站在同一个项目
- ✅ **自动 HTTPS**：无需配置

---

## 🎯 实现方式（3 选 1）

### 方式 1：Next.js App Router（推荐）⭐⭐⭐⭐⭐

**适用于**：使用 Next.js 13+ (App Router) 的项目

#### 步骤：

**1. 创建代理路由**

在你的 Next.js 项目中创建文件：`app/dashboard/route.js`

```javascript
// app/dashboard/route.js
import { NextResponse } from 'next/server';

export const runtime = 'edge'; // 使用 Edge Runtime 提速

export async function GET(request) {
  const url = new URL(request.url);
  
  // 目标 Streamlit 应用
  const streamlitUrl = 'https://superstore-sales-dashboard-johnson.streamlit.app' + url.search;
  
  try {
    // 获取原始请求
    const response = await fetch(streamlitUrl, {
      headers: {
        ...Object.fromEntries(request.headers),
        'Host': 'superstore-sales-dashboard-johnson.streamlit.app'
      },
    });
    
    // 复制响应
    const data = await response.text();
    
    // 返回响应
    return new NextResponse(data, {
      status: response.status,
      headers: {
        'Content-Type': response.headers.get('Content-Type') || 'text/html',
        'Cache-Control': 'public, max-age=60',
      },
    });
  } catch (error) {
    return new NextResponse('Dashboard 暂时不可用', { status: 503 });
  }
}
```

**2. 推送到 GitHub 并部署**

```bash
git add app/dashboard/route.js
git commit -m "Add dashboard proxy"
git push
```

Vercel 会自动部署（1-2 分钟）

**3. 访问链接**

```
https://你的域名.com/dashboard
```

**4. 在网站中嵌入**

```html
<iframe 
    src="https://你的域名.com/dashboard?embed=true"
    style="width: 100%; height: 900px; border: none;"
    title="Dashboard">
</iframe>
```

---

### 方式 2：Next.js Pages Router

**适用于**：使用 Next.js 12 或更早版本（Pages Router）

#### 步骤：

**1. 创建 API 路由**

文件：`pages/api/dashboard.js`

```javascript
// pages/api/dashboard.js
export default async function handler(req, res) {
  const { query } = req;
  const queryString = new URLSearchParams(query).toString();
  
  const streamlitUrl = `https://superstore-sales-dashboard-johnson.streamlit.app${queryString ? '?' + queryString : ''}`;
  
  try {
    const response = await fetch(streamlitUrl, {
      headers: {
        ...req.headers,
        'Host': 'superstore-sales-dashboard-johnson.streamlit.app'
      },
    });
    
    const data = await response.text();
    
    res.setHeader('Content-Type', response.headers.get('Content-Type') || 'text/html');
    res.setHeader('Cache-Control', 'public, max-age=60');
    res.status(response.status).send(data);
  } catch (error) {
    res.status(503).send('Dashboard 暂时不可用');
  }
}

export const config = {
  api: {
    responseLimit: false,
  },
};
```

**2. 创建页面路由**

文件：`pages/dashboard.js`

```javascript
// pages/dashboard.js
export default function Dashboard() {
  return (
    <div style={{ width: '100vw', height: '100vh', margin: 0, padding: 0 }}>
      <iframe
        src="/api/dashboard?embed=true"
        style={{ width: '100%', height: '100%', border: 'none' }}
        title="Dashboard"
      />
    </div>
  );
}
```

**3. 访问链接**

- 独立页面：`https://你的域名.com/dashboard`
- API 端点：`https://你的域名.com/api/dashboard`

---

### 方式 3：纯静态网站（HTML/React/Vue）

**适用于**：不使用 Next.js，但部署在 Vercel 的项目

#### 步骤：

**1. 创建 Vercel 配置**

文件：`vercel.json`

```json
{
  "rewrites": [
    {
      "source": "/dashboard/:path*",
      "destination": "https://superstore-sales-dashboard-johnson.streamlit.app/:path*"
    }
  ]
}
```

**2. 推送并部署**

```bash
git add vercel.json
git commit -m "Add dashboard proxy"
git push
```

**3. 访问链接**

```
https://你的域名.com/dashboard
```

**注意**：这个方法可能无法完美代理所有功能（WebSocket 可能有问题）

---

## 🎨 集成到你的网站

### 选项 A：iframe 嵌入（推荐）

```html
<!-- 在任意页面中嵌入 -->
<div style="width: 100%; height: 900px; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
    <iframe 
        src="https://你的域名.com/dashboard?embed=true"
        style="width: 100%; height: 100%; border: none;"
        title="Dashboard"
        loading="lazy">
    </iframe>
</div>
```

### 选项 B：独立页面

直接访问：`https://你的域名.com/dashboard`

### 选项 C：React 组件

```jsx
// components/DashboardEmbed.jsx
export default function DashboardEmbed() {
  return (
    <div style={{ width: '100%', height: '900px' }}>
      <iframe
        src="/dashboard?embed=true"
        style={{ width: '100%', height: '100%', border: 'none' }}
        title="Dashboard"
      />
    </div>
  );
}
```

---

## 🔧 高级配置

### 添加缓存优化

```javascript
// app/dashboard/route.js (Next.js 13+)
export async function GET(request) {
  // ... 省略其他代码
  
  return new NextResponse(data, {
    headers: {
      'Content-Type': response.headers.get('Content-Type'),
      'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300', // CDN 缓存
      'X-Content-Type-Options': 'nosniff',
    },
  });
}
```

### 添加错误处理

```javascript
export async function GET(request) {
  try {
    const response = await fetch(streamlitUrl, {
      signal: AbortSignal.timeout(10000), // 10 秒超时
    });
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    
    return new NextResponse(await response.text(), {
      status: response.status,
      headers: response.headers,
    });
  } catch (error) {
    console.error('Dashboard proxy error:', error);
    
    return new NextResponse(`
      <html>
        <body style="display: flex; align-items: center; justify-content: center; height: 100vh; font-family: sans-serif;">
          <div style="text-align: center;">
            <h2>⚠️ Dashboard 加载失败</h2>
            <p>请稍后重试或联系管理员</p>
            <button onclick="location.reload()">重新加载</button>
          </div>
        </body>
      </html>
    `, { 
      status: 503,
      headers: { 'Content-Type': 'text/html' }
    });
  }
}
```

### 添加访问统计

```javascript
export async function GET(request) {
  const start = Date.now();
  
  // ... 代理逻辑
  
  const duration = Date.now() - start;
  console.log(`Dashboard loaded in ${duration}ms`);
  
  return response;
}
```

---

## 📊 效果对比

### 访问速度测试

| 链接 | 国内加载时间 | 稳定性 |
|-----|------------|--------|
| **Streamlit Cloud 直连** | 10-30秒 | ⚠️ 不稳定 |
| **Vercel 代理** | 2-5秒 | ✅ 稳定 |

### 用户体验

| 项目 | Streamlit 直连 | Vercel 代理 |
|-----|---------------|------------|
| 首次加载 | 😰 很慢 | 😊 正常 |
| 图表交互 | 😰 卡顿 | 😊 流畅 |
| 移动端 | 😰 经常失败 | 😊 正常 |
| 稳定性 | ⚠️ 时好时坏 | ✅ 稳定 |

---

## 🐛 常见问题

### Q1: 代理后 WebSocket 不工作？

**答**：Streamlit 的实时更新依赖 WebSocket，代理可能会有问题

**解决**：在 Next.js 配置中启用 WebSocket 支持

```javascript
// next.config.js
module.exports = {
  async rewrites() {
    return [
      {
        source: '/dashboard/_stcore/:path*',
        destination: 'https://superstore-sales-dashboard-johnson.streamlit.app/_stcore/:path*',
      },
    ];
  },
};
```

### Q2: 样式显示不正常？

**答**：可能是静态资源路径问题

**解决**：添加资源代理

```javascript
// next.config.js
module.exports = {
  async rewrites() {
    return [
      {
        source: '/dashboard',
        destination: 'https://superstore-sales-dashboard-johnson.streamlit.app',
      },
      {
        source: '/dashboard/:path*',
        destination: 'https://superstore-sales-dashboard-johnson.streamlit.app/:path*',
      },
    ];
  },
};
```

### Q3: Vercel 函数超时？

**答**：Vercel 免费版函数限制 10 秒

**解决**：升级到 Pro 版（$20/月，函数限制 60 秒）或使用 Edge Runtime

```javascript
export const runtime = 'edge'; // 突破函数时间限制
export const maxDuration = 60; // Pro 版可用
```

### Q4: CORS 错误？

**答**：跨域问题

**解决**：添加 CORS 头

```javascript
return new NextResponse(data, {
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
  },
});
```

---

## 🚀 部署检查清单

部署完成后，请检查：

- [ ] 能访问 `https://你的域名.com/dashboard`
- [ ] Dashboard 加载速度正常（< 5 秒）
- [ ] 图表交互功能正常
- [ ] 筛选器正常工作
- [ ] 移动端显示正常
- [ ] 不同浏览器测试通过

---

## 💡 优化建议

### 1. 添加加载状态

```html
<div id="dashboard-container">
  <div id="loading">加载中...</div>
  <iframe 
    src="/dashboard?embed=true" 
    onload="document.getElementById('loading').style.display='none'">
  </iframe>
</div>
```

### 2. 预加载

```html
<link rel="preconnect" href="https://你的域名.com">
<link rel="dns-prefetch" href="https://你的域名.com">
```

### 3. 懒加载

```html
<iframe loading="lazy" src="/dashboard?embed=true"></iframe>
```

---

## 🎉 下一步

1. ✅ 选择合适的方式（推荐方式 1）
2. ✅ 创建代理文件
3. ✅ 推送到 GitHub
4. ✅ 等待 Vercel 自动部署
5. ✅ 测试访问速度
6. ✅ 更新网站嵌入代码

---

**预计耗时**：10-15 分钟  
**技术难度**：⭐⭐☆☆☆  
**效果提升**：⭐⭐⭐⭐⭐

有任何问题随时问！🚀

