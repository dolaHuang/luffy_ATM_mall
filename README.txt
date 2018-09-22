1.本程序功能全部用python的基础知识实现
	用到了time\datetime\os\sys\json\with open\logging\函数\模块知识

2.程序功能
	1.程序有两个主要功能
		1.购物商城，可以进行选择商品并调用ATM进行支付
		2.ATM银行，可以进行提现，转账，查看账户，还款等操作，并支持管理接口
3.home.py 为程序启动文件
	1.ATM银行管理员账户admin 密码admin
	2.商城账号alex 密码1234
	3.ATM银行已注册账号111111 ，888888 ，777777 ， 密码1234

4.程序目录结构：

└─luffy_atm_mall
    │  atm-flow.png   程序流程图
    │  home.py        程序启动文件
    │  README.txt 
    │  __init__.py
    │  
    ├─.idea
    │      luffy_atm_mall.iml
    │      misc.xml
    │      modules.xml
    │      workspace.xml
    │      
    ├─atm
    │  │  __init__.py
    │  │  
    │  ├─bin
    │  │  │  atm.py     ATM 入口
    │  │  │  manage.py  ATM 管理模块
    │  │  │  __init__.py
    │  │  │  
    │  │  └─__pycache__
    │  │          atm.cpython-37.pyc
    │  │          manage.cpython-37.pyc
    │  │          __init__.cpython-37.pyc
    │  │          
    │  ├─conf     配置文件  
    │  │  │  setting.py    程序设置模块
    │  │  │  __init__.py
    │  │  │  
    │  │  └─__pycache__
    │  │          setting.cpython-37.pyc
    │  │          __init__.cpython-37.pyc
    │  │          
    │  ├─core	 程序逻辑目录
    │  │  │  admin_func.py		程序管理员
    │  │  │  auth.py			认证用户模块
    │  │  │  db_handler.py		连接账户数据，序列化和反序列化
    │  │  │  decorator.py		装饰器
    │  │  │  logger.py			记录日志模块
    │  │  │  logics.py			ATM主要功能
    │  │  │  main.py			主函数，功能逻辑交互
    │  │  │  message_utils.py	打印消息工具
    │  │  │  transaction.py		交易中心模块，实现账户金额计算
    │  │  │  __init__.py
    │  │  │  
    │  │  └─__pycache__
    │  │          admin_func.cpython-37.pyc
    │  │          auth.cpython-37.pyc
    │  │          db_handler.cpython-37.pyc
    │  │          decorator.cpython-37.pyc
    │  │          logger.cpython-37.pyc
    │  │          logics.cpython-37.pyc
    │  │          main.cpython-37.pyc
    │  │          message_utils.cpython-37.pyc
    │  │          transaction.cpython-37.pyc
    │  │          __init__.cpython-37.pyc
    │  │          
    │  ├─db   账户数据目录
    │  │  │  __init__.py
    │  │  │  
    │  │  └─accounts		账户数据目录
    │  │          111111.json
    │  │          555555.json
    │  │          666666.json
    │  │          777777.json
    │  │          888888.json
    │  │          999999.json
    │  │          admin.json
    │  │          __init__.py
    │  │          
    │  ├─logs		ATM操作日志
    │  │      access.log				账户操作日志
    │  │      admin_management.log		管理员操作日志
    │  │      transactions.log			交易日志
    │  │      __init__.py
    │  │      
    │  └─__pycache__
    │          __init__.cpython-37.pyc
    │          
    └─shopping_mall       商城目录
        │  __init__.py
        │  
        ├─bin		
        │  │  shopping_mall.py    商城逻辑入口
        │  │  __init__.py
        │  │  
        │  └─__pycache__
        │          shopping_mall.cpython-37.pyc
        │          __init__.cpython-37.pyc
        │          
        ├─conf		商城配置文件
        │  │  setting_mall.py      商城代码设置内容
        │  │  __init__.py
        │  │  
        │  └─__pycache__
        │          setting_mall.cpython-37.pyc
        │          __init__.cpython-37.pyc
        │          
        ├─core     主要逻辑目录
        │  │  auth_mall.py				账户认证
        │  │  check_out_mall.py			账户结算接口
        │  │  decorator_mall.py			装饰器
        │  │  main.py					商城
        │  │  __init__.py
        │  │  
        │  └─__pycache__
        │          auth_mall.cpython-37.pyc
        │          check_out_mall.cpython-37.pyc
        │          decorator_mall.cpython-37.pyc
        │          main.cpython-37.pyc
        │          __init__.cpython-37.pyc
        │          
        ├─db   账户数据
        │  │  __init__.py
        │  │  
        │  └─account		
        │          alex.json  单个账户数据
        │          __init__.py
        │          
        ├─logs	商城操作日志
        │      access_mall.log
        │      transactions_mall.log
        │      __init__.py
        │      
        └─__pycache__
                __init__.cpython-37.pyc
                
