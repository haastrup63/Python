celsius_degrees = [20, 16, 19, 22, 18, 30]
 
# Calculating each celsius degree to fahrenheit
fahrenheit_degrees = list(map(lambda x : (x*1.8)+32, celsius_degrees))

print(fahrenheit_degrees)