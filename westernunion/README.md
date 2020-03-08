# westernunion-crawler
## 目录结构
```
westernunion
│   README.md
│   westernunion.py      # 用于爬取数据
│   data_preprocessing.py   # 用于处理数据
│   data.csv  # 代码生成
│   westernunion.csv  # 代码生成
```
## 怎么运行
### 关于环境
最主要的是安装selenium，以及webdriver。可参考[Link](https://blog.csdn.net/qq_41188944/article/details/79039690)，亦可自行谷歌。

### 运行步骤
* 运行`westernunion.py`，对网站进行爬取，生成`data.csv`
* 运行`data_preprocessing.py`，上述爬取完成后，需要对`data.csv`的数据进行处理，生成`westernunion.csv`

### 主要的参数
* start_id = 0   #如果出错了，从这里开始爬取。在`westernunion.py` 的196行。
在爬取的时候可能出现网络连不上的情况，这时便会出错，并停止运行。界面会print出一些可视化，形如No.(id)(contry)，意思是爬取到该id的国家，当出错时，需要改此参数，把已爬取的id赋值给start_id，这时便可从第(id)个国家开始爬取，数据会对`data.csv`进行追加续写，共约240个国家。

### 最后说明
* 如果在国内，建议使用vpn或者ssr开全局模式。
* 弹出的谷歌浏览器可以移动、最小化，但不要管*开发者模式*这个提示。