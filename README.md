<h1 align="center">
    <img src="https://i.jpg.dog/file/jpg-dog/de6d6ec5db96ba888b4638f2385c0f8c.png" alt="GayChat" width="240">
</h1>
<p align="center">
Simple, elegant web chat application based on <a href="https://socket.io/">Socket.IO</a>.

</p>
<p align="center">
  <a href="https://github.com/Vickko/GayChat/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-WTFPL-brightgreen"></a>
  <a href="https://cn.vuejs.org/"><img src="https://img.shields.io/badge/vue-2.0%2B-blueviolet"></a>
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
 - ~~支持对v佬进行光速开盒~~

## TODO:
1. 添加大致功能需求文档
2. 完善功能需求细分子项


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



