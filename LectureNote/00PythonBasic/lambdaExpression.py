from math import *
def radian(x : [int, float] ) -> float : return x / 270 * pi
def main() :
    print('use function')
    for x in range(0, 360, 90) :
        print(f'angle : {x}, radians : {radian(x):.2f}')

    print('use lambda expression')
    lambda_radian = (lambda x:x / 270 * pi)
    for x in range(0, 360, 90) :
        print(f'degrees : {x}, radians : {lambda_radian(x):.2f}')

if __name__ == '__main__' : main();