←
←

# flask: Flask  request jsonify
from flask import Flask, request, jsonify

#flask_cors: CORS
from flask_cors import CORS

# agent.emotion_monitor: EmotionMonitorService LanguagePronunciationGuide
from agent.emotion_monitor import EmotionMonitorService, LanguagePronunciationGuide

# agent.translation:
from agent.translation import *

# threading
import threading

# logging
import logging

# time
import time

# 创建Flask应用实例，__name__表示当前模块的名称
app = Flask(__name__)

# 为Flask应用启用CORS（跨域资源共享），允许其他域的请求访问这个应用
CORS(app)

# 创建情绪监控服务实例，用于处理摄像头视频流和情绪识别
emotion_service = EmotionMonitorService()

# 配置整个日志系统的基础设置，包括根记录器的级别为DEBUG
logging.basicConfig(level=logging.DEBUG)

# 获取一个日志记录器对象，赋值给变量logger供后续使用
logger = logging.getLogger()

# 将这个logger对象的级别手动设置为DEBUG，确保它能记录调试信息
logger.level = logging.DEBUG

# 注册一个在每次请求后执行的钩子函数，用于记录响应信息
@app.after_request
def log_response(response):

    # 打印HTTP响应的状态码和状态描述（如"200 OK"）
    print(f"response status: {response.status}")

    # 打印所有的HTTP响应头信息，转换为字典格式便于查看
    print(f"response headers: {dict(response.headers)}")

    # 返回响应对象，确保请求-响应循环正常继续
    return response

@app.route("/api/translation", methods = ['POST'])
def generate_llm_translation():
    try:
        data = request.get_json()
        prompt = data.get('prompt', "Hello")
        language = data.get('language', "French")
        response = generate_translation_response(prompt, language)[0].text
        return jsonify({
            "status": "Successful!",
            "message": response
        }), 200
    except Exception as e:
        return jsonify({
            "status": "Failed",
            "message": "Failed to generate message"
        }), 500

# 注册路由装饰器，将函数绑定到/api/followup路径，只允许POST方法
@app.route("/api/followup", methods = ['POST'])
# 定义generate_followup函数处理跟进对话请求
def generate_followup():
    # 尝试执行以下代码块，捕获可能发生的异常
    try:
        # 在控制台打印请求对象信息，用于调试
        print(request)
        # 从请求中解析JSON数据
        data = request.get_json()
        # 从JSON中获取'prev'字段（之前的对话内容），默认值为空字符串
        prev = data.get('prev', "")
        # 调用跟进回复生成函数，根据先前对话内容生成AI回复
        response = generate_followup_response(prev)[0].text
        # 返回成功状态的JSON响应，包含生成的跟进回复，状态码200
        return jsonify({
            "status": "success",
            "message": response
        }), 200
    # 如果发生异常，捕获并处理
    except Exception as e:
        # 返回错误状态的JSON响应，包含错误信息，状态码500
        return jsonify({
            "status": "error",
            "message": "Failed to generate the translation."
        }), 500



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
                "status": "success",
                "message": f"Monitor has started {duration} seconds."
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
            "message": str(e)
        }), 500



# 注册路由装饰器，将函数绑定到/api/monitor/result路径，只允许GET方法
@app.route("/api/monitor/result", methods = ['GET'])
# 定义get_result函数获取情绪监控结果
def get_result():
    # 尝试执行以下代码块，捕获可能发生的异常
    try:
        # 调用情绪监控服务的get_dominant_emotion方法获取主导情绪数据
        emotion_data = emotion_service.get_dominant_emotion()
        # 待办：可以通过检测中性、惊讶和愤怒等情绪来使混淆指标更敏感
        # 如果有情绪数据，继续处理
        if emotion_data:
            # 定义需要跟进的情绪类型及其阈值（中性0.7、惊讶0.6、恐惧0.5、悲伤0.5）
            confusion_indicators = {
                "neutral": 0.7,
                "surprise": 0.6,
                "fear": 0.5,
                "sad": 0.5
            }
            # 判断是否需要跟进：情绪在字典中且分数超过对应阈值
            needs_followup = emotion_data['emotion'] in confusion_indicators and emotion_data['score'] > confusion_indicators[emotion_data['emotion']]
            # 返回成功状态的JSON响应，包含情绪数据和是否需要跟进标志，状态码200
            return jsonify({
                "status": "success",
                "data":{
                    "emotion": emotion_data,
                    "followup": needs_followup
                }
            }), 200
        # 如果没有情绪数据
        else:
            # 返回错误状态的JSON响应，提示无情绪数据可用，状态码404
            return jsonify({
                "status": "No available emotion",
                "message": "No need to follow up"
            }), 404
    # 如果发生异常，捕获并处理
    except Exception as e:
    # 返回错误状态的JSON响应，包含异常信息，状态码500
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# 注册路由装饰器，将函数绑定到/api/monitor/pronunciation路径，只允许POST方法
@app.route("/api/monitor/pronunciation", methods = ['POST'])
# 定义check_pronunciation函数处理特定语言中特定音素的发音检测请求
def check_pronunciation():
    # 注意：请求过多可能导致段错误，需小心处理
    # 尝试执行以下代码块，捕获可能发生的异常
    try:
        # 从请求中解析JSON数据
        data = request.get_json()
        # 从JSON中获取'phoneme'字段（要检测的音素），默认值为空字符串
        phoneme = data.get('phoneme', "")
        # 从JSON中获取'language'字段（目标语言），默认值为"french"
        language = data.get('language', "french")
        # 记录INFO级别日志，表示已解析发音请求
        logger.info("get the requet")
        # 如果情绪监控服务没有发音指南属性，创建新的发音指南实例
        if not hasattr(emotion_service, 'pronunciation_guide'):
            emotion_service.pronunciation_guide = LanguagePronunciationGuide(language)
        # 如果已有发音指南但语言不匹配，重新创建对应语言的发音指南实例
        elif emotion_service.pronunciation_guide.language != language:
            emotion_service.pronunciation_guide = LanguagePronunciationGuide(language)
        # 记录INFO级别日志，表示已创建发音指南
        logger.info("create pronunciation_guide")
        # 调用情绪监控服务的analyze_pronunciation方法分析发音，获取分析结果
        analysis_result = emotion_service.analyze_pronunciation(phoneme)
        # 从分析结果中提取反馈信息
        feedback = analysis_result.get('feedback')
        # 如果有分析结果，返回成功状态的JSON响应，包含发音反馈，状态码200
        if analysis_result:
            return jsonify({
                "status": "success",
                "feedback": feedback
            }), 200
        # 如果没有分析结果，返回错误状态的JSON响应，提示无发音数据可用，状态码404
        else:
            return jsonify({
                "status": "No data",
                "message": "No pronunciation is needed to correct."
            }), 404
    # 如果发生异常，捕获并处理
    except Exception as e:
        # 返回错误状态的JSON响应，包含异常信息，状态码500
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# 检查是否直接运行此脚本（而非被导入）
if __name__ == "__main__":
    # 创建新线程用于运行Flask应用
    flask_thread = threading.Thread(
        target=lambda: app.run(host="0.0.0.0", port=8000, debug=False)
    )
    # 设置线程目标函数为启动Flask服务器，监听所有网络接口的8000端口，关闭调试模式
    # 将线程设置为守护线程，主线程退出时自动结束
    flask_thread.daemon = True
    # 启动Flask线程
    flask_thread.start()
    # 在主线程中运行OpenCV视频显示
    # 尝试执行视频显示，捕获可能发生的异常
    try:
        # 调用情绪监控服务的run_video_display方法运行视频显示循环
        emotion_service.run_video_display()
    # 无论是否发生异常，最终都会执行清理代码
    finally:
        # 调用情绪监控服务的stop方法停止视频捕获并释放资源
        emotion_service.stop()

