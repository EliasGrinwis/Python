with open("../FilesChapter7/stock1.txt") as stock1:
    stock1.readline()
    line_stock_1 = stock1.readline()

    check_list = []

    while line_stock_1:
        if line_stock_1 != "\n":
            #print(line_stock_1.rstrip())
            record = line_stock_1.split(';')
            #print(record[0].rstrip())
            check_list.append(record[0].rstrip())
        line_stock_1 = stock1.readline()

print(check_list)

with open("../FilesChapter7/stock2.txt") as stock2:
    stock2.readline()
    line_stock_2 = stock2.readline()

    while line_stock_2:
        if line_stock_2 != "\n":
            # print(line_stock_1.rstrip())
            record = line_stock_2.split(';')
            print(record[0].rstrip())
        line_stock_2 = stock2.readline()

#FOR LATER