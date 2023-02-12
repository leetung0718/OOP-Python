class ClassA:
    # 類別屬性
    attr = 1

    # 屬性特性
    @property
    def getInfo(self):
        return print("This is class A.")

    # 實體方法(Instance Method)
    def instance_method(self, char):
        print(char)

    # 類別方法(Class Method)
    @classmethod
    def class_method(cls, char):
        print(char)

    # 靜態方法(Static Method)
    @staticmethod
    def static_method(char):
        print(char)


if __name__ == '__main__':
    # instance method
    instance = ClassA()
    instance.instance_method("instance method")  # instance method

    # property
    instance.getInfo

    # static method
    print(ClassA.attr)  # classA's attr = 1
    ClassA.static_method("static method")  # static method

    # class method
    ClassA.class_method("class method")  # class method
