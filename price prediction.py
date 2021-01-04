import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pandas.read_excel("Book1.xlsx")
model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[30]]))
plt.plot(data['version'], data['price'])
plt.scatter(data['version'], data['price'])
plt.show()
