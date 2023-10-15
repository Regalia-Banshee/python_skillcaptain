class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

run=1
while run==True:
    try:
        firstPoint=Point(int(input("Enter x co-ordinate: ")),int(input("Enter y co-ordinate: ")))
        secondPoint=Point(int(input("Enter x co-ordinate again: ")),int(input("Enter y co-ordinate again: ")))
        print(firstPoint==secondPoint)
        run=False

    except ValueError:
        print("Enter numbers!!!")