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
list_2=[1,2,3,4,5,6,7,8]
for i,v in enumerate(list_2):
    if i<len(list_2)/2:
        print(v)
#בגלל שהרשימה ידועה מראש אז זוהי סיבוכיות קבועה כי היא ידועה מראש