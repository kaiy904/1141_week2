# 輸入要轉換的數字
weight = float(input("請輸入數字: "))
unit = input("請輸入單位 (kg 或 lb): ").lower()

if unit == "kg":
    converted = weight * 2.20462
    print(f"{weight} 公斤 ≈ {converted:.2f} 磅")
elif unit == "lb":
    converted = weight / 2.20462
    print(f"{weight} 磅 ≈ {converted:.2f} 公斤")
else:
    print("單位輸入錯誤，請輸入 kg 或 lb")
