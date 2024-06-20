#Tower of Hanoi(Has 3 rods"A","B","C")
def tower(n,a,b,c):
#Here n is the number of discs , a is the "origin" ,b is "mid tower" and c is the destination rod 
    if n==1:
        print("Move the first disc from",a,"to",c)
        return
    tower(n-1,a,c,b)
    print("Move",n,"from",a,"to",c)
    tower(n-1,b,a,c)
n=int(input("Enter number of discs: "))
tower(n,"A","B","C")
