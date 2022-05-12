import os #operating system
#讀取檔案
products = []   #建立一一個清單 


if os.path.isfile("products.csv"):
    print("檔案存在")
    with open("products.csv", "r", encoding="utf-8") as f:
        for line in f:
            if "商品名稱,價格" in line:
                continue
            name, price = line.strip().split(",")
            products.append([name, price])
    print(products)    
else:
    print("找不到檔案.....!")





while True:   #創造一個無限迴圈
    name = input("請輸入購買商品:")  
    if name == "q":  # 設定一個迴圈停止條件
        break
    price = input("請輸入商品價格:")
    price = int(price)
    products.append([name, price])  #二維清單的概念
    #products.append(price)
    

print(products)    
for i in products:
    print("商品名稱:", i[0], "價格:", i[1])
with open("products.csv", "w", encoding="utf-8" ) as f:
    f.write("商品名稱,價格\n")
    for p in products:
        f.write(p[0] + "," + str(p[1])+"\n"  )

