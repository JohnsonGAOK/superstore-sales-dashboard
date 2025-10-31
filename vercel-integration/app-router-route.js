// ===================================
// 方式 1: Next.js App Router (推荐)
// ===================================
// 文件位置: app/dashboard/route.js
// 
// 使用方法:
// 1. 复制这个文件到你的 Next.js 项目的 app/dashboard/route.js
// 2. 推送到 GitHub
// 3. Vercel 自动部署
// 4. 访问: https://你的域名.com/dashboard

import { NextResponse } from 'next/server';

// 使用 Edge Runtime 获得更快的响应速度
export const runtime = 'edge';

// 配置缓存
export const revalidate = 60; // 60 秒重新验证

export async function GET(request) {
  const url = new URL(request.url);
  
  // 构建 Streamlit URL
  const streamlitUrl = 'https://superstore-sales-dashboard-johnson.streamlit.app' + url.search;
  
  try {
    // 代理请求到 Streamlit
    const response = await fetch(streamlitUrl, {
      headers: {
        'User-Agent': request.headers.get('user-agent') || 'Mozilla/5.0',
        'Accept': request.headers.get('accept') || 'text/html',
        'Accept-Language': request.headers.get('accept-language') || 'zh-CN,zh;q=0.9',
      },
      // 10 秒超时
      signal: AbortSignal.timeout(10000),
    });
    
    if (!response.ok) {
      throw new Error(`Streamlit returned ${response.status}`);
    }
    
    // 获取响应内容
    const contentType = response.headers.get('Content-Type') || 'text/html';
    const data = await response.arrayBuffer();
    
    // 返回响应
    return new NextResponse(data, {
      status: 200,
      headers: {
        'Content-Type': contentType,
        'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300',
        'X-Proxied-By': 'Vercel',
      },
    });
    
  } catch (error) {
    console.error('Dashboard proxy error:', error);
    
    // 返回友好的错误页面
    return new NextResponse(`
      <!DOCTYPE html>
      <html lang="zh-CN">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard 加载中</title>
        <style>
          body {
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          }
          .container {
            text-align: center;
            background: white;
            padding: 60px 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 500px;
          }
          h1 {
            font-size: 24px;
            color: #333;
            margin-bottom: 20px;
          }
          p {
            font-size: 16px;
            color: #666;
            margin-bottom: 30px;
            line-height: 1.6;
          }
          button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 14px 32px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
          }
          button:hover {
            transform: translateY(-2px);
          }
          .emoji {
            font-size: 64px;
            margin-bottom: 20px;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="emoji">⚠️</div>
          <h1>Dashboard 暂时不可用</h1>
          <p>服务器正在响应中，请稍后重试<br>如果问题持续，请联系管理员</p>
          <button onclick="location.reload()">🔄 重新加载</button>
        </div>
      </body>
      </html>
    `, { 
      status: 503,
      headers: { 
        'Content-Type': 'text/html; charset=utf-8',
        'Retry-After': '30',
      }
    });
  }
}

// 处理 OPTIONS 请求（CORS 预检）
export async function OPTIONS() {
  return new NextResponse(null, {
    status: 200,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}

