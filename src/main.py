from sklearn.linear_model import LinearRegression 
X = [[1], [2], [3], [4], [5]]
Y = [50 , 60, 72 ,85, 90 ]

model = LinearRegression() 
model.fit(X, Y )
hours = float(input("Enter the hours worked: "))

print("The prediction is: ", model.predict([[hours]]))