const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const path = require('path');
const { sourceMapsEnabled } = require('process');

module.exports = {
  entry: {
    order: './toursite/static/toursite/scripts/order.js',
    tourorder: './toursite/static/toursite/scripts/tourorder.js'
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'js', 'static')
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        }
      },
      {
        test: /\.scss$/,
        use: [
          // style-loader переносить стилі в тег <style> у head
          'style-loader',
          // css-loader перетворює CSS в модуль JS
          'css-loader',
          // sass-loader перетворює SCSS в CSS
          'sass-loader', MiniCssExtractPlugin.loader, {
            loader : "sass-loader", 
            options: {sourceMap: true}
          }
        ]
      }
    ]
  }
};
