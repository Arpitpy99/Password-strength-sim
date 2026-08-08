f = open(r"C:\Users\arpit\OneDrive\Documents\rara.txt","w")
l = []
while True:
    name = input("Enter your name: ")
    roll_no , marks = map(int,input('Enter your roll no and marks').split())
    gate = int(input("Press 0 to exit"))
    l.append([name,roll_no,marks])
    if gate == 0:
        print(l)
        break
a = ""
for i in l:
    a += str(l)+" "
f.write(a)