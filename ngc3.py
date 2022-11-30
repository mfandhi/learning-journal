def convert_ck(c):                  # function konversi c --> k
    return 273.5 + c

def convert_cf (c):                 # function konversi c --> f  
    return c * 9/5 + 32

def convert_kc (k):                 # function konversi k --> c
    return k - 273.15

def convert_fc (f):                 # function konversi f --> c
    return (f - 32) * 5/9

def convert_kf (k):                 # function konversi k --> f
    return ((k-273.15)*9/5 +32) 

def convert_fk (f):                 # function konversi f --> k
    return ((f-32)*5/9 + 273.15)    

temp = input("Input the temperature you like to convert: (e.g., 45F, 300K, 32C)")       # input for conversion
print(temp)
target_unit = input("Convert to: (C/F/K) ")        # target unit conversion
print(target_unit)
degree = int(temp[:-1])       # ngilangin satuan supaya input value sisa angka
unit = temp[-1]           # ngambil satuan yang diinput untuk dipakai di kondisional if


if unit.upper()== "C":                          
    if target_unit.upper() == "K":
        result = round(convert_ck(degree),2)
        print("Converted: ", result, " K")
    elif target_unit.upper() == "F":
        result = round(convert_cf(degree), 2)                   
        print("Converted: ", result, "F")
    elif target_unit.upper() == "C":
        print("it's already in celcius :)")
    else: print("input the right unit :)")

elif unit.upper() == "K":
    if target_unit.upper() == "C":
        result = round(convert_kc(degree),2)
        print("Converted: ", result, " C")
    elif target_unit.upper() == "F":
        result = round(convert_kf(degree),2)            # menyesuaikan input menggunakan kondisional if untuk dikonversi sesuai dengan target yang diminta
        print("Converted: ", result, " F")
    elif target_unit.upper() == "C":
        print("it's already in kelvin :)")
    else: print("input the right unit :)")

elif unit.upper() == "F":
    if target_unit.upper() == "C":
        result = round(convert_fc(degree),2)
        print("Converted: ", result, " C")
    elif target_unit.upper() == "K":
        result = round(convert_fk(degree),2)
        print("Converted: ", result, " K")
    elif target_unit.upper() == "F":
        print("it's already in fahrenheit :)")
    else: print("input the right unit :)")
else: print("input error, please try again:)")