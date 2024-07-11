# OneOrder

OneOrder 是一个基于 Python 和 FastAPI 的轻量级用户订阅服务管理工具，旨在为小公司提供简单高效的订单和订阅服务管理功能。

## 目录
- [特性](#特性)
- [安装](#安装)
- [使用](#使用)
- [API 文档](#api-文档)
- [文件结构](#文件结构)
- [环境变量](#环境变量)
- [贡献](#贡献)
- [许可证](#许可证)

## 特性
- 用户注册和登录（支持 JWT 验证）
- 管理员和普通用户角色区分
- 订阅服务管理（创建、更新、删除、查看）
- 订单管理（创建、更新、删除、查看）
- 支持多种支付方式（微信、支付宝、PayPal）
- 基于 FastAPI 和 SQLAlchemy 实现
- 提供丰富的 API 接口，方便集成

## 安装

### 前提条件
- Python 3.7+
- Git

### 克隆仓库
```sh
git clone https://github.com/yourusername/one_order.git
cd one_order
```

### 创建虚拟环境并安装依赖
```sh
python -m venv venv
source venv/bin/activate  # 对于 Windows，使用 `venv\Scripts\activate`
pip install -r requirements.txt
```

### 运行应用
```sh
uvicorn app.main:app --reload
```
应用将在 http://127.0.0.1:8000 上运行。

## 使用
### 用户注册
使用 Postman 或 cURL 发送请求来注册新用户：
```sh
curl -X POST "http://127.0.0.1:8000/api/users/" -H "Content-Type: application/json" -d '{
  "username": "testuser",
  "email": "test@example.com",
  "phone": "1234567890",
  "password": "password"
}'
```

### 用户登录
获取访问令牌：
```
curl -X POST "http://127.0.0.1:8000/api/token" -H "Content-Type: application/x-www-form-urlencoded" -d "username=testuser&password=password"
```

### 获取当前用户信息
使用获取的访问令牌：
```sh
curl -X GET "http://127.0.0.1:8000/api/users/me" -H "Authorization: Bearer <your_token>"
```

## API文档
启动应用后，可以通过以下链接查看自动生成的 API 文档：
- [Swagger UI]
- [ReDoc]

## 文件结构
```plaintext
one_order/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── order.py
│   │   └── subscription.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── order.py
│   │   └── subscription.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── order.py
│   │   └── subscription.py
│   └── utils/
│       ├── __init__.py
│       └── security.py
├── requirements.txt
└── README.md
```

## 变量环境
应用程序可能需要一些环境变量来配置，例如数据库连接字符串、秘密密钥等。你可以在项目根目录下创建一个 .env 文件来配置这些变量。
### 示例'.env'文件
```plaintext
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 贡献
我们欢迎任何形式的贡献！请遵循以下步骤参与贡献：

Fork 仓库
1.创建你的特性分支 (git checkout -b feature/awesome-feature)
2.提交更改 (git commit -m 'Add some awesome feature')
3.推送到分支 (git push origin feature/awesome-feature)
4.创建一个新的 Pull Request

## 许可证
该项目使用 MIT 许可证。有关更多信息，请参阅 #LICENSE 文件。

```
这个自述文件详细说明了项目的特性、安装步骤、使用方法、API 文档、文件结构、环境变量和贡献指南，能够帮助用户快速上手并参与项目贡献。请根据实际项目情况进行调整和填写。
```


