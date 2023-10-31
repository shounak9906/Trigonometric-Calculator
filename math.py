import math
import time

#prints sine of a value
"""print("sin(1):", math.sin(10/573))"""

#prints cosine of a value
"""print("cos(1):", math.cos(10/573))"""

#prints tangent of a value
"""print("tan(1):", math.tan(10/573))"""

#function to convert radians to degrees
"""a = float(input("Enter radian value to convert to degrees:"))
rad_to_deg = z * 180/math.pi
print(round(rad_to_deg,2))"""

#formulas
"""1rad x 180/pi = deg

1rad = (deg x pi)/180"""

#converts inputed degree value into radians
"""b = float(input("Enter degree value to convert to radians:"))
deg_to_rad = (b * math.pi)/180
print(round(deg_to_rad,4))"""

#pythagoras theorem to find length of hypotenuse
"""s1 = float(input("enter length of first side:"))
s2 = float(input("enter length of second side:"))
hypo = math.sqrt(s1**2 + s2**2)
print("the length of the hypotenuse is:", round(hypo, 3))"""

#pythagoras theorem to find length of any one side of triangle
"""a = input("do you want to find length of hypotenuse?(y/n):")
if a in ('y','yes','Y'):
    s1 = float(input("enter length of first side:"))
    s2 = float(input("enter length of second side:"))
    hypo = math.sqrt(s1**2 + s2**2)
    print("the length of the hypotenuse is:", round(hypo, 3))

else:
    s = float(input("finding length of side, enter length of known non-hypotenuse side:"))
    h = float(input("enter length of hypotenuse:"))
    s_length = math.sqrt(h**2 - s**2)
    print("the length of the side is:", round(s_length, 3))"""

#trigonometry
tri_type = input("is your triangle right-angled?(yes/no):")
calc_type = input("do you want to find the size of an angle or side?:")

if tri_type in ('yes', 'Yes', 'YES', 'it is') :
    if calc_type in ('angle' , 'Angle' , 'ANGLE') :
        
        print('''This calculator only works on right angled triangles. It can find the size of an angle. A
                 sample triangle is given below. Please enter values of sides and angles in the given format. Type 0
                 for the unknown angles and sides. TYPE x FOR THE ANGLE TO BE FOUND. ''')
        print("")
        print("")
        print('''    
                     **
                     ***
                     ****
              side B *****  side C 
                     ******
                     *******
                     ********
                     *********
                      side A
              ''')
        print("")
        print("")
        A = float(input("enter value of side A:"))
        B = float(input("enter value of side B:"))
        C = float(input("enter value of side C:"))
        a = input("enter value of angle a:")
        b = input("enter value of angle b:")

        a_int = 0
        b_int = 0

        if (a != "x") and (a != "0") :
            a_int = float(a)
        if (b != "x") and (b != "0") :
            b_int = float(b)

        if (A >= C) or (B >= C) :
            while (C != 0) :
                print("")
                print("sides can't be larger or equal to hypotenuse.")
                exit()

        if (a != "x") and (b != "x") :
            print("")
            print("please enter x for the angle to be found")
            exit()

        if ((A == 0) and (B == 0) and (C == 0)) and (((a_int == 0) or (a == "x")) and ((b_int == 0) or (b_int == "x"))) :
            print("")
            print("please enter either two sides or one angle")                                       
            exit()

        if  ((a == "x") or (b == "x")) and ((a_int == 0) and (b_int == 0)):
            if (B and C != 0) and (b == "x") : 
                print("finding size of angle b using sine... ")
                b = math.asin(B/C)
                rad_to_deg = b * 180/math.pi
                time.sleep (2)
                print("")
                print("angle b = ", round(rad_to_deg, 2))

            elif (A and C != 0) and (a == "x") :
                print("finding size of angle a using sine... ")
                a = math.asin(A/C)
                rad_to_deg = a * 180/math.pi
                time.sleep (2)
                print("")
                print("angle a = ", round(rad_to_deg, 2))
            
            elif (A and C != 0) and (b == "x") :
                print("finding size of angle b using cosine... ")
                b = math.acos(A/C)
                rad_to_deg = b * 180/math.pi
                time.sleep (2)
                print("")
                print("angle b = ", round(rad_to_deg, 2 ))

            elif (B and C != 0) and (a == "x") :
                print("finding size of angle a using cosine... ")
                a = math.acos(B/C)
                rad_to_deg = a * 180/math.pi
                time.sleep (2)
                print("")
                print("angle a = ", round(rad_to_deg, 2))

            elif (A and B != 0) and (b == "x") :
                print("finding size of angle b using tangent... ")
                b = math.atan(B/A)
                rad_to_deg = b * 180/math.pi
                time.sleep (2)
                print("")
                print("angle b = ", round(rad_to_deg, 2))

            elif (A and B != 0) and (a == "x") :
                print("finding size of angle a using tangent... ")
                a = math.atan(A/B)
                rad_to_deg = a * 180/math.pi
                time.sleep (2)
                print("")
                print("angle a = ", round(rad_to_deg, 2))
                

        if ((a_int != 0) or(b_int != 0)):
            if (a_int != 0) :
                print("finding angle b using given angles...")
                b = 180 - (a_int + 90)
                time.sleep(2)
                print("angle b = ", round(b, 2))

            elif (b_int != 0) :
                print("finding angle a using given angles...")
                a = 180 - (b_int + 90)
                time.sleep(2)
                print("angle a = ", round(a, 2))
            



    elif calc_type in ('side' , 'Side' , 'SIDE' ) :
        
        print('''This calculator only works on right angled triangles. It can find the length of a side . A
                 sample triangle is given below. Please enter values of sides and angles in the given format. Type 0
                 for the unknown angles and sides. TYPE x FOR THE SIDE TO BE FOUND. ''')
        print("")
        print("")
        print('''    
                     **
                     ***
                     ****
              side B ***** side C 
                     ******
                     *******
                     ********
                     *********
                      side A
              ''')
        print("")
        print("")
        
        A = input("enter value of side A:")
        B = input("enter value of side B:")
        C = input("enter value of side C:")
        a = float(input("enter value of angle a:"))
        b = float(input("enter value of angle b:"))

        A_int = 0
        B_int = 0
        C_int = 0

        if (A != "x") and (A != "0") :
            A_int = float(A)
        if (B != "x") and (B != "0") :
            B_int = float(B)
        if (C != "x") and (C != "0") :
            C_int = float(C)

        if (C != "x"):
            if (A_int >= C_int) or (B_int >= C_int) :
                if (C != "0"):
                    print("")
                    print("sides can't be larger or equal to hypotenuse.")
                    exit()

        if (A != "x") and (B != "x") and (C != "x"): 
            print("")
            print("please enter x for the side to be found")
            exit()

        while ((A_int != 0) and (B_int != 0)) or ((A_int != 0) and (C_int != 0)) or ((B_int != 0) and (C_int != 0)) :
            
            if (A_int != 0) and (B_int != 0) and (C == "x") :
                print("finding side C using pythagoras' theorem...")
                C = math.sqrt(A_int**2 + B_int**2)
                time.sleep(2)
                print("")
                print("side C = ", round(C, 2))

            elif (A_int != 0) and (C_int != 0) and (B == "x") :
                print("finding side B using pythagoras' theorem...")
                B = math.sqrt(C_int**2 - A_int**2)
                time.sleep(2)
                print("")
                print("side B = ", round(B, 2))

            elif (B_int != 0) and (C_int != 0) and (A == "x") :
                print("finding side A using pythagoras' theorem...")
                A = math.sqrt(C_int**2 - B_int**2)
                time.sleep(2)
                print("")
                print("side A = ", round(A, 2))

        
        if (A == "x") or (B == "x") or (C == "x") :

            if (A == "x") :
                if (a != 0) and (C != "0") :
                    print("finding side A using sine...")
                    deg_to_rad = (a * math.pi)/180
                    A = math.sin(deg_to_rad) * C_int
                    time.sleep (2)
                    print("")
                    print("side A = ", round(A, 2))
                    

                elif (a != 0) and (B != "0") :
                    print("finding side A using tangent...")
                    deg_to_rad = (a * math.pi)/180
                    A = math.tan(deg_to_rad) * B_int
                    time.sleep (2)
                    print("")
                    print("side A = ", round(B, 2))

                elif (b != 0) and (C != "0") :
                    print("finding side A using cosine...")
                    deg_to_rad = (b * math.pi)/180
                    A = math.cos(deg_to_rad) * C_int
                    time.sleep (2)
                    print("")
                    print("side A = ", round(A, 2))

                elif (b != 0) and (B != "0") :
                    print("finding side A using tangent...")
                    deg_to_rad = (b * math.pi)/180
                    A =  B_int / (math.tan(deg_to_rad))
                    time.sleep (2)
                    print("")
                    print("side A = ", round(A, 2))

            if (B == "x") :
                if (a != 0) and (C != "0") :
                    print("finding side B using sine...")
                    deg_to_rad = (a * math.pi)/180
                    B = math.sin(deg_to_rad) * C_int
                    time.sleep(2)
                    print("")
                    print("side B = ", round(B, 2))

                elif (a != 0) and (A != "0") :
                    print("finding side B using tangent...")
                    deg_to_rad = (a * math.pi)/180
                    B = math.tan(deg_to_rad) * A_int
                    time.sleep(2)
                    print("")
                    print("side B = ", round(B, 2))
                
                elif (b != 0) and (C != "0") :
                    print("finding side B using sine...")
                    deg_to_rad = (b * math.pi)/180
                    B = math.sin(deg_to_rad) * C_int
                    time.sleep(2)
                    print("")
                    print("side B = ", round(B, 2))

                elif (b != 0) and (A != "0") :
                    print("finding side B using tangent...")
                    deg_to_rad = (b * math.pi)/180
                    B = math.tan(deg_to_rad) * A_int
                    time.sleep(2)
                    print("")
                    print("side B = ", round(B, 2))

            if (C == "x") :
                if (a != 0) and (A != "0") :
                    print("finding side C using sine...")
                    deg_to_rad = (a * math.pi)/180
                    C = A_int/(math.sin(deg_to_rad))
                    time.sleep(2)
                    print("")
                    print("side C = ", round(C, 2))

                elif (a != 0) and (B != "0") :
                    print("finding side C using cosine...")
                    deg_to_rad = (a * math.pi)/180
                    C = B_int/(math.cos(deg_to_rad))
                    time.sleep(2)
                    print("")
                    print("side C = ", round(C, 2))

                elif (b != 0) and (A != "0") :
                    print("finding side C using cosine...")
                    deg_to_rad = (b * math.pi)/180
                    C = A_int/(math.cos(deg_to_rad))
                    time.sleep(2)
                    print("")
                    print("side C = ", round(C, 2))

                elif (b != 0) and (B != "0") :
                    print("finding side C using sine...")
                    deg_to_rad = (b * math.pi)/180
                    C = B_int/(math.sin(deg_to_rad))
                    time.sleep(2)
                    print("")
                    print("side C = ", round(C, 2))





if tri_type in ('no', 'No', 'NO', 'it is not'):
    if calc_type in ('angle', 'Angle', 'ANGLE'):
        print('''This calculator only works on NON right angled triangles. It can find the size of an angle. A
                 sample triangle is given below. Please enter values of sides and angles in the given format. Type 0
                 for the unknown angles and sides. TYPE x FOR THE ANGLE TO BE FOUND. ''')
        print("")
        print("")
        print('''     
                    ** 
                   ****
                  ******
                 ********
         side B ********** side C 
               ************
              **************
             ****************
            ******************
                  side A
              ''')
        print("")
        print("")
        A = float(input("enter value of side A:"))
        B = float(input("enter value of side B:"))
        C = float(input("enter value of side C:"))
        a = input("enter value of angle a:")
        b = input("enter value of angle b:")
        c = input("enter value of angle c:")
        
        a_int = 0
        b_int = 0
        c_int = 0

        # converts angle input from string to integer type if they are not x or 0
        if (a != "x") and (a != "0") :
            a_int = float(a)
        if (b != "x") and (b != "0") :
            b_int = float(b)
        if (c != "x") and (c != "0") :
            c_int = float(c)

        # checks if user has inputted the angle to be found
        if (a != "x") and (b != "x") and (c != "x") :
            print("")
            print("type x for the angle to be found.")

        # checks if user has inputted multiple angles to be found
        if ((a == "x") and (b == "x")) or ((a == "x") and (c == "x") or ((b == "x") and (c == "x"))) :
            print("")
            print("program can only find size of one angle at a time")
            
        # checks if given side input is sufficient to find desired output
        if ((A == 0) and (B == 0) and (C != 0)) or ((A == 0) and (B != 0) and (C == 0)) or ((A != 0) and (B == 0) and (C == 0)) :
            if ((a_int == 0) and (b_int == 0) or (a_int == 0) and (c_int == 0) or (c_int == 0) and (b_int == 0)):
                print("please enter the size of atleast two sides or two angles")

        # checks if given angle input is sufficient to find desired output
        if ((a_int == 0) and (b_int == 0) and (c_int == 0)) and ((A == 0) or (B == 0) or (C == 0)) :
            print("please enter value of atleast one angle")
            
        # finding size of angle using given angles
        if ((a_int != 0) and (b_int != 0)) or ((a_int != 0) and (c_int != 0)) or ((b_int != 0) and (c_int != 0)) :
            if (a_int != 0) and (b_int != 0) and (c == "x"):
                print("finding angle c using given angles...")
                c = 180 - (a_int + b_int)
                time.sleep(2)
                print("")
                print("angle c = ", round(c, 2))

            if (a_int != 0) and (c_int != 0) and (b == "x"):
                print("finding angle b using given angles...")
                b = 180 - (a_int + c_int)
                time.sleep(2)
                print("")
                print("angle b = ", round(b, 2))

            if (c_int != 0) and (b_int != 0) and (a == "x"):
                print("finding angle a using given angles...")
                a = 180 - (c_int + b_int)
                time.sleep(2)
                print("")
                print("angle a = ", round(a, 2))



        # finding size of angle a using trigonometry
        # finding angle a
        if (a == "x") :
            
            # when side a is given
            if (A != 0) :
                
                # using angle b, side B and side A
                if (b_int != 0) and (B != 0) :
                    deg_to_rad = (b_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * A) / B) < 1) :
                        print("finding angle a using sine rule...")
                        a = math.asin((math.sin(deg_to_rad) * A) / B)
                        rad_to_deg = a * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle a = ", round(rad_to_deg, 2))

                    else :
                        print("incorrect triangle")
                        
                # using angle c, side c and side a
                if (c_int != 0) and (C != 0) :
                    deg_to_rad = (c_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * A) / C) < 1) :
                        print("finding angle a using sine rule...")
                        a = math.asin((math.sin(deg_to_rad) * A) / C)
                        rad_to_deg = a * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle a = ", round(rad_to_deg, 2))
                        
                    else :
                        print("incorrect triangle")
                        
                # using sides A, B and C
                if (B != 0) and (C != 0) :
                    if (0 <= (B**2 + C**2 - A**2) / (2*B*C) < 1) :
                        print("finding angle a using cosine rule...")
                        a = math.acos((B**2 + C**2 - A**2) / (2*C*B))
                        rad_to_deg = a * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle a = ", round(rad_to_deg, 2))

                    else :
                        print("")
                        print("incorrect triangle!")

                # using angle b and side C to find side B and then using side b and a and angle b
                if (b_int != 0) and (C != 0) :
                    deg_to_rad = (b_int * math.pi)/180
                    B = math.sqrt(A**2 + C**2 - (2 * A * C * math.cos(deg_to_rad)))
                    if (0 <= ((B**2 + C**2 - A**2) / (2*C*B)) < 1) :
                        print("finding angle a using cosine rule..." )
                        a = math.acos((B**2 + C**2 - A**2) / (2*C*B))
                        rad_to_deg = a * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle a = ", round(rad_to_deg, 2))
                        
                    else :
                        print("")
                        print("incorrect triangle!")

                # using angle c and side b to find side C and then using sides a, b and c
                if (c_int != 0) and (B != 0) :
                    deg_to_rad = (c_int * math.pi)/180
                    C = math.sqrt(A**2 + B**2 - (2 * A * B * math.cos(deg_to_rad)))
                    if (0 <= ((B**2 + C**2 - A**2) / (2*C*B)) < 1) :
                        print("finding angle a using cosine rule..." )
                        a = math.acos((B**2 + C**2 - A**2) / (2*C*B))
                        rad_to_deg = a * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle a = ", round(rad_to_deg, 2))

                    else :
                        print("")
                        print("incorrect triangle!")


            # when side a is not given
            elif (A == 0) :
                
                # using angle b, side b and c to find angle c
                if (b_int != 0) and (C != 0) and (B != 0) :
                    deg_to_rad = (b_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * C) / B) < 1) :
                        print("finding angle a using given angles and sine rule...")
                        c = math.asin((math.sin(deg_to_rad) * C) / B)
                        rad_to_deg = c * 180/math.pi
                        # using angles c and b to find angle a
                        a = 180 - (rad_to_deg + b_int)
                        time.sleep(2)
                        print("")
                        print("angle a = ", round(a, 2))

                    else :
                        print("")
                        print("incorrect triangle!")


                # using angle c, sides b and c to find angle b
                if (c_int != 0) and (C != 0) and (B != 0) :
                    deg_to_rad = (c_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * C) / B) < 1) :
                        print("finding angle a using given angles and sine rule...")
                        b = math.asin((math.sin(deg_to_rad) *   B) / C)
                        rad_to_deg = b * 180/math.pi
                        # using angles b and c to find angle a
                        a = 180 - (rad_to_deg + c_int)
                        time.sleep(2)
                        print("")
                        print("angle a = ", round(a, 2))

                    else :
                        print("")
                        print("incorrect triangle!")






        # finding angle b
        elif (b == "x") :
            
            # when side B is given
            if (B != 0) :
                
                # using angle c, sides b and c to find angle b
                if (c_int != 0) and (C != 0) :
                    deg_to_rad = (c_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * B) / C) < 1) :
                        print("finding angle b using sine rule...")
                        b = math.asin((math.sin(deg_to_rad) * B) / C)
                        rad_to_deg = b * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle b = ", round(rad_to_deg, 2))

                    else :
                        print("incorrect triangle")

                # using angle a, sides b and a to find angle b
                if (a_int != 0) and (A != 0) :
                    deg_to_rad = (a_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * B) / A) < 1) :
                        print("finding angle b using sine rule...")
                        b = math.asin((math.sin(deg_to_rad) * B) / A)
                        rad_to_deg = b * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle b = ", round(rad_to_deg, 2))

                    else :
                        print("incorrect triangle")

                # using sides A, B, C
                if (A != 0) and (C != 0) :
                    if (0 <= (A**2 + C**2 - B**2) / (2*A*C) < 1) :
                        print("finding angle b using cosine rule...")
                        b = math.acos((A**2 + C**2 - B**2) / (2*C*A))
                        rad_to_deg = b * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle b = ", round(rad_to_deg, 2))

                    else :
                        print("")
                        print("incorrect triangle!")

                # using angle a, sides B and C to find side A, using side a, b and c to find angle b
                if (a_int != 0) and (C != 0) :
                    deg_to_rad = (a_int * math.pi)/180
                    A = math.sqrt(B**2 + C**2 - (2 * B * C * math.cos(deg_to_rad)))
                    if (0 <= ((A**2 + C**2 - B**2) / (2*C*A)) < 1) :
                        print("finding angle b using cosine rule..." )
                        b = math.acos((A**2 + C**2 - B**2) / (2*C*A))
                        rad_to_deg = b * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle b = ", round(rad_to_deg, 2))
                        
                    else :
                        print("")
                        print("incorrect triangle!")

                # using angle c, sides B and A to find side C and using sides A, B and C to find angle b
                if (c_int != 0) and (A != 0) :
                    deg_to_rad = (c_int * math.pi)/180
                    C = math.sqrt(A**2 + B**2 - (2 * B * A * math.cos(deg_to_rad)))
                    if (0 <= ((A**2 + C**2 - B**2) / (2*C*A)) < 1) :
                        print("finding angle b using cosine rule..." )
                        b = math.acos((A**2 + C**2 - B**2) / (2*C*A))
                        rad_to_deg = b * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle b = ", round(rad_to_deg, 2))
                        
                    else :
                        print("")
                        print("incorrect triangle!")

            # when side b is not given
            elif (B == 0) :
                
                # using angle a, side a and c to find angle c
                if (a_int != 0) and (C != 0) and (A != 0) :
                    deg_to_rad = (a_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * C) / A) < 1) :
                        print("finding angle b using given angles and sine rule...")
                        c = math.asin((math.sin(deg_to_rad) * C) / A)
                        rad_to_deg = c * 180/math.pi
                        # using angles c and a to find angle b
                        b = 180 - (rad_to_deg + a_int)
                        time.sleep(2)
                        print("")
                        print("angle b = ", round(b, 2))

                    else :
                        print("")
                        print("incorrect triangle!")

                # using angle c, side a and c to find angle a
                if (c_int != 0) and (C != 0) and (A != 0) :
                    deg_to_rad = (c_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * A) / C) < 1) :
                        print("finding angle b using given angles and sine rule...")
                        a = math.asin((math.sin(deg_to_rad) * A) / C)
                        rad_to_deg = a * 180/math.pi
                        # using angles c and a to find angle b
                        b = 180 - (rad_to_deg + c_int)
                        time.sleep(2)
                        print("")
                        print("angle b = ", round(b, 2))

                    else :
                        print("")
                        print("incorrect triangle!")





        # finding angle c
        elif (c == "x") :
            
            # when side C is given
            if (C != 0) :
                
                # using angle a, sides C and A to find angle c
                if (a_int != 0) and (A != 0) :
                    deg_to_rad = (a_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * C) / A) < 1) :
                        print("finding angle c using sine rule...")
                        c = math.asin((math.sin(deg_to_rad) * C) / A)
                        rad_to_deg = c * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle c = ", round(rad_to_deg, 2))

                    else :
                        print("incorrect triangle")

                # using angle b, sides C and B to find angle c
                if (b_int != 0) and (B != 0) :
                    deg_to_rad = (b_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * C) / B) < 1) :
                        print("finding angle c using sine rule...")
                        c = math.asin((math.sin(deg_to_rad) * C) / B)
                        rad_to_deg = c * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle c = ", round(rad_to_deg, 2))

                    else :
                        print("incorrect triangle")

                # using sides A, B and C
                if (A != 0) and (B != 0) :
                    if (0 <= (A**2 + B**2 - C**2) / (2*A*B) < 1) :
                        print("finding angle c using cosine rule...")
                        c = math.acos((A**2 + B**2 - C**2) / (2*A*B))
                        rad_to_deg = c * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle c = ", round(rad_to_deg, 2))

                    else :
                        print("")
                        print("incorrect triangle!")

                # using angle a, sides B and C to find side A, using side a, b and c to find angle c
                if (a_int != 0) and (B != 0) :
                    deg_to_rad = (a_int * math.pi)/180
                    A = math.sqrt(B**2 + C**2 - (2 * B * C * math.cos(deg_to_rad)))
                    if (0 <= ((A**2 + B**2 - C**2) / (2*B*A)) < 1) :
                        print("finding angle c using cosine rule..." )
                        c = math.acos((A**2 + B**2 - C**2) / (2*B*A))
                        rad_to_deg = c * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle c = ", round(rad_to_deg, 2))
                        
                    else :
                        print("")
                        print("incorrect triangle!")

                # using angle b, sides A and C to find side B, using side a, b and c to find angle c
                if (b_int != 0) and (A != 0) :
                    deg_to_rad = (b_int * math.pi)/180
                    B = math.sqrt(A**2 + C**2 - (2 * A * C * math.cos(deg_to_rad)))
                    if (0 <= ((A**2 + B**2 - C**2) / (2*B*A)) < 1) :
                        print("finding angle c using cosine rule..." )
                        c = math.acos((A**2 + B**2 - C**2) / (2*B*A))
                        rad_to_deg = c * 180/math.pi
                        time.sleep(2)
                        print("")
                        print("angle c = ", round(rad_to_deg, 2))
                        
                    else :
                        print("")
                        print("incorrect triangle!")

            # when side C is not given
            if (C == 0) :

                # using angle a, sides a and b to find angle b and using angles a and b to find angle c
                if (a_int != 0) and (A != 0) and (B != 0) :
                    deg_to_rad = (a_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * B) / A) < 1) :
                        print("finding angle c using given angles and sine rule...")
                        b = math.asin((math.sin(deg_to_rad) * B) / A)
                        rad_to_deg = b * 180/math.pi
                        # using angles b and a to find angle c
                        c = 180 - (rad_to_deg + a_int)
                        time.sleep(2)
                        print("")
                        print("angle c = ", round(c, 2))

                    else :
                        print("")
                        print("incorrect triangle!")

                    # using angle b, sides a and b to find angle a and using angles a and b to find angle c
                if (b_int != 0) and (A != 0) and (B != 0) :
                    deg_to_rad = (b_int * math.pi)/180
                    if (0 < ((math.sin(deg_to_rad) * A) / B) < 1) :
                        print("finding angle c using given angles and sine rule...")
                        a = math.asin((math.sin(deg_to_rad) * A) / B)
                        rad_to_deg = a * 180/math.pi
                        # using angles b and a to find angle c
                        c = 180 - (rad_to_deg + b_int)
                        time.sleep(2)
                        print("")
                        print("angle c = ", round(c, 2))

                    else :
                        print("")
                        print("incorrect triangle!")






    if calc_type in ('side', 'Side', 'SIDE'):
        print('''This calculator only works on NON right angled triangles. It can find the length of a side. A
                 sample triangle is given below. Please enter values of sides and angles in the given format. Type 0
                 for the unknown angles and sides. TYPE x FOR THE SIDE TO BE FOUND. ''')
        print("")
        print("")
        print('''     
                    ** 
                   ****
                  ******
                 ********
         side B ********** side C 
               ************
              **************
             ****************
            ******************
                  side A
              ''')
        print("")
        print("")
        A = input("enter value of side A:")
        B = input("enter value of side B:")
        C = input("enter value of side C:")
        a = float(input("enter value of angle a:"))
        b = float(input("enter value of angle b:"))
        c = float(input("enter value of angle c:"))
        
        A_int = 0
        B_int = 0
        C_int = 0

        # converts angle input from string to integer type if they are not x or 0
        if (A != "x") and (A != "0") :
            A_int = float(A)
        if (B != "x") and (B != "0") :
            B_int = float(B)
        if (C != "x") and (C != "0") :
            C_int = float(C)

        # checking if user has inputted side to be found
        if (A != "x") and (B != "x") and (C != "x") :
            print("")
            print("please enter side to be found")

        # checks if user has inputted multiple sides to be found
        if ((A == "x") and (B == "x")) or ((A == "x") and (C == "x") or ((B == "x") and (C == "x"))) :
            print("")
            print("program can only find length of one side at a time")

        # checks if atleast size of one side is given
        if (A_int == 0) and (B_int == 0) and (C_int == 0) :
            ("enter size of atleast one side")

        # finding size of third angle if two angles are given
        if (a != 0) and (b != 0) :
            c = 180 - (a + b)
        if (a != 0) and (c != 0) :
            b = 180 - (a + c)
        if (c != 0) and (b != 0) :
            a = 180 - (c + b)
            

        # when angle a is not given (code to find angle a)
        # finding angle a using angle b, sides b and c, and sine rule
        if (a == 0) :
            if (b != 0) and (C_int != 0) and (B_int != 0) :
                deg_to_rad_b = (b * math.pi)/180
                if (0 < ((math.sin(deg_to_rad_b) * C_int) / B_int) < 1) :
                    angle_c = math.asin((math.sin(deg_to_rad_b) * C_int) / B_int)
                    rad_to_deg = angle_c * 180/math.pi
                    # using angles c and b to find angle a
                    a = 180 - (rad_to_deg + b)
                else :
                    print("incorrect triangle")
                    exit()

            # finding angle a using angle c, sides b and c, and sine rule
            if (c != 0) and (C_int != 0) and (B_int != 0) :
                deg_to_rad_c = (c * math.pi)/180
                if (0 < ((math.sin(deg_to_rad_c) * B_int) / C_int) < 1) :
                    angle_b = math.asin((math.sin(deg_to_rad_c) * B_int) / C_int)
                    rad_to_deg = angle_b * 180/math.pi
                    # using angles c and b to find angle a
                    a = 180 - (rad_to_deg + c)
                else :
                    print("incorrect triangle")
                    exit()


        # when angle b is not given (code to find angle b)
        # finding angle b using angle c, sides a and c, and sine rule
        if (b == 0) :
            if (c != 0) and (C_int != 0) and (A_int != 0) :
                deg_to_rad_c = (c * math.pi)/180
                if (0 < ((math.sin(deg_to_rad_c) * A_int) / C_int) < 1) :
                    angle_a = math.asin((math.sin(deg_to_rad_c) * A_int) / C_int)
                    rad_to_deg = angle_a * 180/math.pi
                    # using angles c and a to find angle b
                    b = 180 - (rad_to_deg + c)
                else :
                    print("incorrect triangle")
                    exit()

            # finding angle a using angle a, sides a and c, and sine rule
            if (a != 0) and (C_int != 0) and (A_int != 0) :
                deg_to_rad_a = (a * math.pi)/180
                if (0 < ((math.sin(deg_to_rad_a) * C_int) / A_int) < 1) :
                    angle_c = math.asin((math.sin(deg_to_rad_a) * C_int) / A_int)
                    rad_to_deg = angle_c * 180/math.pi
                    # using angles c and a to find angle b
                    b = 180 - (rad_to_deg + a)
                else :
                    print("incorrect triangle")
                    exit()



        # when angle c is not given (code to find angle c)
        # finding angle c using angle a, sides a and b, and sine rule
        if (c == 0) :
            if (a != 0) and (B_int != 0) and (A_int != 0) :
                deg_to_rad_a = (a * math.pi)/180
                if (0 < ((math.sin(deg_to_rad_a) * B_int) / A_int) < 1) :
                    angle_b = math.asin((math.sin(deg_to_rad_a) * B_int) / A_int)
                    rad_to_deg = angle_b * 180/math.pi
                    # using angles b and a to find angle c
                    c = 180 - (rad_to_deg + a)
                else :
                    print("incorrect triangle")
                    exit()

            # finding angle c using angle b, sides a and b, and sine rule
            if (b != 0) and (B_int != 0) and (A_int != 0) :
                deg_to_rad_b = (b * math.pi)/180
                if (0 < ((math.sin(deg_to_rad_b) * A_int) / B_int) < 1) :
                    angle_a = math.asin((math.sin(deg_to_rad_b) * A_int) / B_int)
                    rad_to_deg = angle_a * 180/math.pi
                    # using angles b and a to find angle c
                    c = 180 - (rad_to_deg + b)
                else :
                    print("incorrect triangle")
                    exit()



                    
        # when side A is x
        if (A == "x") :

            # when size of angle a is given
            if (a != 0) :
            
                # when side b and angle b are given, finding side a using sine
                if (b != 0) and (B_int != 0) :
                    print("")
                    deg_to_rad_a = (a * math.pi)/180
                    deg_to_rad_b = (b * math.pi)/180
                    if (math.sin(deg_to_rad_b) != 0) and (math.sin(deg_to_rad_a) != 0) :
                        print("finding length of side a using sine rule...")    
                        A = (B_int * math.sin(deg_to_rad_a) / math.sin(deg_to_rad_b))
                        time.sleep(2)
                        print("side A = ", round(A, 2), "1")
                    
                    else :
                        print("incorrect triangle 1")
                    

                # when side c and angle c are given, finding side a using sine
                if (c != 0) and (C_int != 0) :
                    print("")
                    deg_to_rad_a = (a * math.pi)/180
                    deg_to_rad_c = (c * math.pi)/180
                    if (math.sin(deg_to_rad_c) != 0) and (math.sin(deg_to_rad_a) != 0) :
                        print("finding length of side a using sine rule...")    
                        A = (C_int * math.sin(deg_to_rad_a) / math.sin(deg_to_rad_c))
                        time.sleep(2)
                        print("side A = ", round(A, 2), "2")
                        
                    else :
                        print("incorrect triangle 2")


                # when sides b and c are given, finding side a using cosine
                if (B_int != 0) and (C_int != 0) :
                    if (b == 0) and (c == 0) :
                        print("")
                        deg_to_rad_a = (a * math.pi)/180
                        if ((B_int**2 + C_int**2) > ((2 * B_int * C_int * math.cos(deg_to_rad_a)))) :
                            print("finding length of side a using cosine rule...")    
                            A = math.sqrt(B_int**2 + C_int**2 - (2 * B_int * C_int * math.cos(deg_to_rad_a)))
                            time.sleep(2)
                            print("side A = ", round(A, 2), "3")
                            
                        else :
                            print("incorrect triangle 3")




        # when side b is x
        if (B == "x") :

            # when size of angle b is given
            if (b != 0) : 

                # when side a and angle a are given, finding side a using sine
                if (a != 0) and (A_int != 0) :
                    print("")
                    deg_to_rad_a = (a * math.pi)/180
                    deg_to_rad_b = (b * math.pi)/180
                    if (math.sin(deg_to_rad_b) != 0) and (math.sin(deg_to_rad_a) != 0) :
                        print("finding length of side b using sine rule...")    
                        B = (A_int * math.sin(deg_to_rad_b) / math.sin(deg_to_rad_a))
                        time.sleep(2)
                        print("side B = ", round(B, 2), "4")
                    
                    else :
                        print("incorrect triangle 4")


                # when side c and angle c are given, finding side a using sine
                if (c != 0) and (C_int != 0) :
                    print("")
                    deg_to_rad_c = (c * math.pi)/180
                    deg_to_rad_b = (b * math.pi)/180
                    if (math.sin(deg_to_rad_b) != 0) and (math.sin(deg_to_rad_c) != 0) :
                        print("finding length of side b using sine rule...")    
                        B = (C_int * math.sin(deg_to_rad_b) / math.sin(deg_to_rad_c))
                        time.sleep(2)
                        print("side B = ", round(B, 2), "5")
                    
                    else :
                        print("incorrect triangle 5")


                # when sides a and c are given, finding side a using cosine
                if (A_int != 0) and (C_int != 0) :
                    if (a == 0) and (c == 0) :
                        print("")
                        deg_to_rad_b = (b * math.pi)/180
                        if ((A_int**2 + C_int**2) > ((2 * A_int * C_int * math.cos(deg_to_rad_b)))) :
                            print("finding length of side b using cosine rule...")    
                            B = math.sqrt(A_int**2 + C_int**2 - (2 * A_int * C_int * math.cos(deg_to_rad_b)))
                            time.sleep(2)
                            print("side B = ", round(B, 2), "6")
                            
                        else :
                            print("incorrect triangle 6")





        # when side c is x
        if (C == "x") :

            # when size of angle c is given
            if (c != 0) : 

                # when side a and angle a are given, finding side a using sine
                if (a != 0) and (A_int != 0) :
                    print("")
                    deg_to_rad_a = (a * math.pi)/180
                    deg_to_rad_c = (c * math.pi)/180
                    if (math.sin(deg_to_rad_c) != 0) and (math.sin(deg_to_rad_a) != 0) :
                        print("finding length of side c using sine rule...")    
                        C = (A_int * math.sin(deg_to_rad_c) / math.sin(deg_to_rad_a))
                        time.sleep(2)
                        print("side C = ", round(C, 2), "7")
                    
                    else :
                        print("incorrect triangle 7")


                # when side b and angle b are given, finding side a using sine
                if (b != 0) and (B_int != 0) :
                    print("")
                    deg_to_rad_c = (c * math.pi)/180
                    deg_to_rad_b = (b * math.pi)/180
                    if (math.sin(deg_to_rad_b) != 0) and (math.sin(deg_to_rad_c) != 0) :
                        print("finding length of side c using sine rule...")    
                        C = (B_int * math.sin(deg_to_rad_c) / math.sin(deg_to_rad_b))
                        time.sleep(2)
                        print("side C = ", round(C, 2), "8")
                    
                    else :
                        print("incorrect triangle 8")


                # when sides a and b are given, finding side a using cosine
                if (A_int != 0) and (B_int != 0) :
                    if (a == 0) and (b == 0) :
                        print("")
                        deg_to_rad_c = (c * math.pi)/180
                        if ((A_int**2 + B_int**2) > ((2 * A_int * B_int * math.cos(deg_to_rad_c)))) :
                            print("finding length of side c using cosine rule...")    
                            C = math.sqrt(A_int**2 + B_int**2 - (2 * A_int * B_int * math.cos(deg_to_rad_c)))
                            time.sleep(2)
                            print("side C = ", round(C, 2), "9")
                            
                        else :
                            print("incorrect triangle 9")
                        
                        








