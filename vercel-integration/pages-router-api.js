// ===================================
// 方式 2: Next.js Pages Router
// ===================================
// 文件位置: pages/api/dashboard.js
// 
// 使用方法:
// 1. 复制这个文件到你的 Next.js 项目的 pages/api/dashboard.js
// 2. 推送到 GitHub
// 3. Vercel 自动部署
// 4. 访问: https://你的域名.com/api/dashboard

export default async function handler(req, res) {
  // 只允许 GET 请求
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  
  const { query } = req;
  const queryString = new URLSearchParams(query).toString();
  
  // 构建 Streamlit URL
  const streamlitUrl = `https://superstore-sales-dashboard-johnson.streamlit.app${queryString ? '?' + queryString : ''}`;
  
  try {
    // 代理请求到 Streamlit
    const response = await fetch(streamlitUrl, {
      headers: {
        'User-Agent': req.headers['user-agent'] || 'Mozilla/5.0',
        'Accept': req.headers['accept'] || 'text/html',
        'Accept-Language': 'zh-CN,zh;q=0.9',
      },
      signal: AbortSignal.timeout(10000), // 10 秒超时
    });
    
    if (!response.ok) {
      throw new Error(`Streamlit returned ${response.status}`);
    }
    
    // 获取响应数据
    const contentType = response.headers.get('Content-Type') || 'text/html';
    const data = await response.text();
    
    // 设置响应头
    res.setHeader('Content-Type', contentType);
    res.setHeader('Cache-Control', 'public, s-maxage=60, stale-while-revalidate=300');
    res.setHeader('X-Proxied-By', 'Vercel');
    
    // 返回数据
    res.status(200).send(data);
    
  } catch (error) {
    console.error('Dashboard proxy error:', error);
    
    // 返回友好的错误页面
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    res.setHeader('Retry-After', '30');
    res.status(503).send(`
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
    `);
  }
}

// 配置 API 路由
export const config = {
  api: {
    // 允许大响应
    responseLimit: false,
    // 禁用 body 解析
    bodyParser: false,
  },
};

