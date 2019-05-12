### 股票实时提醒功能

#### 1.功能

```
根据config.ini的section来读取对应的股票配置信息，通过调取新浪财经的股票接口获取改股票的实时价格，通过钉钉机器人发送对应的提醒信息。这块增加了股票交易日的判断，如果是非交易日不进行任何提醒。
```

#### 2.代码结构

```
项目入口文件是main.py文件。
condition.py是股票交易日判断模块
dingding.py钉钉机器人发送信息模块，可以更改其webhook配置。
stock.py是获取某只股票的实时信息模块
handleconfig.py读取config.ini配置文件信息模块
stock_ding_remaind.py是我原先写的，把所有功能都写在了一个文件里，没有对模块进行拆分，现暂时保留。
```

#### 3.项目运行

```
pip install -r requirements.txt
python main.py
```

