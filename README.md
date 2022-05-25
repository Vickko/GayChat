<h1 align="center">
    <img src="https://i.jpg.dog/file/jpg-dog/de6d6ec5db96ba888b4638f2385c0f8c.png" alt="GayChat" width="240">
</h1>
<p align="center">
Simple, elegant web chat application based on <a href="https://socket.io/">Socket.IO</a>.

</p>
<p align="center">
  <a href="https://github.com/Vickko/GayChat/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-WTFPL-brightgreen"></a>
  <a href="https://cn.vuejs.org/"><img src="https://img.shields.io/badge/vue-3.0%2B-blueviolet"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.6%2B-informational"></a>
</p>

## 架构

```
client
├── vue
├── ...
└── ant design

server
├── Python
├── Alibaba Cloud
├── Redis
├── ...
└── Mysql
```

## 环境及依赖版本

### 前端

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
├── @vue/cli-plugin-babel@4.5.17
├── @vue/cli-plugin-eslint@4.5.17
├── @vue/cli-plugin-router@4.5.17
├── @vue/cli-service@4.5.17
├── @vue/compiler-sfc@3.2.33
├── @vue/eslint-config-standard@5.1.2
├── ant-design-vue@3.2.3
├── axios@0.27.2
├── babel-eslint@10.1.0
├── core-js@3.22.4
├── eslint-plugin-import@2.26.0
├── eslint-plugin-node@11.1.0
├── eslint-plugin-promise@4.3.1
├── eslint-plugin-standard@4.1.0
├── eslint-plugin-vue@7.20.0
├── eslint@6.8.0
├── less-loader@6.2.0
├── less@4.1.2
├── vue-router@4.0.15
└── vue@3.2.33
```

## 功能和需求

### Overall:

1. 用户系统 （注册、登录、登出、删除）
2. 用户资料 （Profile、status）
3. 好友关系，群聊

- 支持添加好友功能及好友在线状态查看

4. 聊天系统 （私聊，群聊，发送文件）

- 实现任意用户间的即时通讯和聊天记录加密存储
- 支持通讯过程中进行多种文件格式的传递
- 支持群聊功能
- 支持在聊天过程中发送表情
- ~~支持对 v 佬进行光速开盒~~

## TODO:

1. 完善功能需求细分子项
2. 文档添加 logout API

### 前端：

1. 开始 Index 和其他相关页面的 UI 设计
2. 细化 Login 页面 UI 实现
3. 完成后续 API 逻辑原型

### 后端

1. 完善文档中后端部分技术栈内容
2. 数据库增加 userid-token 表及相关逻辑
3. login api 增加非法输入及用户名/密码不正确时的返回数据
4. 增加 token 销毁逻辑 （等待 logout API ref）
5. 增加 token expire-time 及其更新逻辑
6. 完成后续 API 接口及相关逻辑
7. 开始 socket.io 部分相关进度

## API

- 接口基准地址： `{{url}}/api/develop/`
- 使用 Token 鉴定授权状态
- 使用标准 HTTP Status Code 标识状态
- 请求和响应数据统一使用 JSON 格式

### 注册，登录与权限验证

#### 用户登录

- 描述： 常规的登录请求，使用 jwt 进行用户鉴权。
- 请求路径：`login`
- 请求方法： `post`
- 请求参数：

```
{
    username: '',   // 用户名, not null
    password: '',     // 密码, not null
}
```

- 响应参数：

```
{
    data: {
        id: '',
        token: '',       // 基于 jwt
    },
    meta: {
        msg: '',        // 请求状态提示
        status: '',    // HTTP Status Code
    }
}
```

#### 用户注册

- 描述：常规的注册请求，后台记录请求 ip 一分钟以防止恶意脚本，请求参数是除了id、 vipLevel 和 isDev 外， User 表内所有内容
- 请求路径：`signup`
- 请求方法： `post`
- 请求参数：

```
{
    username: '',   // 用户名, not null
    password: '',     // 密码, not null
    icon_id: '',
    email: '',
    sex: '',        //Boolean
    introduction: '',
    birth: '',
}
```

- 响应参数：

```
{
    data: {
        id: '',
    },
    meta: {
        msg: '',        // 请求状态提示
        status: '',    // HTTP Status Code
    }
}
```

#### 路由守卫校验

- 描述：客户端请求 index 等需要授权的页面时，请求服务端校验 token 有效性，作为额外的安全保护措施
- 请求路径：`routeguard`
- 请求方法： `get`
- 请求参数：

```
{}
```

- 响应参数：

```
{
    data: {},
    meta: {
        msg: '',        // 请求状态提示
        status: '',    // HTTP Status Code
    }
}
```

### 用户管理

#### 查看用户资料

- 描述：如题，响应参数为 User 表内除了 passwd 外所有内容
- 请求路径：`userprofile`
- 请求方法： `get`
- 请求参数：

```
{
    id: '',     //not null
}
```

- 响应参数：

```
{
    data: {
    id: '',
    username: '',
    icon_id: '',
    email: '',
    sex: '',        //Boolean
    introduction: '',
    birth: '',
    },
    meta: {
        msg: '',        // 请求状态提示
        status: '',    // HTTP Status Code
    }
}
```

#### 修改用户资料

- 描述：如题，为简化处理并统一请求格式，无论修改多少内容，响应参数一律为除了id、 vipLevel 和 isDev 外， User 表内所有内容
- 请求路径：`userprofile`
- 请求方法： `put`
- 请求参数：

```
{
    username: '',
    passwd: '',
    icon_id: '',
    email: '',
    sex: '',        //Boolean
    introduction: '',
    birth: '',
}
```

- 响应参数：

```
{
    data: {},
    meta: {
        msg: '',        // 请求状态提示
        status: '',    // HTTP Status Code
    }
}
```

#### 注销账号

- 描述：如题，出于安全性考量，会再请求一次 passwd，服务端对 token 和 passwd 做双校验，否则返回 403
- 请求路径：`userprofile`
- 请求方法： `delete`
- 请求参数：

```
{
    id: '',
    passwd: '',
}
```

- 响应参数：

```
{
    data: {},
    meta: {
        msg: '',        // 请求状态提示
        status: '',    // HTTP Status Code
    }
}
```

### 关系管理

#### 添加好友

#### 删除好友

#### 查看好友列表

### 群组管理

#### 创建群组

#### （申请）加入群组

#### 设置管理员

#### 转让群主

#### 查看群组列表
