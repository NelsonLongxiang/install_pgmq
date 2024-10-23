install_pgmq 目的是帮助新手在Win平台上安装pgmq插件，减少理解时间，直接上手即可。

## 1、将files里的文件复制到*/PostgreSQL/*/share/extension 目录下

## 2、执行安装python第三方库
```commandline
pip install -r requirements.txt
```

## 请在common.py 指定 postgres_dsn 常量

## 运行脚本
```commandline 
python pgsql_pgmq_extension_install.py
```

## 测试消息队列
```commandline
python test.py
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

### 作者联系方式

1. 作者邮箱：`1169207670@qq.com`
2. Wechat: `1169207670`
