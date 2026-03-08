←
←
# app.py
from flask import Flask, jsonify

app = Flask(__name__)

# 这是一个普通的视图函数，处理 GET 请求
@app.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

# after_request 钩子函数：在每次请求处理完成后自动执行
@app.after_request
def log_response(response):
    # 打印响应状态码
    print(f"Response Status: {response.status}")
    # 打印响应头（转换为字典方便查看）
    print(f"Response Headers: {dict(response.headers)}")
    # 可以在这里修改响应，比如添加一个自定义头
    response.headers['X-Custom-Header'] = 'Added by after_request'
    # 必须返回 response 对象，否则请求会挂起
    return response

if __name__ == '__main__':
    app.run(debug=True)