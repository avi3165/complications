#2
# for i in range(1,11):
#     print(i)
# #סיבוכיות של קבוע כי כל הזמן זה רץ 10 פעמים
#3
# def print_elements(l):
#     for i in l:
#         print(i)
# l=[1,2,3,4]
# print_elements(l)
#סיבוכיות משתנה בהתאם לאורך הרשימה היות והיא משפיעה באופן ישיר על מספר ההדפסות
#4
# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j,end="\t")
#     print()
#סיבוכיות קבועה בגלל שמתחילה מספר הריצות היה כך, ואם נהפוך לעשר זה יהפוך לפי 4 ויהיו 100 ועדיין ישאר קבוע
#5
# number=int(input("Please enter a number: "))
# list_1=[]
# while number!=0:
#     list_1.append(number)
#     number = int(input("Please enter a number: "))
# print(sum(list_1))
#סיבוכיות לינארית בגלל שזה תלוי במספר הקלטים של המשתמש
#6
# list_2=[1,2,3,4,5,6,7,8]
# for i,v in enumerate(list_2):
#     if i<len(list_2)/2:
#         print(v)
#בגלל שהרשימה משתנה אז זוהי סיבוכיות לינארית כי היא נתונה מהמשתמש
#7
# list_3=[3,7,23,46,89,61,2,72,11]
# def find_element(n:int):
#     a = False
#     for i,v in enumerate(list_3):
#         if n==v:
#             a=True
#             print("the number found in index",i)
#     if a ==False:
#         print("The number was not found")
# n=12
#סיבוכיות לניארית כי זה תלוי בגודל הרשימה
#8
# def find_even(li:list[int]):
#     for v in li:
#         if v%2==0:
#             print(v)
# find_even([2,3,7,6,4,12,14])
#סיבוכיות לניארית היות ותלויה באורך רשימה
#9
def max_number(li:str):
    l=li.split(',')
    l_1=[]
    for i in l:
        l_1.append(int(i))
    a=max(l)
    print(a)
li=(input("Please enter a list of numbers: "))
max_number(li)
#סיבוכיות לניארית מפני שיש צורך בקלט וכמות הפעולות משתנה בהתאם לגודל הקלט