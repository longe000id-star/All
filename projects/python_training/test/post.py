←
←
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域，让浏览器也能正常发送 OPTIONS 预检请求

@app.route('/test', methods=['GET', 'POST', 'OPTIONS'])
def test():
    print("Request received!")
    print("Method:", request.method)
    print("Headers:", dict(request.headers))
    
    if request.method == 'POST':
        # 尝试获取 JSON 数据
        data = request.get_json()
        print("Received JSON data:", data)
        # 返回包含收到数据的响应
        return jsonify({
            "message": "POST request successful!",
            "you_sent": data
        })
    else:
        # GET 或 OPTIONS 请求返回简单消息
        return jsonify({"message": "GET request successful!"})

if __name__ == '__main__':
    app.run(debug=True)