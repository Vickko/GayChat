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