←
←
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# /test 端点现在支持 GET、POST、PUT、OPTIONS
@app.route('/test', methods=['GET', 'POST', 'PUT', 'OPTIONS'])
def test():
    print("Request received!")
    print("Method:", request.method)
    print("Headers:", dict(request.headers))
    
    if request.method == 'POST':
        data = request.get_json()
        print("Received JSON data via POST:", data)
        return jsonify({
            "message": "POST request successful!",
            "you_sent": data
        })
    elif request.method == 'PUT':
        data = request.get_json()
        print("Received JSON data via PUT:", data)
        return jsonify({
            "message": "PUT request successful!",
            "you_sent": data
        })
    else:
        # GET 或 OPTIONS 请求返回简单消息
        return jsonify({"message": "GET request successful!"})

# 表单页面（现在发送 PUT 请求）
@app.route('/form')
def form():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>测试 PUT 请求</title>
    </head>
    <body>
        <h2>提交表单发送 PUT 请求</h2>
        <form id="myForm">
            <input type="text" name="name" placeholder="姓名" value="Alice"><br>
            <input type="number" name="age" placeholder="年龄" value="30"><br>
            <button type="submit">提交</button>
        </form>
        <div id="result"></div>

        <script>
        document.getElementById('myForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData.entries());
            const response = await fetch('/test', {
                method: 'PUT',   // 改为 PUT 请求
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            const result = await response.json();
            document.getElementById('result').innerText = JSON.stringify(result, null, 2);
        });
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)