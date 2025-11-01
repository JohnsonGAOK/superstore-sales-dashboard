# 🛒 Superstore Sales Analysis Dashboard (EN/中文)

**Professional Retail Business Intelligence Platform for SMEs**

[![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.18.0-3F4F75.svg)](https://plotly.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

**Languages:** [**English**](#english-version) | [**中文**](#中文版)

---

## English Version

### 📊 Project Overview

This is a **professional-grade retail business data visualization dashboard** designed specifically for Small & Medium Enterprises (SMEs). It helps business owners and decision-makers quickly understand sales data, identify trends, and discover growth opportunities.

---

### ✨ Core Features

#### 📈 Real-time Data Analytics
- **4 Key Performance Indicators (KPIs)**: Total Sales, Order Count, Average Order Value, Unique Customers.
- **Dynamic Filters**: Filter data by Year, Product Category, Region, and Customer Segment.
- **AI-Powered Insights**: Automated generation of business insights.

#### 📊 10+ Professional Charts
1.  **Monthly Sales Trend** (Line Chart) - Identify seasonal patterns.
2.  **Sales by Product Category** (Bar Chart) - Find best-selling categories.
3.  **Sales Distribution by Region** (Pie Chart) - Understand market coverage.
4.  **Customer Segment Analysis** (Horizontal Bar Chart) - Identify core customer groups.
5.  **Top 10 Products** - Discover star products.
6.  **Top 10 Customers** - Identify VIP clients.
7.  **Shipping Mode Analysis** - Optimize logistics costs.
8.  **Sales Heatmap** (Month vs. Year) - Uncover temporal patterns.
9.  **Advanced Statistical Analysis** - Descriptive stats, correlations, outlier detection.
10. **PyGWalker Interactive Exploration** - Drag-and-drop custom chart creation.

#### 🌍 Tri-lingual Support
- **English** (Default)
- **Traditional Chinese** (繁體中文)
- **Simplified Chinese** (简体中文)

#### 📱 Responsive Design
- ✅ **Desktop** - Full experience
- ✅ **Tablet** - Optimized layout
- ✅ **Mobile** - Smooth interaction

#### 🎨 Professional Visual Design
- **Plotly Standard Palette** - Sophisticated light theme.
- **Gradient KPI Cards** - High visual impact.
- **Interactive Charts** - Hover details, zoom, export.
- **Data Table Export** - One-click CSV download.

---

### 🚀 Quick Start

#### 1️⃣ Requirements
- Python 3.8 or higher
- A virtual environment (recommended)

#### 2️⃣ Install Dependencies
```bash
# Navigate to the project directory
cd superstore_dashboard

# (Recommended) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### 3️⃣ Launch App

**Method 1: Using the start script (recommended)**
```bash
chmod +x start.sh  # Grant permission for the first run
./start.sh
```

**Method 2: Direct command**
```bash
streamlit run superstore_dashboard.py
```

**Method 3: Custom port**
```bash
streamlit run superstore_dashboard.py --server.port 8501
```

#### 4️⃣ Access the Dashboard
Once launched, open in your browser:
```
http://localhost:8501
```

---

### 📁 Project Structure
```
superstore_dashboard/
├── superstore_dashboard.py    # Main application file (900+ lines of professional code)
├── superstore_data.csv         # Sample dataset (9,800+ order records)
├── requirements.txt            # Python dependency list
├── README.md                   # Project documentation (this file)
├── start.sh                    # Quick start script
├── gw_config.json              # PyGWalker config (auto-generated)
└── DEPLOYMENT_GUIDE.md         # Deployment guide (optional)
```

---

### 🎯 Use Cases

#### Retail
- 📦 Product portfolio optimization
- 🛍️ Inventory management decisions
- 💰 Pricing strategy formulation

#### E-commerce
- 🌐 Cross-regional sales comparison
- 👥 Customer segmentation
- 📈 Marketing campaign ROI analysis

#### Wholesale
- 🏢 B2B customer value assessment
- 🚚 Logistics cost optimization
- 📊 Seasonal demand forecasting

#### Others
- **Consulting Firms**: Generate quick reports for clients.
- **Startups**: Showcase business growth to investors.
- **Finance Departments**: Visualize sales data for reporting.

---

### 🛠️ Tech Stack

| Tech          | Version | Purpose                  |
|---------------|---------|--------------------------|
| **Streamlit** | ≥1.31.0 | Web Application Framework|
| **Plotly**    | ≥5.18.0 | Interactive Charting Lib |
| **Pandas**    | ≥2.0.0  | Data Processing & Analysis|
| **NumPy**     | ≥1.24.0 | Numerical Computation    |
| **PyGWalker** | ≥0.4.9  | Drag-and-drop Exploration|
| **SciPy**     | ≥1.11.0 | Advanced Statistical Analysis |

---

### 📊 Data Description

#### Data Source
This dashboard uses the classic **Superstore Sales Dataset**, containing historical order data from a US-based retail chain.

#### Data Fields (18 columns)

| Field Name      | Type     | Description                                |
|-----------------|----------|--------------------------------------------|
| `Row ID`        | Integer  | Row identifier                             |
| `Order ID`      | String   | Unique order identifier                    |
| `Order Date`    | Date     | Date the order was placed                  |
| `Ship Date`     | Date     | Date the order was shipped                 |
| `Ship Mode`     | Category | Shipping method                            |
| `Customer ID`   | String   | Unique customer identifier                 |
| `Customer Name` | String   | Customer's name                            |
| `Segment`       | Category | Customer segment (Consumer/Corporate/Home Office)|
| `Country`       | String   | Country                                    |
| `City`          | String   | City                                       |
| `State`         | String   | State                                      |
| `Postal Code`   | Integer  | Postal code                                |
| `Region`        | Category | Region (East/West/Central/South)           |
| `Product ID`    | String   | Unique product identifier                  |
| `Category`      | Category | Product category (Furniture/Office Supplies/Technology)|
| `Sub-Category`  | Category | Product sub-category                       |
| `Product Name`  | String   | Product name                               |
| `Sales`         | Float    | Sales amount (in USD)                      |

#### Data Scale
- **Records**: 9,800+ orders
- **Time Range**: 2015-2018
- **Customers**: 793 unique customers
- **Products**: 1,850+ unique products

---

### 🎨 Customization & Extension

#### Replacing with Your Own Data
1. Prepare your CSV file, ensuring a similar field structure.
2. Replace `superstore_data.csv`.
3. Modify the field mappings in `superstore_dashboard.py` (lines 126-150).
4. Restart the application.

#### Adding New Charts
Reference the chart templates in the project to copy and modify within `superstore_dashboard.py`. All charts adhere to a unified style standard (see the `get_plotly_layout()` function).

#### Adjusting the Color Scheme
Modify the `COLORS` dictionary on lines 147-157 to apply your brand's colors.

---

### 🌐 Production Deployment

#### Method 1: Streamlit Community Cloud (Free)
1. Push the code to a GitHub repository.
2. Visit [share.streamlit.io](https://share.streamlit.io/).
3. Connect your GitHub repository and deploy.
4. Get a public link (e.g., `https://your-app.streamlit.app`).

#### Method 2: Embed in a Company Website (iFrame)
```html
<iframe
  src="https://your-app.streamlit.app/?embed=true"
  style="width: 100%; height: 800px; border: none;"
  title="Sales Dashboard">
</iframe>
```

#### Method 3: Self-Hosted Server (Docker)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "superstore_dashboard.py", "--server.port=8501"]
```

---

### 🐛 FAQ

**Q1: What if PyGWalker loads slowly?**
**A**: A 10-20 second initial load is normal. The configuration is saved to `gw_config.json`, making subsequent loads much faster.

**Q2: How to handle garbled Chinese characters?**
**A**: Ensure your CSV file is encoded in `UTF-8`. If your Excel export is in GBK, use a text editor to "Save As" with UTF-8 encoding.

**Q3: Why are charts not fully visible on mobile?**
**A**: Dashboard has a built-in responsive design. If issues persist, try viewing in landscape mode or on a desktop.

**Q4: How to add user authentication?**
**A**: You can use the `streamlit-authenticator` library to add simple user authentication.

**Q5: Can the data be updated in real-time?**
**A**: The current version uses a static CSV file. For real-time updates, can connect to a database (e.g., PostgreSQL/MySQL) and use `@st.cache_data(ttl=600)` to set a refresh interval (e.g., every 10 minutes).

---

### 📜 License

MIT License - You are free to use, modify, and distribute this project, but you must retain the original author's information.

---

### 🙏 Acknowledgments
- **Streamlit Team** - For the excellent web app framework.
- **Plotly** - For the powerful interactive charting library.
- **PyGWalker** - For the revolutionary drag-and-drop data exploration tool.
- **Kaggle Community** - For providing high-quality datasets.

---
<br>

## 中文版

### 📊 项目概述

这是一个**专业级零售业务数据可视化 Dashboard**。它能帮助用户快速理解销售数据、识别业务趋势、发现增长机会。

---

### ✨ 核心功能

#### 📈 实时数据分析
- **4个关键指标卡片 (KPI)**：总销售额、订单数、平均订单价值、独立客户数。
- **动态过滤器**：按年份、产品类别、地区、客户群体筛选数据。
- **AI 驱动的洞察**：自动生成业务洞察。

#### 📊 10+ 专业图表
1.  **月度销售趋势** (折线图) - 识别季节性模式。
2.  **产品类别销售对比** (柱状图) - 找出畅销品类。
3.  **地区销售分布** (饼图) - 了解市场覆盖。
4.  **客户群体分析** (横向柱状图) - 识别核心客户群。
5.  **Top 10 产品** - 发现明星产品。
6.  **Top 10 客户** - 识别 VIP 客户。
7.  **运送方式分析** - 优化物流成本。
8.  **销售热力图** (月份 vs 年份) - 发现时间规律。
9.  **高级统计分析** - 描述性统计、相关性、异常值检测。
10. **PyGWalker 交互式探索** - 拖拽式自定义图表。

#### 🌍 三语言支持
- **English** (默认)
- **繁體中文**
- **简体中文**

#### 📱 响应式设计
- ✅ **桌面端** - 完整体验
- ✅ **平板端** - 优化布局
- ✅ **移动端** - 流畅交互

#### 🎨 专业视觉设计
- **Plotly 标准配色** - 高级感浅色系。
- **渐变指标卡片** - 强视觉冲击力。
- **交互式图表** - 悬停提示、缩放、导出。
- **数据表格导出** - 一键下载 CSV。

---

### 🚀 快速开始

#### 1️⃣ 环境要求
- Python 3.8 或更高版本
- 虚拟环境 (推荐)

#### 2️⃣ 安装依赖
```bash
# 进入项目目录
cd superstore_dashboard

# (推荐) 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate  # macOS/Linux
# Windows 用户请使用: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

#### 3️⃣ 启动应用

**方法1: 使用启动脚本 (推荐)**
```bash
chmod +x start.sh  # 首次运行需要授权
./start.sh
```

**方法2: 直接使用命令**
```bash
streamlit run superstore_dashboard.py
```

**方法3: 自定义端口**
```bash
streamlit run superstore_dashboard.py --server.port 8501
```

#### 4️⃣ 访问 Dashboard
启动后，在浏览器中打开:
```
http://localhost:8501
```

---

### 📁 项目结构
```
superstore_dashboard/
├── superstore_dashboard.py    # 主应用文件 (900+ 行专业代码)
├── superstore_data.csv         # 示例数据集 (9,800+ 订单记录)
├── requirements.txt            # Python 依赖清单
├── README.md                   # 项目说明 (本文件)
├── start.sh                    # 快速启动脚本
├── gw_config.json              # PyGWalker 配置文件 (自动生成)
└── DEPLOYMENT_GUIDE.md         # 部署指南 (可选)
```

---

### 🎯 适用场景

#### 零售业
- 📦 产品组合优化
- 🛍️ 库存管理决策
- 💰 定价策略制定

#### 电商
- 🌐 跨区域销售对比
- 👥 客户群体细分
- 📈 营销活动 ROI 分析

#### 批发商
- 🏢 B2B 客户价值评估
- 🚚 物流成本优化
- 📊 季节性需求预测

#### 其他
- **咨询公司**: 为客户生成快速报告。
- **创业公司**: 向投资人展示业务增长。
- **财务部门**: 用于销售数据可视化汇报。

---

### 🛠️ 技术栈

| 技术        | 版本    | 用途                 |
|-------------|---------|----------------------|
| **Streamlit** | ≥1.31.0 | Web 应用框架         |
| **Plotly**    | ≥5.18.0 | 交互式图表库         |
| **Pandas**    | ≥2.0.0  | 数据处理与分析       |
| **NumPy**     | ≥1.24.0 | 数值计算             |
| **PyGWalker** | ≥0.4.9  | 拖拽式数据探索       |
| **SciPy**     | ≥1.11.0 | 高级统计分析         |

---

### 📊 数据说明

#### 数据来源
本 Dashboard 使用经典的 **Superstore 销售数据集**，包含一家美国零售连锁店的历史订单数据。

#### 数据字段 (18列)

| 字段名         | 类型     | 说明                                     |
|----------------|----------|------------------------------------------|
| `Row ID`       | 整数     | 行 ID                                    |
| `Order ID`     | 字符串   | 订单编号                                 |
| `Order Date`   | 日期     | 订单日期                                 |
| `Ship Date`    | 日期     | 发货日期                                 |
| `Ship Mode`    | 分类     | 运送方式                                 |
| `Customer ID`  | 字符串   | 客户 ID                                  |
| `Customer Name`| 字符串   | 客户姓名                                 |
| `Segment`      | 分类     | 客户群体 (消费者/企业/家庭办公)          |
| `Country`      | 字符串   | 国家                                     |
| `City`         | 字符串   | 城市                                     |
| `State`        | 字符串   | 州/省                                    |
| `Postal Code`  | 整数     | 邮编                                     |
| `Region`       | 分类     | 地区 (东部/西部/中部/南部)               |
| `Product ID`   | 字符串   | 产品 ID                                  |
| `Category`     | 分类     | 产品类别 (家具/办公用品/技术)            |
| `Sub-Category` | 分类     | 产品子类别                               |
| `Product Name` | 字符串   | 产品名称                                 |
| `Sales`        | 浮点数   | 销售额 (美元)                            |

#### 数据规模
- **记录数**: 9,800+ 条订单
- **时间范围**: 2015-2018 年
- **客户数**: 793 位独立客户
- **产品数**: 1,850+ 种产品

---

### 🎨 自定义与扩展

#### 替换为您自己的数据
1.  准备您的 CSV 文件，确保其包含类似的字段结构。
2.  替换 `superstore_data.csv` 文件。
3.  修改 `superstore_dashboard.py` 中的字段映射 (第 126-150 行)。
4.  重新启动应用。

#### 添加新图表
参考项目中的图表模板，在 `superstore_dashboard.py` 中复制并修改。所有图表都遵循统一的样式标准 (参见 `get_plotly_layout()` 函数)。

#### 调整配色方案
修改第 147-157 行的 `COLORS` 字典，以应用您的品牌色彩。

---

### 🌐 部署到生产环境

#### 方法1: Streamlit Community Cloud (免费)
1.  将代码推送到 GitHub 仓库。
2.  访问 [share.streamlit.io](https://share.streamlit.io/)。
3.  连接您的 GitHub 仓库并部署。
4.  获得一个公开链接 (例如: `https://your-app.streamlit.app`)。

#### 方法2: 嵌入到公司官网 (iFrame)
```html
<iframe
  src="https://your-app.streamlit.app/?embed=true"
  style="width: 100%; height: 800px; border: none;"
  title="销售仪表板">
</iframe>
```

#### 方法3: 自有服务器 (Docker)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "superstore_dashboard.py", "--server.port=8501"]
```

---

### 🐛 常见问题 (FAQ)

**Q1: PyGWalker 加载缓慢怎么办?**
**A**: 首次加载需要 10-20 秒是正常现象，配置会保存到 `gw_config.json`，后续会快很多。

**Q2: 如何处理中文乱码?**
**A**: 确保您的 CSV 文件编码为 `UTF-8`。如果您的 Excel 导出是 GBK 编码，请使用文本编辑器另存为 UTF-8 编码。

**Q3: 移动端图表显示不全怎么办?**
**A**: Dashboard 已内置响应式设计。如果仍有问题，请尝试横屏查看或在桌面端使用。

**Q4: 如何添加用户登录验证?**
**A**: 您可以使用 `streamlit-authenticator` 库添加简单的用户认证。

**Q5: 数据能否实时更新?**
**A**: 当前版本使用静态 CSV 文件。如需实时更新，可以连接到数据库 (e.g., PostgreSQL/MySQL) 并使用 `@st.cache_data(ttl=600)` 设置刷新间隔（例如每 10 分钟刷新一次）。

---

### 📜 开源协议

MIT 许可证 - 您可以自由使用、修改和分发本项目，但需保留原作者信息。

---

### 🙏 致谢
- **Streamlit 团队** - 提供了出色的 Web 应用框架。
- **Plotly** - 提供了强大的交互式图表库。
- **PyGWalker** - 提供了革命性的拖拽式数据探索工具。
- **Kaggle 社区** - 提供了高质量的数据集。

---

