import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# 生成toy data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 分割數據集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 訓練線性回歸模型
model = LinearRegression()
model.fit(X_train, y_train)

# 進行預測
y_pred = model.predict(X_test)

# 保存結果到CSV文件
results = pd.DataFrame(data={'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
results.to_csv('predictions.csv', index=False)

print("Prediction results saved to predictions.csv")
