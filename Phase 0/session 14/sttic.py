class Math:

    @staticmethod
    def add(a,b):

        return a+b


Math.add(10,20)

class Student:

    count = 0

    @classmethod
    def show_count(cls):

        print(cls.count)