←
←
# 注册路由装饰器，将函数绑定到/api/monitor/start路径，只允许POST方法
@app.route("/api/monitor/start", methods = ['POST'])
# 定义start_monitoring函数处理情绪监控启动请求
def start_monitoring():
    # 尝试执行以下代码块，捕获可能发生的异常
    try:
        # 从请求中解析JSON数据
        data = request.get_json()
        # 从JSON中获取'duration'字段（监控时长），转换为浮点数，默认5.0秒
        duration = float(data.get('duration', 5.0))
        # 如果启动成功，返回成功状态的JSON响应，包含启动成功的消息和时长
        if emotion_service.start_monitoring(duration):
            return jsonify({
                "status": "successful!",
                "message": f"Started monitoring {duration} seconds."
            }), 200
        # 如果启动失败，返回错误状态的JSON响应，包含失败信息，状态码500
        else:
            return jsonify({
                "status": "error",
                "message": "Failed to start"
            }), 500
    # 如果发生异常，捕获并处理
    except Exception as e:
        # 返回错误状态的JSON响应，包含异常信息，状态码500
        return jsonify({
            "status": "error",
            "message": "Failed to start"
        }), 500

start_monitoring
duration
float
emotion_service
