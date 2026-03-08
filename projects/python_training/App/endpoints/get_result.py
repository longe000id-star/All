←
←
# 注册路由装饰器，将函数绑定到/api/monitor/result路径，只允许GET方法
@app.route("/api/monitor/result", methods = ['GET'])
# 定义get_result函数获取情绪监控结果
def get_result():
    # 尝试执行以下代码块，捕获可能发生的异常
    try:
        # 调用情绪监控服务的get_dominant_emotion方法获取主导情绪数据
        emotion_data = emotion_service.get_dominant_emotion()
        # 待办：可以通过检测中性、惊讶和愤怒等情绪来使混淆指标更敏感
        # # 如果有情绪数据，继续处理
        if emotion_data:
            # 定义需要跟进的情绪类型及其阈值（中性0.7、惊讶0.6、恐惧0.5、悲伤0.5）
            confusion_indicator = {
                "neutral": 0.7,
                "surprise": 0.6,
                "fear": 0.5,
                "sad": 0.5
            }
            # 判断是否需要跟进：情绪在字典中且分数超过对应阈值
            needs_followup = emotion_data['emotion'] in confusion_indicator and emotion_data['score'] > confusion_indicator[emotion_data['emotion']]
            # 返回成功状态的JSON响应，包含情绪数据和是否需要跟进标志，状态码200
            return jsonify({
                "status": "Success",
                "data": {
                    "emotion": emotion_data,
                    "followup": needs_followup
                }
            }), 200
        # 如果没有情绪数据
        else:
            # 返回错误状态的JSON响应，提示无情绪数据可用，状态码404
            return jsonify({
                "status": "No emotions.",
                "message": " No need to followup."
            }), 404

    # 如果发生异常，捕获并处理
    except Exception as e:
        # 返回错误状态的JSON响应，包含异常信息，状态码500
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

get_result
emotion_data
get_dominant_emotion
confusion_indicators
needs_follwoup
score

