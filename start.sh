#!/bin/bash

# 进入项目目录
cd "$(dirname "$0")"

# 激活虚拟环境
source venv/bin/activate

# 启动 Streamlit
echo "🚀 正在启动 Superstore Dashboard..."
echo "📊 访问地址: http://localhost:8501"
echo "⏹️  按 Ctrl+C 停止服务器"
echo ""

streamlit run superstore_dashboard.py --server.port 8501
