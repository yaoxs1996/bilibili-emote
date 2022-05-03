## 使用说明

1. 在`main.py`的`headers`变量中填入自己的b站cookie
2. 首先单独运行一次`main.py`中的`getPanelJson`方法，生成`panel.json`文件
3. 运行一次`process_json.py`生成`packages.json`文件
4. 运行主函数，`python main.py 123`，其中“123”为`packages.json`中的index编号