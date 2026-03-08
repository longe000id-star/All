←
# 步骤 1：定义 PrintManager 类
class PrintManager
  def initialize
    @queue = []  # 初始化队列
    puts "PrintManager Initialized!"  # 输出初始化信息
  end
end

# 执行步骤 1 后，会显示：
# PrintManager Initialized!
print_manager = PrintManager.new