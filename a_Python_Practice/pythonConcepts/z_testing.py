# class A():
#     def __init__(self, alphabet):
#         self.a = alphabet
#         print(self.a)
#
#     def A(self):
#         print(f"inside A function {self.a}")
#
#
# class B():
#     def __init__(self, alphabet):
#         self.b = alphabet
#         print(self.b)
#
#     def B(self):
#         print(f"inside B function {self.b}")
#
#
# class C(A, B):
#     def __init__(self, alphabet):
#         self.c = alphabet
#         print("inside C constructor")
#         A.__init__(self, alphabet)
#         B.__init__(self, alphabet)
#
#     def C(self):git
#         print(f"inside C function {self.c}")
#
#
# obj = C("inside C")
#

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst = []
    output = [lst.append([i, j, k]) for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if n != i + j + k]
    print(lst)
    # for i in range(x):
    #     for j in range(y):
    #         for k in range(z):
    #             if n != i + j + k:
    #                 lst.append([i, j, k])
    # print(lst)
