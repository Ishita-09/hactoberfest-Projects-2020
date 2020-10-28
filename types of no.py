while True:
    print("1.Special Number")
    print("2.Armstrong Number")
    print("3.Prime Number")
    print("4.Automorphic Number")
    print("5.Exit")
    print()
    c=int(input("Enter Choice:"))
    if c==1:
        x=int(input("Enter a Number:"))
        y=x
        t=0
        while True:
            if x>0:
                q=x%10
                s=1
                for i in range(q,0,-1):
                    s=s*i
                t=t+s
                x=x//10
            else:
                break
        if t==y:
            print("Special Number")
        else:
            print("Not a Special Number")

 


    elif c==2:
        x=int(input("Enter a Number:"))
        y=x
        s=0
        while True:
            if x>0:
                s=s+((x%10)**3)
                x=x//10
            else:
                break
        if s==y:
            print("Armstrong Number")
        else:
            print("Not an Armstrong Number")




    elif c==3:
        x=int(input("Enter a Number:"))
        flag=0
        for i in range(2,x):
            if x%i==0:
                flag=1
        if flag==0:
            print("Prime Number")
        else:
            print("Not a Prime Number")

    


    elif c==4:
        x=int(input("Enter a Number:"))
        y=x**2
        if y>=0 and y<100:
            q=y%10
        elif y>=100 and y<1000:
            q=y%100
        if q==x:
            print("Automorphic Number")
        else:
            print("Not an Automorphic Number")

   

    else:
        print("Exit")
        break
