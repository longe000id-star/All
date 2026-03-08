←
class PrintManager
    # 初始化方法，定义一个空的队列来存储待打印的文档
    def initialize
      @queue = [] # 用于存放打印任务的队列
    end
  
    # 将打印任务添加到队列中
    def queue_print_job(document)
      @queue.push(document) # 将文档加入队列
    end
  
    # 执行打印任务，直到队列为空
    def run
      while @queue.any? # 当队列中还有任务时
        print(@queue.shift) # 从队列中移除并打印第一个文档
      end
    end
  
    private
  
    # 私有方法，用来打印文档（此处模拟打印，实际情况可能是打印机设备）
    def print(document)
      puts document # 打印文档到终端
    end
  end
  
  # 创建PrintManager实例
  print_manager = PrintManager.new
  
  # 将文档添加到打印队列中
  print_manager.queue_print_job("First Document")
  print_manager.queue_print_job("Second Document")
  print_manager.queue_print_job("Third Document")
  
  # 执行打印操作
  print_manager.run
  