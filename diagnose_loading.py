"""
🔍 Dashboard 加载诊断脚本
Quick diagnostic tool to check dashboard loading time
"""

import time
import pandas as pd

print("=" * 60)
print("🔍 Dashboard 加载诊断测试")
print("=" * 60)

# 测试 1: 数据加载速度
print("\n[1/4] 测试数据加载速度...")
start = time.time()
try:
    df = pd.read_csv('superstore_data.csv', encoding='utf-8')
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y', errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y', errors='coerce')
    load_time = time.time() - start
    print(f"   ✅ 数据加载成功: {load_time:.2f}秒")
    print(f"   📊 数据行数: {len(df):,} 行")
    print(f"   💾 数据大小: {df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")
except Exception as e:
    print(f"   ❌ 数据加载失败: {e}")
    exit(1)

# 测试 2: 检查依赖包
print("\n[2/4] 检查必需的包...")
required_packages = ['streamlit', 'plotly', 'pandas', 'numpy', 'scipy', 'pygwalker']
for pkg in required_packages:
    try:
        __import__(pkg)
        print(f"   ✅ {pkg}: 已安装")
    except ImportError:
        print(f"   ❌ {pkg}: 未安装")

# 测试 3: 检查数据完整性
print("\n[3/4] 检查数据完整性...")
missing_cols = set(['Order Date', 'Sales', 'Category', 'Region', 'Segment']) - set(df.columns)
if missing_cols:
    print(f"   ❌ 缺少关键列: {missing_cols}")
else:
    print(f"   ✅ 所有关键列存在")
    print(f"   📉 空值率: {(df.isnull().sum().sum() / df.size * 100):.2f}%")

# 测试 4: 模拟Dashboard启动
print("\n[4/4] 模拟 Dashboard 计算...")
start = time.time()
try:
    # 模拟 Dashboard 的主要计算
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df = df.dropna(subset=['Order Date', 'Sales'])
    
    # 模拟聚合计算
    monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
    category_sales = df.groupby('Category')['Sales'].sum()
    region_sales = df.groupby('Region')['Sales'].sum()
    
    calc_time = time.time() - start
    print(f"   ✅ Dashboard 计算完成: {calc_time:.2f}秒")
except Exception as e:
    print(f"   ❌ Dashboard 计算失败: {e}")

# 总结
print("\n" + "=" * 60)
total_time = load_time + calc_time
print(f"📊 预估 Dashboard 首次加载时间: {total_time:.2f}秒")

if total_time < 2:
    print("✅ 加载速度: 非常快")
elif total_time < 5:
    print("⚠️  加载速度: 正常")
else:
    print("❌ 加载速度: 较慢，建议优化")

print("\n💡 建议:")
if total_time > 3:
    print("   - 数据较大，首次加载需要等待")
    print("   - 使用浏览器时请耐心等待 5-10 秒")
    print("   - 加载完成后，切换筛选器会很快（已缓存）")
else:
    print("   - 加载速度正常")
    print("   - 如果浏览器一直加载，检查网络连接")
    print("   - 尝试强制刷新: Command + Shift + R")

print("=" * 60)
