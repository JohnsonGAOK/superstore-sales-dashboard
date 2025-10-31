// ===================================
// Next.js 配置文件（完整代理方案）
// ===================================
// 文件位置: next.config.js (项目根目录)
// 
// 这个配置文件提供了完整的代理支持，包括:
// - 主 Dashboard 页面
// - Streamlit 静态资源
// - WebSocket 连接
// 
// 使用方法:
// 1. 复制这个文件到你的 Next.js 项目根目录（如果已有，合并配置）
// 2. 推送到 GitHub
// 3. Vercel 自动部署

/** @type {import('next').NextConfig} */
const nextConfig = {
  // ... 你的其他配置

  async rewrites() {
    return [
      // Dashboard 主页面
      {
        source: '/dashboard',
        destination: 'https://superstore-sales-dashboard-johnson.streamlit.app',
      },
      // Dashboard 静态资源（CSS, JS, 图片等）
      {
        source: '/dashboard/static/:path*',
        destination: 'https://superstore-sales-dashboard-johnson.streamlit.app/static/:path*',
      },
      // Streamlit 核心文件
      {
        source: '/dashboard/_stcore/:path*',
        destination: 'https://superstore-sales-dashboard-johnson.streamlit.app/_stcore/:path*',
      },
      // Streamlit 组件
      {
        source: '/dashboard/component/:path*',
        destination: 'https://superstore-sales-dashboard-johnson.streamlit.app/component/:path*',
      },
      // Streamlit WebSocket（实时更新）
      {
        source: '/dashboard/_stcore/stream',
        destination: 'https://superstore-sales-dashboard-johnson.streamlit.app/_stcore/stream',
      },
      // 健康检查
      {
        source: '/dashboard/healthz',
        destination: 'https://superstore-sales-dashboard-johnson.streamlit.app/healthz',
      },
    ];
  },

  async headers() {
    return [
      {
        source: '/dashboard/:path*',
        headers: [
          // CORS 支持
          {
            key: 'Access-Control-Allow-Origin',
            value: '*',
          },
          {
            key: 'Access-Control-Allow-Methods',
            value: 'GET, POST, PUT, DELETE, OPTIONS',
          },
          {
            key: 'Access-Control-Allow-Headers',
            value: 'Content-Type, Authorization',
          },
          // 缓存优化
          {
            key: 'Cache-Control',
            value: 'public, s-maxage=60, stale-while-revalidate=300',
          },
          // 安全头
          {
            key: 'X-Frame-Options',
            value: 'SAMEORIGIN',
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
        ],
      },
    ];
  },

  // 图片优化配置（如果 Dashboard 有图片）
  images: {
    domains: ['superstore-sales-dashboard-johnson.streamlit.app'],
  },
};

module.exports = nextConfig;


// ===================================
// 简化版配置（最小化配置）
// ===================================
// 如果上面的配置太复杂，可以只用这个简化版:

/*
module.exports = {
  async rewrites() {
    return [
      {
        source: '/dashboard/:path*',
        destination: 'https://superstore-sales-dashboard-johnson.streamlit.app/:path*',
      },
    ];
  },
};
*/

