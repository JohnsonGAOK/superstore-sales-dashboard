# 🛒 Superstore Sales Analysis Dashboard

**Professional Retail Business Intelligence Platform for SMEs**

[![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.18.0-3F4F75.svg)](https://plotly.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 📊 项目概述 | Project Overview

这是一个**专业级零售业务数据可视化Dashboard**,专为中小企业设计。它能帮助企业主和决策者快速理解销售数据、识别业务趋势、发现增长机会。

This is a **professional-grade retail business data visualization dashboard** designed specifically for Small & Medium Enterprises (SMEs). It helps business owners and decision-makers quickly understand sales data, identify trends, and discover growth opportunities.

---

## ✨ 核心功能 | Core Features

### 📈 实时数据分析 | Real-time Data Analytics
- **4个关键指标卡片**: 总销售额、订单数、平均订单价值、独立客户数
- **动态过滤器**: 按年份、产品类别、地区、客户群体筛选
- **自动洞察生成**: AI驱动的业务洞察自动识别

### 📊 10+ 专业图表 | 10+ Professional Charts
1. **月度销售趋势** (折线图) - 识别季节性模式
2. **产品类别销售对比** (柱状图) - 找出畅销品类
3. **地区销售分布** (饼图) - 了解市场覆盖
4. **客户群体分析** (横向柱状图) - 识别核心客户
5. **Top 10 产品榜单** - 发现明星产品
6. **Top 10 客户榜单** - 识别VIP客户
7. **运送方式分析** - 优化物流成本
8. **销售热力图** (月份 vs 年份) - 发现时间模式
9. **高级统计分析** - 描述性统计、相关性、异常值检测
10. **PyGWalker交互式探索** - 拖拽式自定义图表

### 🌍 三语言支持 | Tri-lingual Support
- **English** (默认)
- **繁體中文** (Traditional Chinese)
- **简体中文** (Simplified Chinese)

### 📱 响应式设计 | Responsive Design
- ✅ 桌面端 (Desktop) - 完整体验
- ✅ 平板端 (Tablet) - 优化布局
- ✅ 移动端 (Mobile) - 流畅交互

### 🎨 专业视觉设计 | Professional Visual Design
- **Plotly 标准配色** - 高级感浅色系
- **渐变指标卡片** - 视觉冲击力
- **交互式图表** - Hover提示、缩放、导出
- **数据表格导出** - 一键下载CSV

---

## 🚀 快速开始 | Quick Start

### 1️⃣ 环境要求 | Requirements
- Python 3.8 或更高版本
- 虚拟环境 (推荐)

### 2️⃣ 安装依赖 | Install Dependencies

```bash
# 进入项目目录
cd superstore_dashboard

# (推荐) 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 或 Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 3️⃣ 启动应用 | Launch App

**方法1: 使用启动脚本 (推荐)**
```bash
chmod +x start.sh  # 首次运行需要授权
./start.sh
```

**方法2: 直接命令**
```bash
streamlit run superstore_dashboard.py
```

**方法3: 自定义端口**
```bash
streamlit run superstore_dashboard.py --server.port 8501
```

### 4️⃣ 访问Dashboard
启动后,在浏览器中打开:
```
http://localhost:8501
```

---

## 📁 项目结构 | Project Structure

```
superstore_dashboard/
├── superstore_dashboard.py    # 主应用文件 (900+ 行专业代码)
├── superstore_data.csv         # 示例数据集 (9,800+ 订单记录)
├── requirements.txt            # Python依赖清单
├── README.md                   # 项目说明 (本文件)
├── start.sh                    # 快速启动脚本
├── gw_config.json             # PyGWalker配置 (自动生成)
└── DEPLOYMENT_GUIDE.md        # 部署指南 (可选)
```

---

## 🎯 适用场景 | Use Cases

### 零售业 | Retail
- 📦 产品组合优化
- 🛍️ 库存管理决策
- 💰 定价策略制定

### 电商 | E-commerce
- 🌐 跨区域销售对比
- 👥 客户群体细分
- 📈 营销活动ROI分析

### 批发商 | Wholesale
- 🏢 B2B客户价值评估
- 🚚 物流成本优化
- 📊 季节性需求预测

### 其他 | Others
- **咨询公司**: 为客户生成快速报告
- **创业公司**: 向投资人展示业务增长
- **财务部门**: 销售数据可视化汇报

---

## 🛠️ 技术栈 | Tech Stack

| 技术 | 版本 | 用途 |
|------|------|------|
| **Streamlit** | ≥1.31.0 | Web应用框架 |
| **Plotly** | ≥5.18.0 | 交互式图表库 |
| **Pandas** | ≥2.0.0 | 数据处理与分析 |
| **NumPy** | ≥1.24.0 | 数值计算 |
| **PyGWalker** | ≥0.4.9 | 拖拽式数据探索 |
| **SciPy** | ≥1.11.0 | 高级统计分析 |

---

## 📊 数据说明 | Data Description

### 数据来源
本Dashboard使用的是经典的 **Superstore Sales Dataset**,包含美国一家零售连锁店的历史订单数据。

### 数据字段 (18列)
| 字段名 | 类型 | 说明 |
|--------|------|------|
| `Row ID` | Integer | 行ID |
| `Order ID` | String | 订单编号 |
| `Order Date` | Date | 订单日期 |
| `Ship Date` | Date | 发货日期 |
| `Ship Mode` | Category | 运送方式 |
| `Customer ID` | String | 客户ID |
| `Customer Name` | String | 客户姓名 |
| `Segment` | Category | 客户群体 (Consumer/Corporate/Home Office) |
| `Country` | String | 国家 |
| `City` | String | 城市 |
| `State` | String | 州/省 |
| `Postal Code` | Integer | 邮编 |
| `Region` | Category | 地区 (East/West/Central/South) |
| `Product ID` | String | 产品ID |
| `Category` | Category | 产品类别 (Furniture/Office Supplies/Technology) |
| `Sub-Category` | Category | 产品子类别 |
| `Product Name` | String | 产品名称 |
| `Sales` | Float | 销售额 (美元) |

### 数据规模
- **记录数**: 9,800+ 条订单
- **时间范围**: 2015-2018年
- **客户数**: 793 位独立客户
- **产品数**: 1,850+ 种产品

---

## 🎨 自定义与扩展 | Customization & Extension

### 替换您自己的数据
1. 准备CSV文件,确保包含类似的字段结构
2. 替换 `superstore_data.csv`
3. 修改 `superstore_dashboard.py` 中的字段映射 (第126-150行)
4. 重新启动应用

### 添加新的图表
参考项目中的图表模板,在 `superstore_dashboard.py` 中复制并修改。所有图表遵循统一的样式标准 (参见 `get_plotly_layout()` 函数)。

### 调整配色方案
修改第147-157行的 `COLORS` 字典,应用您的品牌色彩。

---

## 🌐 部署到生产环境 | Production Deployment

### 方法1: Streamlit Community Cloud (免费)
1. 将代码推送到GitHub仓库
2. 访问 [share.streamlit.io](https://share.streamlit.io/)
3. 连接GitHub仓库并部署
4. 获得公开链接 (例: `https://your-app.streamlit.app`)

### 方法2: 嵌入到公司官网 (iFrame)
```html
<iframe
  src="https://your-app.streamlit.app/?embed=true"
  style="width: 100%; height: 800px; border: none;"
  title="Sales Dashboard">
</iframe>
```

### 方法3: 自有服务器 (Docker)
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

## 💼 商业应用建议 | Business Application Tips

### 为客户定制
1. **品牌化**: 替换logo、配色、标题
2. **数据对接**: 连接客户的ERP/CRM系统
3. **定制分析**: 根据客户KPI添加专属图表
4. **培训交付**: 提供30分钟使用培训

### 定价参考 (香港市场)
- **快速启动套餐**: HKD 8,000 - 15,000 (3-5天交付)
- **深度定制方案**: HKD 20,000+ (1-3周交付)
- **月度维护顾问**: HKD 3,000 - 5,000/月

### 销售话术
*"我们为中小企业提供**3天快速交付**的专业销售分析Dashboard。无需招聘数据分析师,无需学习复杂BI工具,只需**一个网页链接**,即可随时随地查看您的业务数据。"*

---

## 🐛 常见问题 | FAQ

### Q1: PyGWalker加载缓慢怎么办?
**A**: 首次加载需要10-20秒是正常现象,配置会保存到 `gw_config.json`,后续会快很多。

### Q2: 如何处理中文乱码?
**A**: 确保CSV文件编码为 `UTF-8`。如果您的Excel导出是GBK编码,使用文本编辑器另存为UTF-8。

### Q3: 移动端图表显示不全?
**A**: 已内置响应式设计。如果仍有问题,尝试横屏查看或在桌面端使用。

### Q4: 如何添加用户登录验证?
**A**: 可以使用 `streamlit-authenticator` 库添加简单的用户认证。

### Q5: 数据能否实时更新?
**A**: 当前版本使用静态CSV。如需实时更新,可连接数据库 (PostgreSQL/MySQL) 并使用 `@st.cache_data(ttl=600)` 设置刷新间隔。

---

## 📜 开源协议 | License

MIT License - 您可以自由使用、修改和分发本项目,但需保留原作者信息。

---

## 🙏 致谢 | Acknowledgments

- **Streamlit Team** - 出色的Web应用框架
- **Plotly** - 强大的交互式图表库
- **PyGWalker** - 革命性的拖拽式数据探索工具
- **Kaggle Community** - 提供高质量数据集

---

## 📧 联系与支持 | Contact & Support

如有任何问题、建议或合作意向,欢迎联系:

- 📧 Email: your-email@example.com
- 💼 LinkedIn: [Your Profile]
- 🌐 Website: [Your Company Website]

---

<div align="center">

**🛒 Built with ❤️ for Small & Medium Enterprises**

*让数据驱动决策,让分析触手可及*

*Make Data-Driven Decisions, Analytics at Your Fingertips*

</div>

