from datetime import datetime as dt
a = dt.strptime("1910-12-13", "%Y-%m-%d")
b = dt.strptime("1910-11-13", "%Y-%m-%d")

print (a>b)
