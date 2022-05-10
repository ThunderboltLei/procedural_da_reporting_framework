### 编程式 DA 报告生成及展示平台
```text
基于 streamlit & python 脚本，快速编写数据分析报告，实现分析报告动态化、多样式等处理。意在两点：
1、打破传统 DA 报告模式
2、突出 DA / DS 分析能力及开发能力
```

#### 一、背景
```text
目前，业界 DA 平台特点：
1、多为图表展示，扁平化展示，样式单调且固定
2、平台开发需要人数过多，前端、后端、DA、DS至少10人以上，配合难度大。
3、无法体现 DA 或 DS 的技术能力
```

#### 二、特点
```text
1、快速编写 DA 报告
2、程序设计式，充分体现 DA 分析师能力
3、基于 Python 语言开发 DA 报告，直接展示，无需前端和后端开发的配合。
4、动态化展示，提交 DA 分析脚本，即可展示分析报告。
5、DA或DS控制展示样式，显示不拘于一格、不形于一态、不定于一尊
6、此框架样例开发仅本人一人天即完成。
```

#### 三、开发
```text
1、使用此平台，只需要根据样例脚本进行编写即可，参考此项目 scripts/demo/my_script_01.py 脚本编辑模式。
2、将开发后脚本上传平台后，便会立刻展示。
```

#### 四、运行
```text
1、运行命令： streamlit run <路径>/app.py
2、数据文件在 data 目录下
3、scripts 目录：
（1）样例脚本存放在 demo 目录下
（2）正式脚本存放在 formal 目录下
4、DB信息配置文件：.streamlit/secrets.toml                                                  
[mysql]
host = "10.72.105.44"
port = 3306
database = "demo"
user = "anonymous"
password = "anonymous"
```

#### 五、待完善
```
1、完善平台框架
2、支持多数据源，如 Hive, PostgreSQL 等
3、提供 SDK 及 API 服务
<<< 程序完善中 >>>
```

样式截图：
![image](https://github.com/ThunderboltLei/procedural_da_reporting_framework/blob/main/data/p_da_r_f_01.png)
![image](https://github.com/ThunderboltLei/procedural_da_reporting_framework/blob/main/data/p_da_r_f_02.png)
![image](https://github.com/ThunderboltLei/procedural_da_reporting_framework/blob/main/data/p_da_r_f_03.png)
