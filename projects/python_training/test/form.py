←
←
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 原来的 /test 端点不变
@app.route('/test', methods=['GET', 'POST', 'OPTIONS'])
def test():
    print("Request received!")
    print("Method:", request.method)
    print("Headers:", dict(request.headers))
    
    if request.method == 'POST':
        data = request.get_json()
        print("Received JSON data:", data)
        return jsonify({
            "message": "POST request successful!",
            "you_sent": data
        })
    else:
        return jsonify({"message": "GET request successful!"})

# 新增：提供一个简单的表单页面
@app.route('/form')
def form():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>测试 POST 请求</title>
    </head>
    <body>
        <h2>提交表单发送 POST 请求</h2>
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
                method: 'POST',
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