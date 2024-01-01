class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self,other):
        return self.x==other.x,self.y==other.y

while True:
    try:
        f_point=Point(int(input("Enter x coordinate: ")),int(input("Enter y cooridnate: ")))
        s_point=Point(int(input("Enter other x coordinate: ")),int(input("Enter other y cooridnate: ")))
        print(f_point==s_point)
        False
    except ValueError:
        print("Enter numbers")
