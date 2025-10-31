#!/bin/bash
echo "🔍 检查 GitHub Pages 状态..."
echo ""
echo "1️⃣  查看部署历史:"
echo "   https://github.com/JohnsonGAOK/superstore-sales-dashboard/actions"
echo ""
echo "2️⃣  检查 Pages 设置:"
echo "   https://github.com/JohnsonGAOK/superstore-sales-dashboard/settings/pages"
echo ""
echo "3️⃣  测试访问 (将在新窗口打开):"
echo "   https://johnsongaok.github.io/superstore-sales-dashboard/"
echo ""
echo "⏱️  GitHub Pages 通常需要 1-5 分钟部署完成"
echo "   如果超过 5 分钟还在加载，可能是网络问题"
echo ""

# 打开浏览器查看
open "https://github.com/JohnsonGAOK/superstore-sales-dashboard/actions"

echo "按任意键打开 Dashboard 页面..."
read -n 1
open "https://johnsongaok.github.io/superstore-sales-dashboard/"
