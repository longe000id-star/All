←
←
# 检查是否直接运行此脚本（而非被导入）
if __name__ == '__main__':
    # 创建新线程用于运行Flask应用
    # 设置线程目标函数为启动Flask服务器，监听所有网络接口的8000端口，关闭调试模式
     flask_thread = threading.Thread(
        target=lambda: app.run(host="0.0.0.0", port=8000, debug=False)
     )
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

flask_thread
threading.Thread
target=lambda
daemon
run_video_display
finally
stop
