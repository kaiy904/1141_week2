# 整合轉換程式：長度、溫度、重量

print("歡迎使用整合轉換程式！")
print("請選擇轉換類型：")
print("1: 長度 (公里 ↔ 英里)")
print("2: 溫度 (攝氏 ↔ 華氏)")
print("3: 重量 (公斤 ↔ 磅)")

choice = input("輸入數字選擇類型 (1/2/3): ")

if choice == "1":
    # 長度轉換
    value = float(input("輸入數值: "))
    unit = input("輸入單位 (km 或 mi): ").lower()
    if unit == "km":
        result = value * 0.621371
        print(f"{value} 公里 = {result} 英里")
    elif unit == "mi":
        result = value / 0.621371
        print(f"{value} 英里 = {result} 公里")
    else:
        print("單位輸入錯誤！請輸入 km 或 mi")

elif choice == "2":
    # 溫度轉換
    value = float(input("輸入數值: "))
    unit = input("輸入單位 (C 或 F): ").upper()
    if unit == "C":
        result = (value * 9/5) + 32
        print(f"{value}°C = {result}°F")
    elif unit == "F":
        result = (value - 32) * 5/9
        print(f"{value}°F = {result}°C")
    else:
        print("單位輸入錯誤！請輸入 C 或 F")

elif choice == "3":
    # 重量轉換
    value = float(input("輸入數值: "))
    unit = input("輸入單位 (kg 或 lb): ").lower()
    if unit == "kg":
        result = value * 2.20462
        print(f"{value} 公斤 = {result} 磅")
    elif unit == "lb":
        result = value / 2.20462
        print(f"{value} 磅 = {result} 公斤")
    else:
        print("單位輸入錯誤！請輸入 kg 或 lb")

else:
    print("輸入錯誤！請輸入 1、2 或 3")
