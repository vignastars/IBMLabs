def compute_lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
     while True:
          if(greater % x == 0) and (greater % y == 0):
                lcm = greater
                break
            greater += 1
            return lcm
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
print("the lcm is ",compute_lcm(num1,num2))
        
            