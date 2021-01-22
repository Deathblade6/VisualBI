# Time Complexity-O(n) Space Complexity-O(1)
def main():
    n=[int(x) for x in input("Enter input ages comma-separated:").split(',')]
    l=[0]*10
    for i in n:
        if i>=1 and i<11:
            l[0]+=1
        elif i>=11 and i<21:
            l[1]+=1
        elif i>=21 and i<31:
            l[2]+=1
        elif i>=31 and i<41:
            l[3]+=1
        elif i>=41 and i<51:
            l[4]+=1
        elif i>=51 and i<61:
            l[5]+=1
        elif i>=61 and i<71:
            l[6]+=1
        elif i>=71 and i<81:
            l[7]+=1
        elif i>=81 and i<91:
            l[8]+=1
        elif i>=91 and i<101:
            l[9]+=1
        else:
            print(i,"is an invalid age.")
    print("Age Group\t Total number of People")
    for i in range(10):
        if i==0:
            print("1-10\t\t",l[0])
        else:
            print(str(i)+"1-"+str(i+1)+"0\t\t",l[i])

main()
