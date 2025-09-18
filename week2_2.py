# 公里與英里互換程式

choice = input("請選擇轉換方式 (1: 公里 → 英里, 2: 英里 → 公里): ")

if choice == "1":
    km = float(input("請輸入公里數: "))
    mile = km * 0.621371
    print(km, "公里 = ", round(mile, 2), "英里")

elif choice == "2":
    mile = float(input("請輸入英里數: "))
    km = mile / 0.621371
    print(mile, "英里 = ", round(km, 2), "公里")

else:
    print("輸入錯誤，請選擇 1 或 2")
