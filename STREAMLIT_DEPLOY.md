# 🚀 Streamlit Cloud 部署指南

## ✅ GitHub 已就绪
代码仓库: https://github.com/JohnsonGAOK/superstore-sales-dashboard
分支: main
主文件: superstore_dashboard.py

---

## 📝 部署步骤（5分钟完成）

### 步骤 1️⃣: 访问 Streamlit Cloud
👉 https://share.streamlit.io/

### 步骤 2️⃣: 登录
- 点击右上角 **"Sign in"** 或 **"Sign up"**
- 选择 **"Continue with GitHub"**
- 使用你的 GitHub 账号（JohnsonGAOK）登录
- 授权 Streamlit 访问你的仓库

### 步骤 3️⃣: 创建新应用
- 点击 **"New app"** 或 **"Create app"**

### 步骤 4️⃣: 填写部署信息

```
Repository: JohnsonGAOK/superstore-sales-dashboard
Branch: main
Main file path: superstore_dashboard.py
App URL (可选): superstore-dashboard (或自定义)
```

### 步骤 5️⃣: 点击 "Deploy!"
- Streamlit 会自动检测 `requirements.txt`
- 安装依赖包（pandas, streamlit, plotly）
- 启动你的应用

### 步骤 6️⃣: 等待部署完成
⏱️ 通常需要 **2-5 分钟**

你会看到：
```
🔨 Installing dependencies...
✅ Dependencies installed
🚀 Starting app...
✅ App is live!
```

---

## 🎉 部署完成后

你会获得一个永久链接，格式类似：
```
https://johnsongaok-superstore-sales-dashboard-xxxxx.streamlit.app
```

这个链接可以：
- ✅ 直接分享给任何人
- ✅ 永久在线（只要仓库存在）
- ✅ 自动更新（推送代码后自动重新部署）

---

## 🔄 后续更新流程

1. **修改本地代码**
   ```bash
   # 编辑 superstore_dashboard.py
   ```

2. **测试**
   ```bash
   ./start.sh
   ```

3. **推送到 GitHub**
   ```bash
   git add .
   git commit -m "更新描述"
   git push origin main
   ```

4. **自动部署**
   - Streamlit Cloud 会自动检测更新
   - 1-2 分钟后自动重新部署
   - 无需手动操作！

---

## 📊 查看应用状态

登录后在 Streamlit Cloud 控制台可以：
- 查看部署日志
- 查看访问统计
- 重启应用
- 查看错误信息

---

## ❓ 常见问题

### Q: 部署失败怎么办？
A: 检查：
1. `requirements.txt` 是否正确
2. `superstore_data.csv` 是否存在
3. 查看部署日志（Manage app → Logs）

### Q: 如何更新应用？
A: 直接推送代码到 GitHub，Streamlit 自动更新

### Q: 可以私有部署吗？
A: 免费版必须公开，付费版支持私有

### Q: 访问速度慢怎么办？
A: Streamlit Cloud 服务器在国外，国内访问可能较慢

---

## 🎯 快速链接

- Streamlit Cloud: https://share.streamlit.io/
- GitHub 仓库: https://github.com/JohnsonGAOK/superstore-sales-dashboard
- 本地运行: `./start.sh`

---

创建时间: 2025-10-31
