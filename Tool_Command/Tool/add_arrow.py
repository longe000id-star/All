←
#!/usr/bin/env python3
import os

# 要处理的文件扩展名
extensions = ('.sh', '.md', '.py', '.txt', '.json', '.yml', '.yaml', '.csv', '.js', '.html', '.css')

root_dir = '/Users/longe/Desktop/All'

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(extensions):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('←\n' + content)
                print(f"✓ {filepath}")
            except Exception as e:
                print(f"✗ {filepath}: {e}")
