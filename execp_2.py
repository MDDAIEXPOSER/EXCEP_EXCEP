"""
Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация, то есть соединение, строк.
В остальных случаях введенные числа суммируются.
"""

def digit(type_1, type_2):
        try:
            return int(type_1) + int(type_2)
        except:
            return str(type_1) + str(type_2)

def main():
        print(digit(str(input()), str(input())))


if __name__ == "__main__":
  main()
