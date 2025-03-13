import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import time
from scipy.spatial.distance import euclidean
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression





import matplotlib.pyplot as plt
from dtw import dtw
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

#  数据集划分（80% 训练集，20% 测试集）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  训练随机森林回归模型
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

#  预测
y_pred = rf.predict(X_test)

#  评估模型
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 输出结果
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R-Score: {r2:.4f}")

from pai.estimator import Estimator

# 获取PAI支持的最新PyTorch镜像。
torch_image_uri = retrieve("PyTorch", framework_version="1.12").image_uri

est = Estimator(
    source_dir="./test/"
)

# 提交训练作业，同时打印训练作业的Web详情页URL。fit调用默认等待到作业终止（成功、失败、或被停止）。
est.fit()
