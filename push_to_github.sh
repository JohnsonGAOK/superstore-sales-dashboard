#!/bin/bash

echo "================================================"
echo "🚀 推送到 GitHub"
echo "================================================"
echo ""

# 检查是否有 token
if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ 错误：未设置 GITHUB_TOKEN 环境变量"
    echo ""
    echo "请先创建 GitHub Personal Access Token："
    echo "1. 访问：https://github.com/settings/tokens/new"
    echo "2. 勾选 'repo' 权限"
    echo "3. 生成 token 后，运行："
    echo ""
    echo "   export GITHUB_TOKEN=你的token"
    echo "   ./push_to_github.sh"
    echo ""
    exit 1
fi

echo "✅ 检测到 GITHUB_TOKEN"
echo "📦 准备推送..."
echo ""

# 设置远程 URL（带 token）
git remote set-url origin https://${GITHUB_TOKEN}@github.com/JohnsonGAOK/superstore-sales-dashboard.git

# 推送
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "================================================"
    echo "✅ 推送成功！"
    echo "================================================"
    echo ""
    echo "🌐 访问你的仓库："
    echo "   https://github.com/JohnsonGAOK/superstore-sales-dashboard"
    echo ""
else
    echo ""
    echo "================================================"
    echo "❌ 推送失败"
    echo "================================================"
    echo ""
    echo "可能的原因："
    echo "1. Token 权限不足"
    echo "2. 仓库不存在"
    echo "3. 网络问题"
    echo ""
fi

# 恢复原始 URL（不带 token，安全）
git remote set-url origin https://github.com/JohnsonGAOK/superstore-sales-dashboard.git

