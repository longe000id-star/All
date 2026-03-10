---
cssclasses:
  - oup-modern-large
---


[← Terminal_Index](../all_index/Terminal_Index.md)

1. 验证和登录Cline的时候，需要清除和关闭电脑上所有的代理 proxy

```fish

set -x http_proxy http://proxy.example.com:8080
set -x https_proxy http://proxy.example.com:8080
set -x all_proxy http://proxy.example.com:8080
set -x HTTP_PROXY http://proxy.example.com:8080
set -x HTTPS_PROXY http://proxy.example.com:8080
set -x ALL_PROXY http://proxy.example.com:8080

set -gx http_proxy http://127.0.0.1:7890
set -gx https_proxy http://127.0.0.1:7890
set -gx all_proxy socks5://127.0.0.1:7890
```

2. 然后就是重新加载fish
```fish
exec fish
```


[← Terminal_Index](../all_index/Terminal_Index.md)

###### Backup
```markdown
[← Terminal_Index](../all_index/Terminal_Index.md)
```