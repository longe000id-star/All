←
←
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域，让浏览器也能正常发送 OPTIONS 预检请求

@app.route('/test', methods=['GET', 'POST', 'OPTIONS'])
def test():
    # 这些 print 会输出到运行 Flask 的终端窗口
    print("Request received!")
    print("Method:", request.method)
    print("Headers:", dict(request.headers))
    
    # 返回一个 JSON 响应
    return jsonify({"message": "Test successful!"})

if __name__ == '__main__':
    app.run(debug=True)