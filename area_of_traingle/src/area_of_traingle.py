'''
Area of a Triangle from Sides
    Just use this two step process:
    Step 1: Calculate "s" (half of the triangles perimeter):  s =  a+b+c2
    Step 2: Then calculate the Area: herons formula A = sqrt( s(s-a)(s-b)(s-c) )
'''

def calculate_area_of_traingle(side_a=-1,side_b=-1,side_c=-1):

    try:
        #comparison can only happen if input var is int or float
        if(side_a <= 0 or side_b <= 0 or side_c <= 0 ):
            print("side should not be greater than 0")
            return -1
    except:
        print("side is not a valid data type , not integer or float")
        return -2

    t_perimeter = side_a+side_b+side_c
    t_area = (t_perimeter*(t_perimeter-side_a)*(t_perimeter-side_b)*(t_perimeter-side_c)) ** 0.5
    print(t_area)
    return t_area

if __name__ == '__main__':
    exit(calculate_area_of_traingle('a',0.0005,1))