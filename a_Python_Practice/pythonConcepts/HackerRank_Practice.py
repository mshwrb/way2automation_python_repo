from operator import itemgetter


class Problems:

    # _name__ == '__main__':
    # first_name = input()
    # last_name = input()
    # print_full_name(first_name, last_name)

    @staticmethod
    def a():
        x = int(input())
        y = int(input())
        z = int(input())
        n = int(input())
        lst = []
        output = [lst.append([i, j, k]) for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if
                  n != i + j + k]
        return lst

    # https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
    @staticmethod
    def nested_list():
        name_list = ["Harry", "Berry", "Tina", "Akriti", "Harsh", "kirti"]
        score_list = [37.21, 37.21, 37.2, 41, 39, 37.2]
        result = []
        final_items = []
        for i in range(len(name_list)):
            result.append([name_list[i], score_list[i]])
        result.sort(key=lambda x: x[1])
        print("sorted : ", result)
        lowest = result[0][1]
        lowest2 = None
        for i in range(0, len(result)):
            if result[i][1] < lowest:
                lowest2 = lowest
                lowest = result[i][1]
            elif result[i][1] == lowest:
                continue
            elif lowest2 is None or lowest2 >= result[i][1]:
                lowest2 = result[i][1]
                final_items.append(result[i])
        final_items.sort(key=lambda x: x[0])
        for i in range(len(final_items)):
            print(final_items[i][0])

    @staticmethod
    def finding_percentage():
        student_marks = {"Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60]}
        query_name = "Malika"
        print("%.2f" % (sum(student_marks[query_name]) / len(student_marks[query_name])))

    @staticmethod
    def mutate_string(string, position, character):
        print(string[:position] + character + string[position + 1:])

    @staticmethod
    def count_substring(string, sub_string):
        count = 0
        for i in range(len(string)):
            if string[i:i + len(sub_string)] == sub_string:
                count += 1
        return count

    @staticmethod
    def string_validation(s):
        s = "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
        for n in s:
            if n.isalnum():
                print(True)
                break
        else:
            print(False)
        for n in s:
            if n.isalpha():
                print(True)
                break
        else:
            print(False)
        for n in s:
            if n.isdigit():
                print(True)
                break
        else:
            print(False)
        for n in s:
            if n.isalpha() and n.islower():
                print(True)
                break
        else:
            print(False)
        for n in s:
            if n.isalpha() and n.isupper():
                print(True)
                break
        else:
            print(False)

    @staticmethod
    def python_tuples():
        n = 2
        integer_list = [1, 2]
        print(hash(tuple(integer_list)))

    @staticmethod
    def swap_case(s):
        s1 = ""
        print("k96.5gi.SABdh3S.6IfZXmaH5ipTMwj4W0Uj9mowc45EOzKHAsS73GXkOqCD90uGE02CaXpNYmwTyw'trvCo.0vNbQ.Siq5hfHKX")
        for n in s:
            if n.isalpha() and n.isupper():
                s1 = s1 + n.lower()
            elif n.isalpha() and n.islower():
                s1 = s1 + n.upper()
            elif n.isspace() or n == "\"" or n.isnumeric() or n == "." or n == "'":
                s1 = s1 + n
        return s1



print(Problems.swap_case("K96.5GI.sabDH3s.6iFzxMAh5IPtmWJ4w0uJ9MOWC45eoZkhaSs73gxKoQcd90Uge02cAxPnyMWtYW'TRVcO.0VnBq.sIQ5HFhkx"))
