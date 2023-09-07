
def addNums(start : int = 1, end : int = 10) :
    result = 0
    for i in range(start, end + 1) : result += i;
    return result

def main() : addNums();

if __name__ == '__main__' : main();
