import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# สร้าง DataFrame ตัวอย่าง
data = {
    'area': [1000, 1500, 2000, 2500, 3000],
    'bedrooms': [3, 3, 2, 4, 4],
    'age': [10, 5, 20, 15, 10],
    'price': [500000, 700000, 600000, 900000, 800000]
}

df = pd.DataFrame(data)

# แยก Features และ Target
X = df[['area', 'bedrooms', 'age']]
y = df['price']

# แบ่งข้อมูลเป็นชุดฝึกและชุดทดสอบ
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# สร้างโมเดล
model = LinearRegression()
model.fit(X_train, y_train)

# ทำนาย
y_pred = model.predict(X_test)

# ประเมินผล
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')


# เนสชชช