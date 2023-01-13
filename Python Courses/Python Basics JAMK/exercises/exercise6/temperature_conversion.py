def celToFah():
    cel = float(input("Enter temperature in celsius to convert to fahrenheit: "))
    fah = (cel*1.8) + 32
    print("%.1f" %fah)
    
celToFah()

def fahToCel():
    fah = float(input("Enter temperature in fahrenheit to convert to celsius: "))
    cel = (fah-32) / 1.8
    print("%.1f" %cel)
    
fahToCel()