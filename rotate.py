def main():
    l=[int(x) for x in input("Enter array space separated: ").split()]
    n=int(input("Enter size: "))
    k=int(input("Enter number of shifts: "))
    x=int(input("Choose which way to shift 1 or 2: "))

    k=k%n

    if x==1:
        #Time Complexity - O(n*k) Space Complexity - O(1)
        for i in range(k):
            for j in range(n-1,0,-1):
                l[j],l[j-1]=l[j-1],l[j]
        print(l)

    elif x==2:
        #Time Complexity - O(n) Space Complexity - O(n)
        ans=[]
        for i in range(n):
            ans.append(l[(i+(n-k))%n])
        print(ans)
main()
