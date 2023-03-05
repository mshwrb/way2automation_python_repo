import calendar
import math
import multiprocessing
import os
import platform
import site
import struct
import sys
from datetime import datetime
from math import pi
from subprocess import call


class PythonBasicPart_1:
    def question_1_escape_chars(self):
        print(
            "Twinkle, twinkle, little star,\n\t\tHow I wonder what you are!\n\t\t\t\tUp above the world so high,\n\t\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are")

    def question_2_versions_info(self):
        print("Python Version")
        print(sys.version)
        print("version info")
        print(sys.version_info)
        print("platform version")
        print(platform.version())
        print(platform.machine())
        print(platform.architecture())

    def question_3_date_time(self):
        print(datetime.datetime.now())
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))

    def question_4_circle_area(self):
        radius = float(input("Input the radius of the circle: "))
        circle_area = pi * radius * radius
        print("area of circle of radius " + str(radius) + " is " + str(circle_area))

    def question_5_concatination(self):
        fName = input("Enter First Name: ")
        lName = input("Enter Last Name: ")
        print(lName + " " + fName)

    def question_6_split(self):
        user_input_values = input("Enter comma seperated numbers: ")
        user_list = user_input_values.split(",")
        user_tuple = tuple(user_list)
        print('list ', user_list)
        print('tuple ', user_tuple)

    def question_7_split(self):
        fileName = input("Input the fileName: ")
        file_extention = fileName.split(".")
        print("The extention of the file is " + file_extention[1])

    def question_8_indexing(self, color_list):
        print("first item in color list is: " + color_list[0])
        print("last item in color list is: " + color_list[-1])

    def question_9_i_specifier(self):
        exam_st_date = (11, 12, 2014)
        print("The examination will start from : %i / %i / %i" % exam_st_date)

    def question_10_s_specifier(self):
        a = int(input("input an integer: "))
        n1 = int("%s" % a)
        n2 = int("%s%s" % (a, a))
        n3 = int("%s%s%s" % (a, a, a))
        print(n1 + n2 + n3)

    def question_11_doc(self):
        print(abs.__doc__)

    def question_12_calender(self):
        y = int(input("Enter the year: "))
        m = int(input("Enter the month: "))
        print(calendar.month(y, m))

    def question_13_multiline_coment(self):
        print("""
        a string that you "don't" have to escape
        This
        is a  ....... multi-line
        heredoc string --------> example
        """)

    def question_14_date_difference(self):
        first_date = input('enter the first date in yyyy,mm,dd format: ')
        second_date = input('enter the second date in yyyy,mm,dd format: ')
        first_date_obj = datetime.strptime(first_date, '%Y,%m,%d')
        second_date_obj = datetime.strptime(second_date, '%Y,%m,%d')
        delta = second_date_obj - first_date_obj
        print(delta.days)

    def question_15_sphere_volume(self, radius):
        sphere_volume = (4 / 3) * pi * radius ** 3  # ** used for exponential
        print(sphere_volume)

    def question_16_difference(self, number):
        difference = 0
        if number > 17:
            difference = (number - 17) * 2
        elif number <= 17:
            difference = 17 - number
        print(difference)

    def question_18_sum(self, n1, n2, n3):
        sum = n1 + n2 + n3
        if n1 == n2 == n3:
            print(sum)
        else:
            print(sum * 3)

    def question_19_string(self, str):
        if len(str) >= 2 and str[:2] == "Is":
            print(str)
        else:
            print("Is" + str)

    def question_20_n_copies(self, str, n):
        result = ""
        for i in range(n):
            result = result + str
        print(result)

    def question_21_odd_even(self):
        n = int(input("Enter the number: "))
        if n % 2 == 0 or n == 0:
            print("The given number is even")
        else:
            print("The given number is odd")

    def question_22_count(self, list, number):
        count = 0
        for i in list:
            if i == number:
                count += 1
        print(count)

    def question_23_copies(self, str, n):
        result = ""
        if 2 >= len(str) > 0:
            for i in range(n):
                result = result + str
        else:
            for i in range(n):
                result = result + str[:2]
        print(result)

    def question_24(self, letter):
        all_vowels = 'aeiouAEIOU'
        print(letter in all_vowels)

    def question_25(self, value, group):
        print(value in group)

    def question_26_histogram(self, list):
        for n in list:
            output = ""
            times = n
            while times > 0:
                output = output + '*'
                times -= 1
            print(output)

    def question_27_concatination(self, list):
        string = ""
        for i in list:
            string = string + str(i)
        print(int(string))

    def question_28_all_even_numbers(self, list):
        for i in list:
            if i == 237:
                print(i)
                break
            elif i % 2 == 0:
                print(i)

    def question_29_set_difference(self):
        color_list_1 = {"White", "Black", "Red"}
        color_list_2 = {"Red", "Green"}
        print(color_list_1.difference(color_list_2))
        print(color_list_2.difference(color_list_1))

    def question_30_triangle_area(self, base, height):
        area = base * height * (1 / 3)
        print(area)

    def question_31_gcd(self, num_1, num_2):
        print(math.gcd(num_1, num_2))

    def question_32_lcm(self, num_1, num_2):
        print(math.lcm(num_1, num_2))

    def question_33(self, n1, n2, n3):
        print(0) if (n1 == n2 or n2 == n3 or n1 == n3) else print(n1 + n2 + n3)

    def question_34(self, n1, n2):
        print(20) if (20 > n1 + n2 > 15) else print(n1 + n2)

    def question_35(self, n1, n2):
        if (n1 == n2) or (abs(n1 - n2) == 5) or (n1 + n2 == 5):
            print(True)
        else:
            print(False)

    def question_36(self, n1, n2):
        if not (isinstance(n1, int) and isinstance(n2, int)):
            return print("Either or both objects are not integers")
        return print(n1 + n2)

    def question_37_personalDetails(self):
        name, age = "Keshav", 31
        address = "Flat no.106, 6th floor, shashi apartments, sector 31, gurugram"
        print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

    def question_38(self, x, y):
        print((x + y) ** 2)

    def question_40(self, list1, list2):
        print(math.sqrt(((list1[0] - list2[0]) ** 2) + ((list1[1] - list2[1]) ** 2)))

    def question_41(self):
        print(os.path.isfile('main.py'))

    def question_42(self):
        print(platform.architecture()[0])
        print(struct.calcsize("P") * 8)

    def question_43(self):
        print(os.name)
        print(platform.system())
        print(platform.release())

    def question_44(self):
        print(site.getsitepackages())

    def question_45(self):
        print(call(["ls", "-l"]))

    def question_46(self):
        print(os.path.realpath(__file__))

    def question_47(self):
        print(multiprocessing.cpu_count())

    def question_48(self):
        n = "246.2458"
        print(float(n))
        print(int(float(n)))

    def fabonachi_series(self, nterms):
        n1, n2 = 0, 1
        count = 0
        fabonachi_list = []
        while count < nterms:
            fabonachi_list.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
        return fabonachi_list

object = PythonBasicPart_1()
print(object.fabonachi_series(5))
