←
←
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# 注册路由装饰器，将函数绑定到/test路径，允许GET、POST、OPTIONS方法
@app.route('/test', methods = ['GET', 'POST', 'OPTIONS'])
# 定义test函数处理请求
def test():
    # 在控制台输出"Request received!"，表示收到请求
    print("Request received")
    # 打印客户端请求使用的HTTP方法（GET、POST等）
    print(f"request method: {request.method}")
    # 打印所有HTTP请求头信息，转换为字典格式
    print(f"request headers: {request.headers}")
    # 返回JSON格式的成功响应，包含测试成功的消息
    return jsonify({"message" : "Test is successfully!"})

# 1. methods参数语法错误：methods['GET', 'POST', 'OPTIONS'] 应为 methods=['GET', 'POST', 'OPTIONS']
# 2. 函数定义参数错误：def test(request) 应为 def test()，Flask路由函数不需要显式传入request参数
# 3. Print大写错误：Print 应为 print
# 4. 属性错误：request.methods 应为 request.method
# 5. JSON响应错误：jsonify("Test is sucessfully!") 应为 jsonify({"message": "Test is sucessfully!"})，jsonify通常接收字典对象


from flask import Flask, request, jsonify 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/test", methods = ['GET', 'POST', 'OPTIONS'])
def test():
    print(f"request method: {request.method}")
    print(f"request headers: {request.headers}")
    return jsonify({"message": "Test is successfully!"})