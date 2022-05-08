# GayChat

Simple, elegant web chat application.

基于 Web 的在线聊天社交平台
### 架构

```
client
├── vue
├── ...
└── ant design

server
├── Python
├── ...
└── Mysql
```

### 环境及依赖版本

#### 前端

> 一个众所周知的事实是，node 开发对依赖版本极为敏感，经常出现一些与依赖相关的臭名昭著的问题。随着时间推移, 除文档中注明的、开发时最终所使用的特定版本号可以保证可用外，其余各依赖不同的版本组合均有可能变为可用/不可用。因此，如有需要尝试某些依赖的其他版本，请在安装相关环境时自行测试。

从 nvm 在 github 的仓库下载并安装 nvm，使用 nvm 管理 node 版本。

nvm 0.39.1

node v16.15.0

npm 8.9.0

**注意：npm 镜像源也会对依赖问题造成影响，开发时使用如下镜像源（原淘宝镜像，国内裸连速度较高）**
```
npm config set home https://npmmirror.com
npm config set registry https://registry.npmmirror.com
```
```
npm ls -g
/Users/vickko/.nvm/versions/node/v16.15.0/lib
├── @vue/cli@5.0.4
├── corepack@0.10.0
└── npm@8.9.0
```
```
npm ls
gaychat-client@0.1.0 /Users/vickko/Documents/Code/nosync.nosync/GayChat/src/client/gaychat-client
├── @babel/core@7.17.10
├── @babel/eslint-parser@7.17.0
├── @vue/cli-plugin-babel@5.0.4
├── @vue/cli-plugin-eslint@5.0.4
├── @vue/cli-plugin-router@5.0.4
├── @vue/cli-service@5.0.4
├── @vue/eslint-config-standard@6.1.0
├── core-js@3.22.4
├── eslint-plugin-import@2.26.0
├── eslint-plugin-node@11.1.0
├── eslint-plugin-promise@5.2.0
├── eslint-plugin-vue@8.7.1
├── eslint@7.32.0
├── vue-router@4.0.15
└── vue@3.2.33
```

## TODO:

1. 添加大致功能需求文档
2. 完善功能需求细分子项

### 功能

1. 用户系统 （注册、登录、登出、删除）
2. 用户资料 （Profile、status）
3. 好友关系，群聊
4. 聊天系统 （私聊，群聊，发送文件）

## API

* 接口基准地址： ```{{url}}/api/develop/```
* 使用 Token 鉴定授权状态
* 使用标准 HTTP Status Code 标识状态
* 请求和响应数据统一使用 JSON 格式

#### login

* 请求路径：```login```
* 请求方法： ```post```
* 请求参数：
```
{
    username: '',   // 用户名, not null
    passwd: '',     // 密码, not null
}
```
* 响应参数：
```
{
    data: {
        username: '',   
        token: '',       // 基于 jwt
    },
    meta: {
        msg: '',        // 请求状态提示
        status： '',    // HTTP Status Code
    }
}
```