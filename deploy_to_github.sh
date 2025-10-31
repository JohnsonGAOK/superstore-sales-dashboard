#!/bin/bash

# ===================================
# Superstore Dashboard - GitHub 部署脚本
# ===================================
# 
# 功能：
# 1. 检查必要文件
# 2. 初始化 Git 仓库
# 3. 添加 .gitignore
# 4. 推送到 GitHub
# 5. 提供 Streamlit Cloud 部署链接
#
# 使用方法：
# chmod +x deploy_to_github.sh
# ./deploy_to_github.sh
# ===================================

set -e  # 遇到错误立即退出

echo "🚀 Superstore Dashboard - GitHub 部署助手"
echo "=========================================="
echo ""

# 检查是否在正确的目录
if [ ! -f "superstore_dashboard.py" ]; then
    echo "❌ 错误：未找到 superstore_dashboard.py"
    echo "请确保在项目根目录下运行此脚本"
    exit 1
fi

echo "✅ 找到 Dashboard 主文件"

# 检查必要文件
required_files=("requirements.txt" "README.md" "superstore_data.csv")
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "⚠️  警告：未找到 $file"
    else
        echo "✅ 找到 $file"
    fi
done

echo ""
echo "=========================================="
echo "第一步：配置 Git 仓库"
echo "=========================================="

# 检查是否已经初始化 Git
if [ -d ".git" ]; then
    echo "✅ Git 仓库已存在"
else
    echo "📦 初始化 Git 仓库..."
    git init
    echo "✅ Git 仓库初始化完成"
fi

# 创建或更新 .gitignore
echo ""
echo "📝 创建 .gitignore 文件..."
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Streamlit
.streamlit/secrets.toml

# PyGWalker
gw_config.json

# macOS
.DS_Store

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
*.log

# 临时文件
*.tmp
EOF

echo "✅ .gitignore 文件创建完成"

# 配置 Git 用户信息（如果未配置）
if ! git config user.name > /dev/null 2>&1; then
    echo ""
    echo "请配置 Git 用户信息："
    read -p "输入您的名字: " git_name
    read -p "输入您的邮箱: " git_email
    git config user.name "$git_name"
    git config user.email "$git_email"
    echo "✅ Git 用户信息配置完成"
fi

echo ""
echo "=========================================="
echo "第二步：准备提交代码"
echo "=========================================="

# 添加所有文件
echo "📦 添加文件到 Git..."
git add .

# 显示将要提交的文件
echo ""
echo "将要提交的文件："
git status --short

# 提交
echo ""
read -p "是否继续提交？(y/n): " confirm
if [ "$confirm" != "y" ]; then
    echo "❌ 操作已取消"
    exit 0
fi

git commit -m "Initial commit: Superstore Sales Dashboard

- 添加主 Dashboard 应用 (superstore_dashboard.py)
- 添加数据文件 (superstore_data.csv)
- 添加依赖清单 (requirements.txt)
- 添加项目文档 (README.md, DEPLOYMENT_GUIDE.md)
- 添加嵌入示例 (embed_examples/)
- 支持三语言切换 (English/繁體中文/简体中文)
- 集成 Plotly + PyGWalker + 高级分析功能"

echo "✅ 代码提交完成"

echo ""
echo "=========================================="
echo "第三步：连接 GitHub 远程仓库"
echo "=========================================="
echo ""
echo "请在 GitHub 上创建一个新仓库："
echo "1. 访问: https://github.com/new"
echo "2. 仓库名建议: superstore-sales-dashboard"
echo "3. 设置为 Public（Streamlit Cloud 需要）"
echo "4. ⚠️  不要初始化 README 和 .gitignore"
echo ""
read -p "已创建仓库？输入您的 GitHub 用户名: " github_username
read -p "输入仓库名称 (默认: superstore-sales-dashboard): " repo_name
repo_name=${repo_name:-superstore-sales-dashboard}

# 设置远程仓库
remote_url="https://github.com/$github_username/$repo_name.git"
echo ""
echo "📡 连接远程仓库: $remote_url"

# 检查是否已有 remote
if git remote | grep -q "^origin$"; then
    echo "⚠️  已存在 origin，将更新为新地址"
    git remote set-url origin "$remote_url"
else
    git remote add origin "$remote_url"
fi

echo "✅ 远程仓库连接成功"

echo ""
echo "=========================================="
echo "第四步：推送代码到 GitHub"
echo "=========================================="

echo "📤 推送代码..."
git branch -M main
if git push -u origin main; then
    echo "✅ 代码推送成功！"
else
    echo "❌ 推送失败"
    echo ""
    echo "可能的原因："
    echo "1. 网络连接问题"
    echo "2. GitHub 认证失败（需要配置 Personal Access Token）"
    echo "3. 仓库不存在"
    echo ""
    echo "请尝试手动推送："
    echo "git push -u origin main"
    exit 1
fi

echo ""
echo "=========================================="
echo "🎉 部署准备完成！"
echo "=========================================="
echo ""
echo "📋 下一步操作："
echo ""
echo "1️⃣  访问 Streamlit Cloud 部署页面:"
echo "   🔗 https://share.streamlit.io/"
echo ""
echo "2️⃣  使用 GitHub 账号登录"
echo ""
echo "3️⃣  点击 'New app'，配置如下:"
echo "   - Repository: $github_username/$repo_name"
echo "   - Branch: main"
echo "   - Main file path: superstore_dashboard.py"
echo "   - App URL: $repo_name"
echo ""
echo "4️⃣  点击 'Deploy!' 开始部署 (约 2-3 分钟)"
echo ""
echo "5️⃣  部署完成后，您将获得链接:"
echo "   🌐 https://$repo_name.streamlit.app"
echo ""
echo "6️⃣  使用 iFrame 嵌入到您的网站:"
echo "   📄 参考: embed_examples/fullscreen.html"
echo "   🔗 src=\"https://$repo_name.streamlit.app/?embed=true\""
echo ""
echo "=========================================="
echo "📚 参考文档:"
echo "   - EMBED_GUIDE.md (嵌入指南)"
echo "   - DEPLOYMENT_GUIDE.md (部署详解)"
echo "   - embed_examples/ (HTML 示例)"
echo "=========================================="
echo ""
echo "🎊 祝您部署顺利！"
echo ""

