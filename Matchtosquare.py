def mycode(numbers):
    summ = sum(numbers)
    width1 = 0
    width2 = 0
    if summ % 4 == 0:
        width = summ/4
        for a in numbers:
            if a > width:
                return False
            if width in numbers:
                numbers.remove(width)
                width1 +=1
                print("test 1:", width1, numbers)
            if width - a in numbers:
                numbers.remove(a)
                numbers.remove(width-a)
                width1+= 1
                print("test 2:", width1, numbers)
                if sum(numbers)== width:
                    width1+=1               
            if width - a > min(numbers, default= 100):
                width = width-a
                numbers.remove(a)
                width1+= 1
                print("test 3:", width, numbers)     
        if width1 == 4:
            return True
        return False

print(mycode([4,4,4,4]))