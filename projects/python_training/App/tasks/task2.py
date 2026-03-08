←
←
from flask import Flask, request, jsonify
# agent.emotion_monitor: EmotionMonitorService LanguagePronunciationGuide
from agent.emotion_monitor import EmotionMonitorService, LanguagePronunciationGuide
# agent.translation:
from agent.translation import *

app = Flask(__name__)

# 注册路由装饰器，将函数绑定到/api/translation路径，只允许POST方法
@app.route("/api/translation", methods = ['POST'])
# 定义generate_llm_translation函数处理翻译请求
def generate_llm_translation():
    # 使用Claude AI生成用户想学习的内容的翻译
    # 待办：修改字段名以匹配正确的字段名称
    # 尝试执行以下代码块，捕获可能发生的异常
    # 从请求中解析JSON数据
    try:
        data = request.get_json()
    # 从JSON中获取'prompt'字段，默认值为"Hello"
        prompt = data.get('prompt')
    # 从JSON中获取'language'字段，默认值为"French"
        language = data.get('language', "French")
    # 调用翻译生成函数，获取AI生成的翻译文本
        
        if prompt:
            # 返回成功状态的JSON响应，包含翻译结果，状态码200
            response = generate_translation_response(prompt, language)[0].text
            return jsonify({
                "status": "Success.",
             "message": response
            }), 200
        else:
            return jsonify({
                "error": "Missing prompt"
            }), 400
# 如果发生异常，捕获并处理
    except Exception as e:
    # 返回错误状态的JSON响应，包含错误信息，状态码500
        return jsonify({
            "status": "Failed",
            "message": "Failed to generate translation"
        }), 500

if __name__ == "__main__":
    app.run(port=8000)
