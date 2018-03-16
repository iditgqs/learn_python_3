## mongodb安装与使用
#### 安装
1. tar 解压
2. PATH环境变量 export PATH=$PATH:/usermongodbbin
3. mongod.conf:
    ```
        # 数据文件
        dbpath=/home/gqs/.local/share/mongodb/data/db

        # 日志文件
        logpath=/home/gqs/.local/share/mongodb/data/log/mongo.log

        # 错误日志采用追加模式，配置这个选项后mongodb的日志会追加到现有的日志文件，而不是从新创建一个新文件
        logappend=true

        # 启用日志文件，默认启用
        journal=true

        # 这个选项可以过滤掉一些无用的日志信息，若需要调试使用请设置为false
        quiet=false

        # 端口号 默认为27017，注意这里端口修改为9888后，要用mongo --port=9888连接，否则报错。
        port=27017
    ```
4. mongod --config mongod.conf &  ------->server启动
5. mongo ----->client连接
