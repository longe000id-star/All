---
cssclasses:
  - oup-modern-large
---

←
←
# RESTful API 设计测试题

> 该测试跟python字典数据结构密切相关. 需要对字典数据结构进行训练，然后才继续完成这个测验。

## 一、选择题

1. **RESTful API 的核心思想是什么？** (A)

   A. 用 URL 表示资源，用 HTTP 方法表示对资源的操作  
   B. 用 URL 表示操作，用 HTTP 方法表示资源  
   C. 用 URL 和 HTTP 方法都表示资源  
   D. 用 URL 和 HTTP 方法都表示操作

2. **以下哪个 URL 设计最符合 RESTful 风格？** (D)

   A. `/get_user?id=123`  
   B. `/users/123`  
   C. `/user?id=123`  
   D. `/api/getUser/123`

3. **要创建一个新的资源，应该使用哪个 HTTP 方法？** (A)

   A. GET  
   B. PUT  
   C. POST  
   D. DELETE

4. **要更新一个已存在的资源，应该使用哪个 HTTP 方法？** (A)

   A. POST  
   B. PUT  
   C. PATCH  
   D. GET

5. **以下哪个状态码表示"资源未找到"？** (B)

   A. 200  
   B. 404  
   C. 500  
   D. 401

## 二、代码实操题

### 任务1：创建用户管理 API
基于你现有的 Flask 应用，创建一个简单的用户管理系统。要求：

1. **创建用户列表存储**（在内存中）
   ```python
   users = [
       {"id": 1, "name": "Alice", "email": "alice@example.com"},
       {"id": 2, "name": "Bob", "email": "bob@example.com"}
   ]
   ```

2. **实现以下 RESTful 端点**：

   - **GET /api/users**：获取所有用户列表
     - 返回：`{"users": [...], "total": 2}`
     - 状态码：200

   - **GET /api/users/<id>**：获取指定ID的用户
     - 成功：返回用户信息，状态码200
     - 失败：返回 `{"error": "User not found"}`，状态码404

   - **POST /api/users**：创建新用户
     - 请求体：`{"name": "Charlie", "email": "charlie@example.com"}`
     - 返回：`{"message": "User created", "user": {...}}`，状态码201
     - 要求：name 和 email 字段不能为空，否则返回400错误

   - **PUT /api/users/<id>**：更新用户信息
     - 请求体：`{"name": "Updated Name", "email": "new@example.com"}`
     - 成功：返回更新后的用户信息，状态码200
     - 失败：返回404错误

   - **DELETE /api/users/<id>**：删除用户
     - 成功：返回 `{"message": "User deleted"}`，状态码200
     - 失败：返回404错误

3. **测试要求**：
   - 使用 curl 命令测试每个端点
   - 验证正确的 HTTP 方法、状态码和返回数据

```python
from flask import Flask, request, jsonify
app = Flask(__name__)
users = [
  {"id": 1, "name": "Alice", "email": "alice@example.com"}
  {"id": 2, "name": "Bob", "email": "bob@example.com"}
]
@app.route("/api/users", methods=['GET'])
def get_users():
  return jsonify({
    "users": users,
    "total": 2
  }), 200

@app.route("/api/users/<id>, methods=['GET']")
def id():
  data = requst.get_json()
  id = data.get('id', 1)
  return jsonify({
    "info" ; users[(int(id)-1)],
  })
except Exception as e:
  return jsonify({
    "status": "error",
    "message": "User not found."
  }), 500

@app.route("/api/user, methods=['POST']")
def create_user:
  new_user = request.get_json()
  new_user['id'] = 3
  if new_user['name'] and new_user['email'] is None:
    return jsonify({
      "message": "error"
    }), 400
  users.append(new_user)
  return jsonify({
  "message": "User created",
  "user": users
  }), 201

@app.route("/api/users/id", methods=['POST'])
def update_user():
  data = request.get_json()
  update_name = data.get('name')
  ❌ 关键这里都没有指明是谁，而且也没有id, 怎么确定更新目标呢？

@app.route("api/users/id", methods=['GET'])
def delete_user():
  data = request.get_json()
  if data
  ❌ 关键这里也没有不知道前端发来什么请求？是删除哪一个id吗？
关键这里我还是不知道

```

**示例测试命令**：
```bash
# 获取所有用户
curl -X GET http://localhost:8000/api/users

# 创建新用户
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "David", "email": "david@example.com"}'

# 获取特定用户
curl -X GET http://localhost:8000/api/users/1

# 更新用户
curl -X PUT http://localhost:8000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Updated", "email": "alice.new@example.com"}'

# 删除用户
curl -X DELETE http://localhost:8000/api/users/1
```

### 任务2：添加数据验证和错误处理
在任务1的基础上，添加更完善的验证和错误处理：

1. **邮箱格式验证**：使用简单的正则表达式验证邮箱格式
> 这里的简单的正则表达式是什么意思呢？我不是很明白？ 
2. **ID 格式验证**：确保 ID 
> 不是啊，前面几道题的的请求，压根就没有有关与id的request啊
3. **重复数据检查**：创建用户时检查邮箱是否已存在
这里可能就是：
```python
new_user = request.get_json()
email = new_user['email']
if email:
  new_user['id] = 3
  users.append(new_user)
  return jsonify({
    "message": "Create new user!",
    "user": users
  }), 200
else:
  return jsonify({
    "message": "email doesnt exist!"
  }), 500

```
4. **统一错误响应格式**：所有错误都使用统一的格式

**预期的错误响应格式**：
```json
{
  "error": "Invalid email format",
  "status": 400
}
```

### 任务3：添加分页功能
为 `GET /api/users` 端点添加分页支持：

- 支持查询参数：`?page=1&limit=10`
- 返回格式：
  ```json
  {
    "users": [...],
    "pagination": {
      "current_page": 1,
      "total_pages": 3,
      "total_items": 25,
      "items_per_page": 10
    }
  }
  ```

**测试命令**：
```bash
# 获取第2页，每页5条
curl -X GET "http://localhost:8000/api/users?page=2&limit=5"
```

## 三、思考题

1. **为什么 RESTful API 要使用名词而不是动词来设计 URL？**

>答：不是很清楚.

2. **GET 和 POST 方法的主要区别是什么？在什么情况下应该使用哪个？**

> 答：GET 方法是获取资源，而POST方法则是提交资源。比如我们想获取前端的request的数据的话，那么需要使用到GET，但如果我们想更新数据的话，需要POST

3. **状态码 200、201、400、404、500 分别代表什么含义？**
> 200,返回成功。201不知道。400跟数据错误有关，而404则是缺少数据。500跟其他很多的错误都有关比如网络错误，代码错误等。
4. **在实际项目中，为什么要进行数据验证？不验证会有什么风险？**

> 不清楚。
5. **分页功能为什么重要？如果不分页会有什么问题？**
> 不清楚。

## 四、进阶挑战

### 任务4：添加身份验证
为你的用户管理 API 添加简单的身份验证：

1. 创建一个"管理员"用户，拥有所有权限
2. 普通用户只能查看自己的信息
3. 只有管理员可以创建、更新、删除用户
4. 使用请求头传递简单的 token 进行身份验证

❌
**测试命令**：
```bash
# 以管理员身份创建用户
curl -X POST http://localhost:8000/api/users \
  -H "Authorization: Bearer admin_token" \
  -H "Content-Type: application/json" \
  -d '{"name": "Eve", "email": "eve@example.com"}'

# 以普通用户身份查看自己信息
curl -X GET http://localhost:8000/api/users/1 \
  -H "Authorization: Bearer user_token"
```

**提示**：可以先在代码中硬编码几个测试用的 token，后续可以学习 JWT 等更安全的认证方式。