## 项目结构
```
ecommerce_data_analysis/
├── data/   # 生成的模拟数据
│ ├── behaviors.csv
│ ├── campaigns.csv
│ ├── items.csv
│ ├── orders.csv
│ ├── users.csv
│ └── sale_datas.db  # sqlite数据库，包含上述5个csv表的数据
├── 模拟数据生成脚本.ipynb
├── scripts/ # 脚本形式的处理代码
│ ├── bi主题设置/    # powerbi所用主题背景
│ ├── RFM_data/
│ │  └── RFM分析表.xlsx
│ ├── RFM分析测试代码.ipynb
│ ├── RFM数据表生成脚本.py    # （同RFM分析测试代码.ipynb）
│ └── 用户价值分析报表.pbix    # 分析报表
└── README.md # 项目介绍
```
