import os # operating system

#讀取檔案
products = []
if os.path.isfile('products.csv'):#os的路徑使用isfile功能 檢查檔在不在
	print('Yeah!找到檔案')
	with open ('products.csv','r',encoding='utf-8') as f:
		for line in f:
			if'商品,價格' in line:
				continue # 繼續 如果遇到商品或價格在line裡面就跳到下一回
				name, price=line.strip().split(',')#用strip 去掉\n 再用split 切割完的結果是清單
				#name = s[0]
				#price = s[1]
				products.append([name,price])
	print(products)


else:
	print('找不到檔案')


#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = int(input ('請輸入商品價格:'))
	#p = []
	#p.append(name)
	#p.append(price)
	p =[name,price] #省略寫法
	products.append(p)
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0],'的價格是',p[1])

#寫入檔案
with open('products.csv','w',encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0]+ ',' + str(p[1]) +'\n') #'\n'換行
	



