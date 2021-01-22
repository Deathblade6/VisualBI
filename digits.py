#Time Complexity-O(n) Space Complexity-O(n)
#The code currently only counts till nine occurences but can be easily expanded by adding the english representation of the numbers 10,11...etc to the variable d
def main():
    x=[int(x) for x in input("Enter digit: ")]
    d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    val={}
    ctr=1
    s=''
    for i in range(len(x)):
        if i!=len(x)-1 and x[i]==x[i+1]:
            ctr+=1
        else:
            if ctr>1:
                s+=str(d[ctr])+" "+str(x[i])+"\'s and "
            else:
                s+=str(d[ctr])+" "+str(x[i])+" and "
            ctr=1
        if x[i] in val:
            val[x[i]]+=1
        else:
            val[x[i]]=1
    print(s.rstrip('and '))
    z=''
    for i in val:
        if i not in d:
            print("The code currently only counts till nine occurences but can be easily expanded by adding the english representation of the numbers 10,11...etc to the variable d")
            return
        if val[i]>1:
            z+=d[val[i]] + " "+str(i)+"\'s and "
        else:
            z+=d[val[i]] + " "+str(i)+" and "

    print("Total:",z.rstrip('and '))

main()
