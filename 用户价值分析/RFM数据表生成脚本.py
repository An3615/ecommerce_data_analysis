import pandas as pd
from sqlalchemy import create_engine

def run()
    # 读取数据 —— MySQL数据库
    engine = create_engine('mysql+pymysql://root:123456@localhost/sale_datas')
    orders = pd.read_sql_table('orders', engine)
    orders_1 = orders[orders['订单状态']=='已完成']
    
    # 一、用户价值分析 —— RFM 模型
    
    latest_date = orders['下单时间'].max() + pd.Timedelta(days=1)
    rfm = orders.groupby(['用户ID']).agg({
        '下单时间': lambda x: (latest_date - x.max()).days, 
        '订单ID': 'count', 
        '支付金额': 'sum'
    }).reset_index()
    rfm.columns = ["用户ID", "最近购买间隔（天）", "购买次数", "总消费金额"]
    
    # 计算RFM分数
    rfm['R_score'] = pd.qcut(rfm['最近购买间隔（天）'].rank(method='first'), q=5, labels=[i for i in range(5,0,-1)]).astype(int)
    rfm['F_score'] = pd.qcut(rfm['购买次数'].rank(method='first'), q=5, labels=[i for i in range(1,6,1)]).astype(int)
    rfm['M_score'] = pd.qcut(rfm['总消费金额'].rank(method='first'), q=5, labels=[i for i in range(1,6,1)]).astype(int)
    
    # 用户分类 —— 依据R、F、M的平均分
    R_mean = rfm['R_score'].mean()
    F_mean = rfm['F_score'].mean()
    M_mean = rfm['M_score'].mean()
    def _group(row): 
        # 高-高-高
        if row['R_score'] >= R_mean and row['F_score'] >= F_mean and row['M_score'] >= M_mean: 
            return '重要价值用户'
        # 高-低-高
        elif row['R_score'] >= R_mean and row['F_score'] < F_mean and row['M_score'] >= M_mean:
            return '重要发展用户'
        # 低-高-高
        elif row['R_score'] < R_mean and row['F_score'] >= F_mean and row['M_score'] >= M_mean:
            return '重要保持用户'
        # 低-低-高
        elif row['R_score'] < R_mean and row['F_score'] < F_mean and row['M_score'] >= M_mean:
            return '重要挽留用户'
        # 高-高-低
        elif row['R_score'] >= R_mean and row['F_score'] >= F_mean and row['M_score'] < M_mean:
            return '一般价值用户'
        # 高-低-低
        elif row['R_score'] >= R_mean and row['F_score'] < F_mean and row['M_score'] < M_mean:
            return '一般发展用户'
        # 低-高-低
        elif row['R_score'] < R_mean and row['F_score'] >= F_mean and row['M_score'] < M_mean:
            return '一般保持用户'
        # 低-低-低
        else:
            return '一般挽留用户'
    rfm['用户类型'] = rfm.apply(_group, axis=1)
    rfm.to_excel('./RFM_data/RFM分析表.xlsx', index=False)

if __name__ == '__main__':
    run()