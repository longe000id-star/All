←
# 步骤 2：定义添加打印任务的方法
class PrintManager
    def initialize
      @queue = []  # 初始化队列
      puts "PrintManager Initialized!"  # 输出初始化信息
    end
  
    # 将打印任务加入队列
    def queue_print_job(document)
      @queue.push(document)  # 将打印任务加入队列
      puts "Queued: #{document}"  # 输出队列信息
    end
  end
  
  # 创建 PrintManager 实例并添加任务
  print_manager = PrintManager.new
  print_manager.queue_print_job("First Document")
  print_manager.queue_print_job("Second Document")
  
