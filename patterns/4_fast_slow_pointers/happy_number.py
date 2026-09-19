

def happy_num(num:int) -> bool :
    fast = slow = num
    while True:
        slow = get_next_num(slow)
        fast = get_next_num(get_next_num(fast))

        if fast == 1:
            return True
        elif fast == slow:
            print(f"Found loop->{fast} and {slow}")
            break
            #return False


def get_next_num(num:int) -> int:
    # num is 23
    sum = 0
    print(f"get_next_num for {num}")
    while num > 0:
        digit = num % 10
        num //= 10
        sum += digit ** 2 
    print(f"is {sum} ")
    return sum


if __name__ == '__main__':
    print("Hello world!")
    #get_next_num(23)

    happy_num(43)

