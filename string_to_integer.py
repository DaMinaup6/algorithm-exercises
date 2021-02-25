def myAtoi(s):
    digit_read = False
    sign_read  = False
    negative   = False
    num_arr    = []

    for char in s:
        if (digit_read or sign_read) and not char.isdigit():
            break

        if char == ' ':
            continue
        elif char == '+':
            sign_read = True
        elif char == '-':
            sign_read = True
            negative  = True
        elif char.isdigit():
            digit_read = True
            num_arr.append(int(char))
        else:
            break

    if len(num_arr) == 0:
        return 0
    else:
        output = 0
        for idx, num in enumerate(num_arr):
            output += num * 10 ** (len(num_arr) - 1 - idx)
        if negative:
            output *= -1

        return max(min(output, 2 ** 31 - 1), -2 ** 31)

print(f"myAtoi('00+- 123'):      correct: {myAtoi('00+- 123') == 0}")
print(f"myAtoi('00-+ 123'):      correct: {myAtoi('00-+ 123') == 0}")
print(f"myAtoi('00- 123'):       correct: {myAtoi('00- 123') == 0}")
print(f"myAtoi('+-12'):          correct: {myAtoi('+-12') == 0}")
print(f"myAtoi('00000-42a1234'): correct: {myAtoi('00000-42a1234') == 0}")
print(f"myAtoi('- 123'):         correct: {myAtoi('- 123') == 0}")
print(f"myAtoi('02-+ 123'):      correct: {myAtoi('02-+ 123') == 2}")
print(f"myAtoi('12 345 6'):      correct: {myAtoi('12 345 6') == 12}")
print(f"myAtoi('00123-'):        correct: {myAtoi('00123-') == 123}")
