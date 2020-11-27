/*
 * @Description: 描述
 * @Author: 吴文周
 * @Github: http://gitlab.yzf.net/wuwenzhou
 * @Date: 2019-11-19 08:46:03
 * @LastEditors: 吴文周
 * @LastEditTime: 2020-11-27 09:15:26
 */
const path = require('path')
const ispro = process.env.NODE_ENV !== 'development'
function resolve(dir) {
  return path.join(__dirname, dir)
}
module.exports = {
  pages: {
    // 多页面时可以配置按需打包
    index: {
      // page 的入口
      entry: 'src/pages/index/main.js',
      // 模板来源
      template: 'src/pages/index/index.html',
      // 在 dist/index.html 的输出
      filename: 'index.html',
      // 当使用 title 选项时，
      // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'EasyWork',
      chunks: ['chunk-vendors', 'chunk-common', 'index']
    }
  },
  publicPath: ispro ? 'http://cdn.wuwenzhou.com.cn' : '/',
  // publicPath: ispro ? '' : '/',
  // outputDir: '../tensorflow-server/static',
  assetsDir: 'static',
  lintOnSave: false,
  productionSourceMap: false,
  devServer: {
    port:9527,
    proxy: {
      '/api': {
        target: 'http://localhost:9567'
      },
      '/socket.io': {
        target: 'http://localhost:9567',
        ws:true
      },
    }
  },
  chainWebpack: config => {
    config.resolve.alias
      .set('@', resolve('src'))
      .set('assets', resolve('src/assets'))
      .set('components', resolve('src/components'))
      .set('base', resolve('baseConfig'))
      .set('public', resolve('public'))
    // if (ispro) {
    //     config.plugin('html')
    //     .tap(args => {
    //         args[0].cdn = cdn;
    //       return args;
    //     })
    //   }
  }
}
