## 使用说明

1. 在主目录的`json`目录下新建`headers.json`文件，示例内容为：
```json
{
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Cookie": "xxxxxxx"
}
```
2. 第一次运行需要生成json文件，命令为`python main.py 1 y`，其中`1`为表情包编号，第一次运行时随机填，第二个参数`y`表示下载生成json文件
3. 后续运行时只需要执行`python main.py xxxx`，其中`xxxx`是表情包的编号，请参见`json/packages.json`中的index编号，例如262对应星瞳表情包，就可以使用`python main.py 262`