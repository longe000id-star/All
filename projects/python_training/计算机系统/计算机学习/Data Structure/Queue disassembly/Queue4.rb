←
# 步骤 4：定义私有的 print 方法来处理打印文档
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
  
    # 执行打印任务
    def run
      while @queue.any?
        document = @queue.shift
        print(document)  # 调用私有打印方法
      end
    end
  
    private
  
    # 模拟打印文档的方法
    def print(document)
      puts "Printing: #{document}"  # 打印文档到终端
    end
  end
  
  # 创建 PrintManager 实例并添加任务
  print_manager = PrintManager.new
  print_manager.queue_print_job("First Document")
  print_manager.queue_print_job("Second Document")
  
  # 执行打印任务
  print_manager.run
  