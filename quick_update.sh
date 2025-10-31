#!/bin/bash

# ========================================
# 快速更新到 Streamlit Cloud
# Quick Update to Streamlit Cloud
# ========================================

echo "🚀 准备更新到 Streamlit Cloud..."
echo ""

# 1. 检查是否有改动
if [[ -z $(git status -s) ]]; then
    echo "❌ 没有检测到任何改动"
    echo "   提示：请先修改代码后再运行此脚本"
    exit 1
fi

# 2. 显示改动文件
echo "📝 检测到以下改动："
git status -s
echo ""

# 3. 询问 commit 信息
read -p "📋 请输入更新说明 (例: 优化图表样式): " commit_message

if [[ -z "$commit_message" ]]; then
    commit_message="更新应用"
fi

# 4. 执行推送
echo ""
echo "⏳ 正在推送到 GitHub..."
git add .
git commit -m "$commit_message"
git push origin main

# 5. 完成提示
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 推送成功！"
    echo ""
    echo "📊 Streamlit Cloud 正在自动部署中..."
    echo "   预计等待时间: 1-3 分钟"
    echo ""
    echo "🔗 查看部署状态："
    echo "   https://share.streamlit.io/"
    echo ""
    echo "💡 提示："
    echo "   - 等待 1-3 分钟后刷新你的应用链接"
    echo "   - 可以在 Streamlit Cloud 控制台查看实时日志"
    echo "   - 如果部署失败，请检查日志并修复错误"
else
    echo ""
    echo "❌ 推送失败，请检查错误信息"
fi

