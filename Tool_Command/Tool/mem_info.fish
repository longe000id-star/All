←
#!/usr/bin/env fish

# 获取页面大小（字节）
set pagesize (vm_stat | grep "page size" | awk '{print $8}')

# 总内存（字节）
set total (sysctl hw.memsize | awk '{print $2}')

# 各内存分类的页数（去掉小数点）
set free (vm_stat | grep "Pages free" | awk '{print $3}' | tr -d '.')
set active (vm_stat | grep "Pages active" | awk '{print $3}' | tr -d '.')
set speculative (vm_stat | grep "Pages speculative" | awk '{print $3}' | tr -d '.')
set wired (vm_stat | grep "Pages wired down" | awk '{print $4}' | tr -d '.')
set compressed (vm_stat | grep "Pages occupied by compressor" | awk '{print $5}' | tr -d '.')
set file (vm_stat | grep "File-backed pages" | awk '{print $3}' | tr -d '.')

# 计算应用内存（活跃 + 推测）
set app_pages (math "$active + $speculative")

# 转换为 MB
set app_mb (math "$app_pages * $pagesize / 1024 / 1024")
set wired_mb (math "$wired * $pagesize / 1024 / 1024")
set compressed_mb (math "$compressed * $pagesize / 1024 / 1024")
set file_mb (math "$file * $pagesize / 1024 / 1024")
set free_mb (math "$free * $pagesize / 1024 / 1024")
set total_mb (math "$total / 1024 / 1024")

# 计算已用内存
set used_mb (math "$app_mb + $wired_mb + $compressed_mb + $file_mb")

# 输出结果
echo "==================== 内存详细分类 (MB) ===================="
echo "总物理内存      : $total_mb MB"
echo "已用内存        : $used_mb MB"
echo "├─ 应用内存     : $app_mb MB   (App Memory: 活跃 + 推测页)"
echo "├─ 联动内存     : $wired_mb MB  (Wired: 内核锁定)"
echo "├─ 压缩内存     : $compressed_mb MB (Compressed)"
echo "└─ 文件缓存     : $file_mb MB  (Cached Files)"
echo "空闲内存        : $free_mb MB"
echo "=========================================================="
