class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    # TODO Написать статический метод add для сложения двух чисел

    @staticmethod
    def mul(a, b):
        return a * b # TODO  Написать статический метод mul для умножения двух чисел


if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
