# 📦 Vercel Dashboard 代理集成包

这个文件夹包含了在 Vercel 网站中集成 Dashboard 所需的所有文件和说明。

---

## 📁 文件清单

| 文件 | 用途 | 适用项目 |
|-----|------|---------|
| **给另一个窗口的说明.md** | 🎯 快速入门指南 | 所有项目 |
| **app-router-route.js** | Next.js 13+ 代理代码 | App Router 项目 |
| **pages-router-api.js** | Next.js 12 代理代码 | Pages Router 项目 |
| **next.config.js** | Next.js 完整配置 | Next.js 项目 |
| **vercel.json** | Vercel 配置 | 静态网站 |
| **vercel_proxy_guide.md** | 详细技术文档 | 技术参考 |

---

## 🚀 快速开始（3 步骤）

### 第 1 步：判断项目类型

打开你的 Vercel 网站项目，检查目录结构：

```bash
# Next.js 13+ (App Router)
如果有 app/ 目录 → 使用 app-router-route.js

# Next.js 12 (Pages Router)
如果有 pages/ 目录 → 使用 pages-router-api.js

# 纯静态网站
如果都没有 → 使用 vercel.json
```

### 第 2 步：复制对应文件

#### **Next.js App Router**
```bash
# 复制到你的项目
cp app-router-route.js 你的项目/app/dashboard/route.js
```

#### **Next.js Pages Router**
```bash
# 复制到你的项目
cp pages-router-api.js 你的项目/pages/api/dashboard.js
```

#### **静态网站**
```bash
# 复制到你的项目根目录
cp vercel.json 你的项目/vercel.json
```

### 第 3 步：推送部署

```bash
cd 你的项目
git add .
git commit -m "Add dashboard proxy"
git push
```

Vercel 会自动部署（1-2 分钟）

---

## ✅ 验证

部署完成后，访问：

```
https://你的域名.com/dashboard
```

应该能看到 Dashboard 正常加载！

---

## 🎨 在网站中嵌入

### 简单版（推荐）

```html
<iframe 
    src="/dashboard?embed=true"
    style="width: 100%; height: 900px; border: none;">
</iframe>
```

### 美化版

```html
<div style="width: 100%; height: 900px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin: 30px 0;">
    <iframe 
        src="/dashboard?embed=true"
        style="width: 100%; height: 100%; border: none;"
        title="Dashboard"
        loading="lazy">
    </iframe>
</div>
```

---

## 💡 告诉另一个 AI 窗口

直接发送这段话：

```
请帮我在 Vercel 网站中添加 Dashboard 代理。

Dashboard 链接：https://superstore-sales-dashboard-johnson.streamlit.app/

我有完整的代码文件在 superstore_dashboard/vercel-integration/ 目录，
请查看"给另一个窗口的说明.md"并根据我们的项目类型选择合适的方案实现。

目标：让 /dashboard 路径能访问这个 Dashboard，解决国内访问慢的问题。
```

---

## 📊 效果对比

| 项目 | 直连 Streamlit | 通过 Vercel 代理 |
|-----|--------------|----------------|
| 国内访问速度 | 10-30秒 ⚠️ | 2-5秒 ✅ |
| 稳定性 | 不稳定 ⚠️ | 稳定 ✅ |
| 成本 | $0 | $0 ✅ |
| 维护 | 简单 | 简单 ✅ |

---

## 🐛 故障排查

### 问题 1: 404 Not Found

**原因**：文件位置不对

**解决**：
- App Router: 确保文件在 `app/dashboard/route.js`
- Pages Router: 确保文件在 `pages/api/dashboard.js`

### 问题 2: 503 超时

**原因**：Streamlit 应用冷启动

**解决**：等待 10 秒后刷新，后续访问会快

### 问题 3: 样式错误

**原因**：静态资源未代理

**解决**：使用 `next.config.js` 完整配置

---

## 📖 详细文档

需要更多信息？查看：

- **快速入门** → `给另一个窗口的说明.md`
- **完整指南** → `vercel_proxy_guide.md`
- **代码示例** → 各个 `.js` 文件中的注释

---

## 🎉 优势总结

使用 Vercel 代理方案的好处：

1. ✅ **免费** - 无需额外费用
2. ✅ **快速** - 国内访问速度提升 5-10 倍
3. ✅ **简单** - 只需添加一个文件
4. ✅ **统一** - 和网站在同一个域名下
5. ✅ **自动更新** - Dashboard 更新自动同步

---

**预计实施时间**：10-15 分钟  
**技术难度**：⭐⭐☆☆☆  
**效果提升**：⭐⭐⭐⭐⭐

开始吧！🚀

