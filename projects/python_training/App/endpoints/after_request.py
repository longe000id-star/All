←
←


after_request
log_response
response.status
dict
response.headers
print

# 注册一个在每次请求后执行的钩子函数，用于记录响应信息
@app.route after_request(response)
def log_response:
    # 打印HTTP响应的状态码和状态描述（如"200 OK"）
    print("response status:" response.status)
    # 打印所有的HTTP响应头信息，转换为字典格式便于查看
    print("response headers:" dict(response.headers))
    # 返回响应对象，确保请求-响应循环正常继续
    return ()

@app.after_request(response)
def log_response(response):
    print("response status:", response.status)
    print(f"response status:" {response.status})
    print("response headers:", dict(response.headers))
    print(f"response headers:" {dict(response.headers)})
    return(response)

from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.after_request
def log_response(response):
    print(f"response status: {response.status}")
    print(f"response headers: {dict(response.headers)}")
    return response





from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# 注册一个在每次请求后执行的钩子函数，用于记录响应信息
@app.after_request
def log_response(response):
    # 打印HTTP响应的状态码和状态描述（如"200 OK"）
    print(f"response status: {response.status}") #f-string
    # 打印所有的HTTP响应头信息，转换为字典格式便于查看
    print("response status:", response.status)
    print(f"response headers: {dict(response.headers)}")
    print("response headers:", response.headers)
     # 返回响应对象，确保请求-响应循环正常继续
    return response


# 完整的 import.py  log.py after_request


    
    
   
