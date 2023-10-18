'''
 Print the following using two for loops

1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
'''

num=int(input("Enter the number:"))
print("The multiplication table of:",num)
for i in range(1,num+1):
    for num in range(1,6):
        print(i,"*",num,"=",i*num)