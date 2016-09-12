
def mines(X,x,y):
    #рахує кількість мін навколо точки
    mine = 0
    if X[x][y] == "*":
        return "*"
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if 0<=i<len(X) and 0<=j<len(X[0]):
                if X[i][j] == "*":
                    mine += 1
    return mine

print("Вітаю!!!\nЦе гра МІНЕР")
print("Введіть розмір ігрового поля\n")
rows, colums = input().split()
rows = int(rows)
colums = int(colums)
table = []
result = [[0 for x in range(colums)]for y in range(rows)]
print("Веддіть іргове поле: '*' - бомба, '.' - пуста клітинка.\n ")
#зчитуємо ігрове поле і записуємо в список
for i in range(rows):
    v = list(input())
    table.append(v)
#для кожної точки шукаємо міни
for i in range(rows):
    for j in range(colums):
        result[i][j] = mines(table,i,j)
    print("")
#виводимо результат
for i in range(rows):
    for j in range(colums):
        print(result[i][j],end="")
    print("")

