←
←
# 创建Flask应用实例，__name__表示当前模块的名称
# 为Flask应用启用CORS（跨域资源共享），允许其他域的请求访问这个应用
# 创建情绪监控服务实例，用于处理摄像头视频流和情绪识别

app = Flask(__name__)
CORS(app)
emotion_service = EmotionMonitorService()
