#1
# def half_list(li:str):
#     l=li.split(",")
#     for i in range(0,len(l)//2):
#         print(l[i],end=" ")
#     print()
#     for i in range(len(l)//2,len(l)):
#         print(l[i],end=" ")
# li=str(input("Enter a list "))
# half_list(li)
#בודאי שזה נשאר o(n) כי עדיין הסיבוכיות תלויה באורך הקלט של המשתמש
#2
# def two_times(li:list):
#     for i in li:
#         print(i,i)
# two_times(["s","f","g"])
#O(n) וכן ניתן על ידי שהכנסנו בהדפסה אחת את שני האיברים
#3
# def min_num(li):
#     min=li[0]
#     for i in li:
#         if i<min:
#             min=i
#     return min
# print(min_num([8,95,-76,100]))
#במידה ומדובר ברשימה מאורגנת אפשר להפוך את זה ליותר קטן ע"י פניה לאינדס 0 ןאז זה O(1)
#4
# def even_num(li):
#     l=[]
#     for i in li:
#         if i%2==0:
#             l.append(i)
#     return sum(l)
# print(even_num([1,6,4,5,56,66]))
#סיבוכיות נשמרת ואינה משתנה כי הסיבוכיות מושפעת באופן ישיר מהמשתמש
#5
# def positive(l):
#     p_l=[]
#     p_l_1=[]
#     for i in l:
#         if i>0:
#             p_l.append(i)
#         else:
#             if len(p_l_1)<len(p_l):
#                 p_l_1=p_l
#             p_l=[]
#         if len(p_l_1) < len(p_l):
#             p_l_1 = p_l
#     return p_l_1
# print(positive([1,-2,5,-9,6,-6,6,-4,3,4,2]))
#סיבוכיות O(N) בגלל שזה תלוי רק במשתמש ולא נתון כפונקציה ריבועית
# #6
# def even(l:list):
#     for i in l:
#         for j in l:
#             print(i,j)
#     return " "
# print(even([1,2,3,4,5,9]))
#סיבוכיות o(n) בשניה
#7
s=set()
c=0
def duplicate(l:list):
    c=0
    for i,v in enumerate(l):
        for j,h in enumerate(l):
            if v==h and i!=j:
                s.add(v)
                c +=1
    print(c)
    return s
print(duplicate([1,2,2,3,5,7,8,7,8]))
# O(N) בשניה
#8



