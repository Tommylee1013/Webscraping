def print_hello(): print('hello')
def print_message(phrase): print(phrase)
def game(number) :
    if number == 1 : print('attack')
    elif number == 2 : print('deffense')
def plus(v1, v2) : return (v1 + v2)
def main() :
    input0 = "hello"
    print(type(input0))
    print_message("hello")

    input1 = 10
    print(type(input1))
    print_message(input1)

    input2 = [10]
    print(type(input2))
    print_message(input2)

    input3 = {10}
    print(type(input3))
    print_message(input3)

    print(game(2))

    result1 = plus(10, 15)
    print(f'result = {result1}')

if __name__ == '__main__' : main()