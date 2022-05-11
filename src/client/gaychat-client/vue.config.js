module.exports = {
  css: {
    // less antdv全局颜色设置
    loaderOptions: {
      less: {
        lessOptions: {
          modifyVars: {
            // If you are using less-loader@5 please spread the lessOptions to options directly
            /* "primary-color": "#D48806",
            "link-color": "#D48806",
            "layout-header-background": "#3B1B00", */
            'heading-color': '#2C3E50',
            'text-color': '#2C3E50',
            'border-radius-base': '4px'
            // 'typography-title-font-weight': '500',
          },
          javascriptEnabled: true
        }
      }
    }
  },
  // transpileDependencies: true

  // 开发时使用以下配置项开启 vue 代理服务解决 CORS 跨域问题
  /* devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:3001',
        ws: true,
        changeOrigin: true
      }
    }
  } */
}
