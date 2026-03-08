←
←
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
        logger.info("Get pronunciation request.")
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
                "status": "No phoneme",
                "message": "No need to correct pronunciation."
            }), 404
    # 如果发生异常，捕获并处理
    except Exception as e:
        # 返回错误状态的JSON响应，包含异常信息，状态码500
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


check_pronunciation
phoneme 
logger.info
hasattr
emotion_service
pronunciation_guide
LanguagePronunciationGuide
pronunciation_guide.language
analysis
analyze_pronunciation
