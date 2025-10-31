"""
🛒 Superstore Sales Analysis Dashboard
========================================
专业的零售业务数据可视化分析平台
Professional Retail Business Data Visualization Platform

技术栈 | Tech Stack:
- Streamlit: Web 应用框架
- Plotly: 交互式图表
- Pandas: 数据处理
- SciPy: 高级统计分析

作者 | Author: AI Data Analytics
版本 | Version: 1.1 (性能优化版)
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
from scipy import stats

# ========================================
# 页面配置 | Page Configuration
# ========================================
st.set_page_config(
    page_title="Superstore Sales Dashboard",
    layout="wide",
    page_icon="🛒",
    initial_sidebar_state="expanded"
)

# ========================================
# 自定义样式 | Custom Styles
# ========================================
st.markdown("""
<style>
/* 页面背景 | Page Background */
.main {
    background-color: #F5F7FA;
}

/* 指标卡片美化 | Metric Card Styling - 浅色高级感（紧凑版）*/
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
    padding: 12px 16px;
    border-radius: 10px;
    border: 1px solid #90CAF9;
    box-shadow: 0 2px 8px rgba(33, 150, 243, 0.12);
    transition: all 0.3s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(33, 150, 243, 0.18);
}

[data-testid="stMetric"] label {
    color: #1565C0 !important;
    font-weight: 600 !important;
    font-size: 11px !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #0D47A1 !important;
    font-size: 22px !important;
    font-weight: 700 !important;
}

[data-testid="stMetric"] [data-testid="stMetricDelta"] {
    color: #1976D2 !important;
    font-size: 11px !important;
}

/* 图表容器美化 | Chart Container Styling */
.plotly {
    border-radius: 8px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    background: white;
    padding: 8px;
    border: 1px solid #E0E0E0;
}

/* 侧边栏样式 | Sidebar Styling - 浅色主题 */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #FAFAFA 0%, #F5F5F5 100%);
    border-right: 1px solid #E0E0E0;
}

[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stRadio label {
    color: #424242 !important;
    font-weight: 600 !important;
}

/* 按钮美化 | Button Styling */
.stButton > button {
    background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px 20px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(33, 150, 243, 0.3);
}

/* 下载按钮 | Download Button */
.stDownloadButton > button {
    background: linear-gradient(135deg, #4CAF50 0%, #388E3C 100%);
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px 20px;
    font-weight: 600;
}

/* 响应式设计 | Responsive Design */
@media (max-width: 768px) {
    [data-testid="stMetric"] {
        padding: 12px 16px !important;
        margin-bottom: 8px;
    }
    
    h1 {
        font-size: 22px !important;
    }
    
    h2, h3 {
        font-size: 16px !important;
    }
    
    .plotly {
        max-width: 100%;
        overflow-x: auto;
    }
}

@media (min-width: 769px) and (max-width: 1024px) {
    [data-testid="stMetric"] {
        padding: 14px 18px !important;
    }
}

/* 洞察卡片 | Insight Cards */
.insight-card {
    background: linear-gradient(135deg, #FFFFFF 0%, #F8F9FA 100%);
    border-left: 4px solid #2196F3;
    padding: 14px 18px;
    margin: 8px 0;
    border-radius: 6px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    border: 1px solid #E3F2FD;
}

.insight-card:hover {
    box-shadow: 0 3px 10px rgba(33, 150, 243, 0.15);
    transform: translateX(4px);
    transition: all 0.3s ease;
}

/* 数据来源引用 | Data Source Citation */
.data-source {
    background: #FFF3E0;
    border-left: 4px solid #FF9800;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 16px 0;
}
</style>
""", unsafe_allow_html=True)

# ========================================
# 配色方案 | Color Scheme
# ========================================
COLORS = {
    'plotly_blue': '#636EFA',
    'plotly_red': '#EF553B',
    'plotly_green': '#00CC96',
    'plotly_purple': '#AB63FA',
    'plotly_orange': '#FFA15A',
    'plotly_teal': '#19D3F3',
    'plotly_pink': '#FF6692',
    'plotly_yellow': '#FEC400'
}

# ========================================
# 数据加载与缓存 | Data Loading & Caching
# ========================================
@st.cache_data(show_spinner=False)
def load_data():
    """加载并预处理数据 | Load and preprocess data"""
    try:
        df = pd.read_csv('superstore_data.csv', encoding='utf-8')
        
        # 数据类型转换 | Data type conversion
        df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y', errors='coerce')
        df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y', errors='coerce')
        
        # 提取时间特征 | Extract time features
        df['Year'] = df['Order Date'].dt.year
        df['Month'] = df['Order Date'].dt.month
        df['Quarter'] = df['Order Date'].dt.quarter
        df['Month-Year'] = df['Order Date'].dt.to_period('M').astype(str)
        df['Weekday'] = df['Order Date'].dt.day_name()
        
        # 数据验证 | Data validation
        df = df.dropna(subset=['Order Date', 'Sales'])
        df = df[df['Sales'] > 0]
        
        return df
    
    except Exception as e:
        st.error(f"❌ 数据加载失败 | Data loading failed: {e}")
        return pd.DataFrame()

# ========================================
# 统一图表布局配置 | Unified Chart Layout
# ========================================
def get_plotly_layout(title="", height=400):
    """统一的 Plotly 图表布局 | Unified Plotly chart layout"""
    return {
        'font': {
            'family': 'Arial, Helvetica, sans-serif',
            'size': 12,
            'color': '#37474F'  # 深灰色，确保在白色背景上清晰可读
        },
        'title': {
            'text': title,
            'font': {'size': 16, 'color': '#1565C0', 'family': 'Arial', 'weight': 'bold'},
            'x': 0.5,
            'xanchor': 'center'
        },
        'paper_bgcolor': '#FFFFFF',
        'plot_bgcolor': '#FAFAFA',
        'hovermode': 'closest',
        'hoverlabel': {
            'bgcolor': 'white',
            'font_size': 12,
            'font_family': 'Arial',
            'font_color': '#37474F',
            'bordercolor': '#BDBDBD'
        },
        'height': height,
        'margin': {'l': 50, 'r': 50, 't': 50, 'b': 50},
        'xaxis': {
            'gridcolor': '#E0E0E0',
            'showgrid': True,
            'zeroline': False,
            'linecolor': '#BDBDBD',
            'tickfont': {'color': '#37474F'}  # 深色轴标签
        },
        'yaxis': {
            'gridcolor': '#E0E0E0',
            'showgrid': True,
            'zeroline': False,
            'linecolor': '#BDBDBD',
            'tickfont': {'color': '#37474F'}  # 深色轴标签
        },
    }

# ========================================
# 多语言支持 | Multi-language Support
# ========================================
LANGUAGES = {
    'English': {
        'title': '🛒 Superstore Sales Analysis Dashboard',
        'subtitle': 'Professional Retail Business Intelligence Platform',
        'lang_selector': 'Language',
        'filter_section': '🎯 Data Filters',
        'year_range': 'Year Range',
        'category_filter': 'Product Category',
        'region_filter': 'Sales Region',
        'segment_filter': 'Customer Segment',
        'all': 'All',
        'consumer': 'Consumer',
        'corporate': 'Corporate',
        'home_office': 'Home Office',
        # 指标 | Metrics
        'total_sales': 'Total Sales',
        'total_orders': 'Total Orders',
        'avg_order_value': 'Avg Order Value',
        'unique_customers': 'Unique Customers',
        # 图表标题 | Chart Titles
        'sales_trend': 'Monthly Sales Trend',
        'category_sales': 'Sales by Category',
        'region_sales': 'Sales by Region',
        'segment_sales': 'Sales by Customer Segment',
        'top_products': 'Top 10 Products by Sales',
        'top_customers': 'Top 10 Customers by Revenue',
        'shipping_mode': 'Orders by Shipping Mode',
        'sales_heatmap': 'Sales Heatmap (Month vs Year)',
        # 洞察 | Insights
        'insights_title': '💡 Key Business Insights',
        'data_table': '📋 Detailed Data Table',
        'download_data': 'Download Filtered Data (CSV)',
        'advanced_stats': '📊 Advanced Statistical Analysis',
        # 地图 | Map
        'geo_distribution': '🗺️ Geographic Sales Distribution',
        # 数据来源 | Data Source
        'data_source_title': '📊 Data Source',
        'data_source_text': 'Dataset from Kaggle: <a href="https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting/data" target="_blank" style="color: #FF6F00; font-weight: bold;">Superstore Sales Forecasting Dataset</a>',
    },
    '繁體中文': {
        'title': '🛒 超級市場銷售分析儀表板',
        'subtitle': '專業零售商業智能平台',
        'lang_selector': '語言',
        'filter_section': '🎯 數據篩選器',
        'year_range': '年份範圍',
        'category_filter': '產品類別',
        'region_filter': '銷售地區',
        'segment_filter': '客戶群體',
        'all': '全部',
        'consumer': '消費者',
        'corporate': '企業',
        'home_office': '家庭辦公室',
        'total_sales': '總銷售額',
        'total_orders': '總訂單數',
        'avg_order_value': '平均訂單金額',
        'unique_customers': '獨立客戶數',
        'sales_trend': '月度銷售趨勢',
        'category_sales': '按類別銷售',
        'region_sales': '按地區銷售',
        'segment_sales': '按客戶群體銷售',
        'top_products': '銷售前10產品',
        'top_customers': '消費前10客戶',
        'shipping_mode': '按運送方式訂單',
        'sales_heatmap': '銷售熱力圖（月份 vs 年份）',
        'insights_title': '💡 關鍵業務洞察',
        'data_table': '📋 詳細數據表',
        'download_data': '下載篩選數據 (CSV)',
        'advanced_stats': '📊 高級統計分析',
        'geo_distribution': '🗺️ 地理銷售分布',
        'data_source_title': '📊 數據來源',
        'data_source_text': '數據集來自 Kaggle: <a href="https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting/data" target="_blank" style="color: #FF6F00; font-weight: bold;">Superstore 銷售預測數據集</a>',
    },
    '简体中文': {
        'title': '🛒 超级市场销售分析仪表板',
        'subtitle': '专业零售商业智能平台',
        'lang_selector': '语言',
        'filter_section': '🎯 数据筛选器',
        'year_range': '年份范围',
        'category_filter': '产品类别',
        'region_filter': '销售地区',
        'segment_filter': '客户群体',
        'all': '全部',
        'consumer': '消费者',
        'corporate': '企业',
        'home_office': '家庭办公室',
        'total_sales': '总销售额',
        'total_orders': '总订单数',
        'avg_order_value': '平均订单金额',
        'unique_customers': '独立客户数',
        'sales_trend': '月度销售趋势',
        'category_sales': '按类别销售',
        'region_sales': '按地区销售',
        'segment_sales': '按客户群体销售',
        'top_products': '销售前10产品',
        'top_customers': '消费前10客户',
        'shipping_mode': '按运送方式订单',
        'sales_heatmap': '销售热力图（月份 vs 年份）',
        'insights_title': '💡 关键业务洞察',
        'data_table': '📋 详细数据表',
        'download_data': '下载筛选数据 (CSV)',
        'advanced_stats': '📊 高级统计分析',
        'geo_distribution': '�地理销售分布',
        'data_source_title': '📊 数据来源',
        'data_source_text': '数据集来自 Kaggle: <a href="https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting/data" target="_blank" style="color: #FF6F00; font-weight: bold;">Superstore 销售预测数据集</a>',
    }
}

# ========================================
# 主程序 | Main Program
# ========================================

# 加载数据 | Load data
with st.spinner('Loading data...'):
    df = load_data()

if df.empty:
    st.stop()

# ========================================
# 侧边栏 - 语言与过滤器 | Sidebar - Language & Filters
# ========================================
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/shopping-cart.png", width=80)
    
    # 语言选择 | Language selection
    lang = st.selectbox(
        "Language / 語言 / 语言",
        list(LANGUAGES.keys()),
        index=0
    )
    t = LANGUAGES[lang]
    
    st.markdown("---")
    st.subheader(t['filter_section'])
    
    # 年份范围 | Year range
    year_min, year_max = int(df['Year'].min()), int(df['Year'].max())
    selected_years = st.slider(
        t['year_range'],
        year_min,
        year_max,
        (year_min, year_max)
    )
    
    # 产品类别 | Product category
    categories = [t['all']] + sorted(df['Category'].unique().tolist())
    selected_category = st.selectbox(
        t['category_filter'],
        categories
    )
    
    # 销售地区 | Sales region
    regions = [t['all']] + sorted(df['Region'].unique().tolist())
    selected_region = st.selectbox(
        t['region_filter'],
        regions
    )
    
    # 客户群体 | Customer segment
    segments = [t['all']] + sorted(df['Segment'].unique().tolist())
    selected_segment = st.selectbox(
        t['segment_filter'],
        segments
    )
    
    st.markdown("---")
    st.caption("📊 Dashboard Version 1.0")
    st.caption("💼 Professional BI Solution for SMEs")

# ========================================
# 数据过滤 | Data Filtering
# ========================================
filtered_df = df.copy()

# 应用过滤器 | Apply filters
filtered_df = filtered_df[
    (filtered_df['Year'] >= selected_years[0]) &
    (filtered_df['Year'] <= selected_years[1])
]

if selected_category != t['all']:
    filtered_df = filtered_df[filtered_df['Category'] == selected_category]

if selected_region != t['all']:
    filtered_df = filtered_df[filtered_df['Region'] == selected_region]

if selected_segment != t['all']:
    filtered_df = filtered_df[filtered_df['Segment'] == selected_segment]

# ========================================
# 主标题与副标题 | Main Title & Subtitle
# ========================================
# 使用更紧凑的标题样式，与侧边栏按钮对齐
st.markdown(f"""
<h1 style="margin-top: -60px; margin-bottom: 2px; font-size: 28px; color: #1565C0;">
    {t['title']}
</h1>
<p style="margin-top: 0; margin-bottom: 8px; font-size: 14px; color: #616161; font-weight: 500;">
    {t['subtitle']}
</p>
""", unsafe_allow_html=True)

# ========================================
# 关键指标卡片 (4列) | Key Metrics Cards (4 columns)
# ========================================
col1, col2, col3, col4 = st.columns(4)

total_sales = filtered_df['Sales'].sum()
total_orders = filtered_df['Order ID'].nunique()
avg_order_value = total_sales / total_orders if total_orders > 0 else 0
unique_customers = filtered_df['Customer ID'].nunique()

with col1:
    st.metric(
        t['total_sales'],
        f"${total_sales:,.2f}",
        delta=f"{(total_sales / df['Sales'].sum() * 100):.1f}% of total"
    )

with col2:
    st.metric(
        t['total_orders'],
        f"{total_orders:,}",
        delta=f"{unique_customers:,} customers"
    )

with col3:
    st.metric(
        t['avg_order_value'],
        f"${avg_order_value:,.2f}",
        delta="Per order"
    )

with col4:
    st.metric(
        t['unique_customers'],
        f"{unique_customers:,}",
        delta=f"{(total_orders / unique_customers):.1f} orders/customer"
    )

# ========================================
# 核心可视化区域 - 2列布局 | Core Visualization - 2 Columns
# ========================================
col_left, col_right = st.columns([1.2, 1])

with col_left:
    # 地理销售分布地图 | Geographic Sales Distribution Map
    st.markdown(f"### {t['geo_distribution']}")
    
    # 州名到州代码映射 | State name to state code mapping
    state_abbrev = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
        'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
        'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
        'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
        'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
        'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
        'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
        'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
        'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
        'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
        'District of Columbia': 'DC'
    }
    
    # 按州汇总销售数据 | Aggregate sales by state
    state_sales = filtered_df.groupby('State').agg({
        'Sales': 'sum',
        'Order ID': 'nunique',
        'Customer ID': 'nunique'
    }).reset_index()
    state_sales.columns = ['State', 'Total Sales', 'Orders', 'Customers']
    
    # 转换州名为州代码 | Convert state names to state codes
    state_sales['State Code'] = state_sales['State'].map(state_abbrev)
    
    # 使用 Plotly 的 choropleth 地图 | Use Plotly choropleth map
    geo_fig = px.choropleth(
        state_sales,
        locations='State Code',
        locationmode='USA-states',
        color='Total Sales',
        scope='usa',
        color_continuous_scale='Blues',
        hover_name='State',
        hover_data={
            'State Code': False,
            'Total Sales': ':$,.2f',
            'Orders': ':,',
            'Customers': ':,'
        },
        labels={'Total Sales': 'Sales ($)'}
    )
    
    geo_fig.update_layout(**get_plotly_layout("", height=380))
    geo_fig.update_geos(
        showcountries=False,
        showsubunits=True,
        showlakes=False
    )
    st.plotly_chart(geo_fig, use_container_width=True)

with col_right:
    # 销售趋势图 | Sales Trend
    st.markdown(f"### {t['sales_trend']}")
    
    # 按月汇总销售额 | Aggregate sales by month
    monthly_sales = filtered_df.groupby('Month-Year')['Sales'].sum().reset_index()
    monthly_sales = monthly_sales.sort_values('Month-Year')
    
    trend_fig = go.Figure()
    trend_fig.add_trace(go.Scatter(
        x=monthly_sales['Month-Year'],
        y=monthly_sales['Sales'],
        mode='lines+markers',
        name='Sales',
        line=dict(color=COLORS['plotly_blue'], width=2.5),
        marker=dict(size=6, line=dict(width=1.5, color='white')),
        fill='tonexty',
        fillcolor='rgba(99, 110, 250, 0.15)',
        hovertemplate='<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>'
    ))
    
    trend_fig.update_layout(**get_plotly_layout("", height=380))
    trend_fig.update_xaxes(tickangle=-45)
    st.plotly_chart(trend_fig, use_container_width=True)

# ========================================
# 图表区域 2 - 4列紧凑布局 | Chart Section 2 - 4 Compact Columns
# ========================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    # 按类别销售 | Sales by category
    st.markdown(f"**{t['category_sales']}**")
    category_sales = filtered_df.groupby('Category')['Sales'].sum().reset_index()
    category_sales = category_sales.sort_values('Sales', ascending=False)
    
    cat_fig = px.bar(
        category_sales,
        x='Category',
        y='Sales',
        color='Category',
        color_discrete_sequence=[COLORS['plotly_blue'], COLORS['plotly_orange'], COLORS['plotly_green']],
        text_auto='.2s'
    )
    cat_fig.update_traces(
        marker=dict(line=dict(width=1, color='white')),
        textposition='outside',
        textfont=dict(size=11, color='#37474F'),
        hovertemplate='<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>'
    )
    cat_fig.update_layout(**get_plotly_layout("", height=320))
    cat_fig.update_layout(showlegend=False, margin=dict(l=30, r=30, t=30, b=30))
    st.plotly_chart(cat_fig, use_container_width=True)

with col2:
    # 按地区销售 | Sales by region
    st.markdown(f"**{t['region_sales']}**")
    region_sales = filtered_df.groupby('Region')['Sales'].sum().reset_index()
    region_sales = region_sales.sort_values('Sales', ascending=False)
    
    region_fig = px.pie(
        region_sales,
        values='Sales',
        names='Region',
        color_discrete_sequence=[COLORS['plotly_blue'], COLORS['plotly_green'], COLORS['plotly_orange'], COLORS['plotly_purple']],
        hole=0.45
    )
    region_fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        textfont=dict(size=10, color='white'),
        hovertemplate='<b>%{label}</b><br>Sales: $%{value:,.2f}<br>%{percent}<extra></extra>'
    )
    region_fig.update_layout(**get_plotly_layout("", height=320))
    region_fig.update_layout(showlegend=False, margin=dict(l=10, r=10, t=30, b=10))
    st.plotly_chart(region_fig, use_container_width=True)

with col3:
    # 按客户群体销售 | Sales by segment
    st.markdown(f"**{t['segment_sales']}**")
    segment_sales = filtered_df.groupby('Segment')['Sales'].sum().reset_index()
    segment_sales = segment_sales.sort_values('Sales', ascending=True)
    
    segment_fig = px.bar(
        segment_sales,
        y='Segment',
        x='Sales',
        orientation='h',
        color='Segment',
        color_discrete_sequence=[COLORS['plotly_purple'], COLORS['plotly_teal'], COLORS['plotly_pink']],
        text_auto='.2s'
    )
    segment_fig.update_traces(
        marker=dict(line=dict(width=1, color='white')),
        textposition='outside',
        textfont=dict(size=11, color='#37474F'),
        hovertemplate='<b>%{y}</b><br>Sales: $%{x:,.2f}<extra></extra>'
    )
    segment_fig.update_layout(**get_plotly_layout("", height=320))
    segment_fig.update_layout(showlegend=False, margin=dict(l=30, r=30, t=30, b=30))
    st.plotly_chart(segment_fig, use_container_width=True)

with col4:
    # 运送方式分布 | Shipping mode distribution
    st.markdown(f"**{t['shipping_mode']}**")
    shipping_data = filtered_df.groupby('Ship Mode').agg({
        'Order ID': 'count',
        'Sales': 'sum'
    }).reset_index()
    shipping_data.columns = ['Ship Mode', 'Orders', 'Sales']
    shipping_data = shipping_data.sort_values('Orders', ascending=False)
    
    shipping_fig = px.bar(
        shipping_data,
        x='Ship Mode',
        y='Orders',
        color='Sales',
        color_continuous_scale='Greens',
        text='Orders'
    )
    shipping_fig.update_traces(
        marker=dict(line=dict(width=1, color='white')),
        textposition='outside',
        textfont=dict(size=10, color='#37474F'),
        hovertemplate='<b>%{x}</b><br>Orders: %{y}<br>Sales: $%{marker.color:,.2f}<extra></extra>'
    )
    shipping_fig.update_layout(**get_plotly_layout("", height=320))
    shipping_fig.update_layout(coloraxis_showscale=False, margin=dict(l=30, r=30, t=30, b=70))
    shipping_fig.update_xaxes(tickangle=-45, tickfont=dict(size=9))
    st.plotly_chart(shipping_fig, use_container_width=True)

# ========================================
# 图表区域 3 - Top 10 与热力图 | Chart Section 3 - Top 10 & Heatmap
# ========================================
col1, col2, col3 = st.columns(3)

with col1:
    # Top 10 产品 | Top 10 products
    st.markdown(f"**{t['top_products']}**")
    top_products = filtered_df.groupby('Product Name')['Sales'].sum().reset_index()
    top_products = top_products.nlargest(10, 'Sales')
    top_products = top_products.sort_values('Sales', ascending=True)
    
    product_fig = px.bar(
        top_products,
        y='Product Name',
        x='Sales',
        orientation='h',
        color='Sales',
        color_continuous_scale='Blues',
        text_auto='.2s'
    )
    product_fig.update_traces(
        marker=dict(line=dict(width=0.5, color='white')),
        textposition='outside',
        textfont=dict(size=9, color='#37474F'),
        hovertemplate='<b>%{y}</b><br>Sales: $%{x:,.2f}<extra></extra>'
    )
    product_fig.update_layout(**get_plotly_layout("", height=350))
    product_fig.update_layout(coloraxis_showscale=False, margin=dict(l=10, r=50, t=30, b=30))
    product_fig.update_yaxes(tickfont=dict(size=9))
    st.plotly_chart(product_fig, use_container_width=True)

with col2:
    # Top 10 客户 | Top 10 customers
    st.markdown(f"**{t['top_customers']}**")
    top_customers = filtered_df.groupby('Customer Name')['Sales'].sum().reset_index()
    top_customers = top_customers.nlargest(10, 'Sales')
    top_customers = top_customers.sort_values('Sales', ascending=True)
    
    customer_fig = px.bar(
        top_customers,
        y='Customer Name',
        x='Sales',
        orientation='h',
        color='Sales',
        color_continuous_scale='Purples',
        text_auto='.2s'
    )
    customer_fig.update_traces(
        marker=dict(line=dict(width=0.5, color='white')),
        textposition='outside',
        textfont=dict(size=9, color='#37474F'),
        hovertemplate='<b>%{y}</b><br>Sales: $%{x:,.2f}<extra></extra>'
    )
    customer_fig.update_layout(**get_plotly_layout("", height=350))
    customer_fig.update_layout(coloraxis_showscale=False, margin=dict(l=10, r=50, t=30, b=30))
    customer_fig.update_yaxes(tickfont=dict(size=9))
    st.plotly_chart(customer_fig, use_container_width=True)

with col3:
    # 销售热力图 | Sales heatmap
    st.markdown(f"**{t['sales_heatmap']}**")
    heatmap_data = filtered_df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
    heatmap_pivot = heatmap_data.pivot(index='Month', columns='Year', values='Sales')
    
    heatmap_fig = go.Figure(data=go.Heatmap(
        z=heatmap_pivot.values,
        x=heatmap_pivot.columns,
        y=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        colorscale='Blues',
        text=np.round(heatmap_pivot.values, 0),
        texttemplate='%{text:,.0f}',
        textfont={"size": 8, "color": "#37474F"},
        colorbar=dict(
            title=dict(text="Sales", font=dict(size=10)),
            tickfont=dict(size=9)
        )
    ))
    heatmap_fig.update_layout(**get_plotly_layout("", height=350))
    heatmap_fig.update_layout(margin=dict(l=30, r=30, t=30, b=30))
    heatmap_fig.update_xaxes(tickfont=dict(size=9))
    heatmap_fig.update_yaxes(tickfont=dict(size=9))
    st.plotly_chart(heatmap_fig, use_container_width=True)

# ========================================
# 高级统计分析 (可折叠) | Advanced Statistics (Collapsible)
# ========================================
with st.expander(f"📊 {t['advanced_stats']}", expanded=False):
    st.markdown("### 📈 Descriptive Statistics for Sales")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 销售额描述性统计 | Sales descriptive statistics
        sales_stats = filtered_df['Sales'].describe()
        sales_stats_df = pd.DataFrame(sales_stats).T
        sales_stats_df['Skewness'] = stats.skew(filtered_df['Sales'].dropna())
        sales_stats_df['Kurtosis'] = stats.kurtosis(filtered_df['Sales'].dropna())
        
        st.dataframe(sales_stats_df.style.format("{:.2f}"), use_container_width=True)
        
        # 销售额分布直方图 | Sales distribution histogram
        hist_fig = px.histogram(
            filtered_df,
            x='Sales',
            nbins=50,
            color_discrete_sequence=[COLORS['plotly_blue']],
            marginal='box'
        )
        hist_fig.update_layout(**get_plotly_layout("Sales Distribution", height=350))
        st.plotly_chart(hist_fig, use_container_width=True)
    
    with col2:
        # 相关性分析 | Correlation analysis
        st.markdown("**📊 Correlation Analysis**")
        st.caption("Analyze relationships between key metrics")
        
        # 计算每个订单的汇总数据用于相关性分析
        order_summary = filtered_df.groupby('Order ID').agg({
            'Sales': 'sum',
            'Row ID': 'count'  # 作为订单项数量
        }).reset_index()
        order_summary.columns = ['Order ID', 'Total Sales', 'Items Count']
        
        if len(order_summary) > 1:
            corr_data = order_summary[['Total Sales', 'Items Count']].corr()
            
            corr_fig = go.Figure(data=go.Heatmap(
                z=corr_data.values,
                x=corr_data.columns,
                y=corr_data.columns,
                colorscale='RdBu',
                zmid=0,
                text=corr_data.values.round(2),
                texttemplate='%{text}',
                textfont={"size": 14, "color": "white"},
                colorbar=dict(title="Correlation")
            ))
            corr_fig.update_layout(**get_plotly_layout("", height=350))
            st.plotly_chart(corr_fig, use_container_width=True)
        
        # 箱型图 | Box plot
        box_fig = px.box(
            filtered_df,
            x='Category',
            y='Sales',
            color='Category',
            color_discrete_sequence=[COLORS['plotly_blue'], COLORS['plotly_orange'], COLORS['plotly_green']],
            points='outliers'
        )
        box_fig.update_layout(**get_plotly_layout("Sales Distribution by Category", height=350))
        box_fig.update_layout(showlegend=False)
        st.plotly_chart(box_fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ========================================
# 业务洞察卡片 | Business Insights Cards
# ========================================
st.markdown(f"### {t['insights_title']}")

# 自动生成洞察 | Auto-generate insights
top_category = filtered_df.groupby('Category')['Sales'].sum().idxmax()
top_category_sales = filtered_df.groupby('Category')['Sales'].sum().max()
top_category_pct = (top_category_sales / total_sales * 100)

top_region = filtered_df.groupby('Region')['Sales'].sum().idxmax()
top_region_sales = filtered_df.groupby('Region')['Sales'].sum().max()
top_region_pct = (top_region_sales / total_sales * 100)

top_segment = filtered_df.groupby('Segment')['Sales'].sum().idxmax()
top_segment_sales = filtered_df.groupby('Segment')['Sales'].sum().max()

best_month = monthly_sales.loc[monthly_sales['Sales'].idxmax(), 'Month-Year']
best_month_sales = monthly_sales['Sales'].max()

avg_delivery_time = (filtered_df['Ship Date'] - filtered_df['Order Date']).dt.days.mean()

# 2行3列紧凑布局 | 2 rows x 3 columns compact layout
col1, col2, col3 = st.columns(3)

insights_row1 = [
    {
        'icon': '🏆',
        'title': 'Top Category',
        'content': f"<b>{top_category}</b>: ${top_category_sales:,.0f} ({top_category_pct:.1f}%)"
    },
    {
        'icon': '🌍',
        'title': 'Top Region',
        'content': f"<b>{top_region}</b>: ${top_region_sales:,.0f} ({top_region_pct:.1f}%)"
    },
    {
        'icon': '👥',
        'title': 'Top Segment',
        'content': f"<b>{top_segment}</b>: ${top_segment_sales:,.0f}"
    }
]

for col, insight in zip([col1, col2, col3], insights_row1):
    with col:
        st.markdown(f"""
        <div class="insight-card">
            <h4 style="margin: 0 0 6px 0; color: #1565C0; font-size: 14px;">{insight['icon']} {insight['title']}</h4>
            <p style="margin: 0; color: #37474F; line-height: 1.4; font-size: 13px;">{insight['content']}</p>
        </div>
        """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

insights_row2 = [
    {
        'icon': '📅',
        'title': 'Peak Month',
        'content': f"<b>{best_month}</b>: ${best_month_sales:,.0f}"
    },
    {
        'icon': '🚚',
        'title': 'Avg Delivery',
        'content': f"<b>{avg_delivery_time:.1f} days</b> average delivery time"
    },
    {
        'icon': '📦',
        'title': 'Orders/Customer',
        'content': f"<b>{(total_orders / unique_customers):.1f}</b> average orders per customer"
    }
]

for col, insight in zip([col1, col2, col3], insights_row2):
    with col:
        st.markdown(f"""
        <div class="insight-card">
            <h4 style="margin: 0 0 6px 0; color: #1565C0; font-size: 14px;">{insight['icon']} {insight['title']}</h4>
            <p style="margin: 0; color: #37474F; line-height: 1.4; font-size: 13px;">{insight['content']}</p>
        </div>
        """, unsafe_allow_html=True)

# ========================================
# 数据表格与下载 | Data Table & Download
# ========================================
with st.expander(f"📋 {t['data_table']}", expanded=False):
    st.dataframe(
        filtered_df[[
            'Order Date', 'Customer Name', 'Category', 'Sub-Category',
            'Product Name', 'Region', 'Segment', 'Sales', 'Ship Mode'
        ]].sort_values('Order Date', ascending=False),
        use_container_width=True,
        height=400
    )
    
    # 下载按钮 | Download button
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=f"⬇️ {t['download_data']}",
        data=csv,
        file_name=f"superstore_filtered_data_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

# ========================================
# 数据来源引用 | Data Source Citation
# ========================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div class="data-source">
    <strong>{t['data_source_title']}</strong><br>
    {t['data_source_text']}<br>
    📅 <strong>Data Period:</strong> {filtered_df['Order Date'].min().date()} to {filtered_df['Order Date'].max().date()} | <strong>Records:</strong> {len(filtered_df):,}
</div>
""", unsafe_allow_html=True)

# ========================================
# 页脚 | Footer
# ========================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7F8C8D; padding: 20px;">
    <p><b>🛒 Superstore Sales Dashboard</b> | Version 1.1 (Performance Optimized)</p>
    <p>Built with ❤️ using Streamlit, Plotly, Pandas & SciPy</p>
    <p>💼 Professional BI Solution for Small & Medium Enterprises</p>
</div>
""", unsafe_allow_html=True)

