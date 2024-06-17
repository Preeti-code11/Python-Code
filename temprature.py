def convert_temp_in_celsius(fahrenheit):
    celsius=(fahrenheit-32)*(5/9)
    return celsius
temprature=convert_temp_in_celsius(100)
print(temprature)
def convert_temp_in_fahrenheit(celsius):
    fahrenheit=(celsius*(9/5))+32
    return fahrenheit
temprature=convert_temp_in_fahrenheit(37.7777777)
print(temprature)