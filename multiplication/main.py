from re import A


while True:

    num = int(input("Please input number of what multiplication table you want?: "))

    def output(x, num):
        multiplier = x + 1
        total = multiplier * num
        return f"{multiplier} * {num} = {total}"

    if type(num) != int:
        print("Please input number!")
        continue

    mx = [output(x, num) for x in range(20)]

    print(mx)
