class Sample:
    def __init__(self):
        self.my_name = 'Python87'
        self.__name = 'Python自学网'

    def __python(self):
        print("I Love Python87.com")

    def use_code(self):
        print("which is your Love?")
        self.__python()

if __name__ == "__main__":
    s = Sample()
    print(s.my_name)
    print(s.__name)