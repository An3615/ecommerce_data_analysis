# 电商数据分析 —— 基于RFM模型的用户价值分析
**电商数据分析 · MySQL、Python、PowerBI等多工具协同分析 · 商业智能报告展示**

## 项目简介
本项目旨在利用生成的模拟电商数据，基于RFM模型模拟用户价值分析的场景，目标是模拟实现从数据库数据获取、数据处理、建立RFM模型进行数据分析到可视化的完整分析管线，锻炼自身的数据分析思维和适用多种分析工具的能力。

数据说明：基于Python生成的模拟数据，数据本身并无意义，重要的分析过程。

目标：根据不同的R、F、M取值，对用户进行分层分类，分析用户价值。

## 主要步骤
- 利用Python建立RFM模型
- 根据R、F、M对用户进行分层（分类）并贴上标签（详情参考“RFM分析测试代码.ipynb”）
- 使用PowerBI建立报表进行分析（详情查看“用户价值分析报表.pbix”）

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
│
├── 模拟数据生成脚本.ipynb
│
├── scripts/ # 脚本形式的处理代码
│ ├── bi主题设置/    # powerbi所用主题背景
│ ├── RFM_data/
│ │  └── RFM分析表.xlsx
│ ├── RFM分析测试代码.ipynb
│ ├── RFM数据表生成脚本.py    # （同RFM分析测试代码.ipynb）
│ └── 用户价值分析报表.pbix    # 分析报表
│
└── README.md # 项目介绍
```

## 部分效果展示
![image](https://github.com/user-attachments/assets/5e7fb211-f11c-4122-a93d-a0ad4f4abd7c)

![image](https://github.com/user-attachments/assets/7924deb7-e845-4b06-b112-0395f29c75e8)

![image](https://github.com/user-attachments/assets/17a7009d-2498-4ee0-9c6c-066907b0abc1)

## 项目价值
- 熟练掌握MySQL数据交互
- 锻炼Python进行数据分析的能力、以及数据分析思维
- 实战运用 PowerBI 制作专业报表
