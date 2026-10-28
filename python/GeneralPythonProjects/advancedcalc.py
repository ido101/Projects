while True:
    prob = input("Enter a math problem (type 'q' to quit): ")
    if prob == 'q':
        quit()
    signs = ["+", "*", "x", "-", "/"]
    sign = ''
    for s in signs:
        if s in prob:
            sign = s
    nums = prob.split(sign)
    nums[0],nums[1] = int(nums[0]), int(nums[1])
    if sign == "+":
        print(sum(nums))
    elif sign == "/":
        print(nums[0] / nums[1])
    elif sign in ["*", "x"]:
        print(nums[0] * nums[1])
    elif sign == "-":
        print(nums[0] - nums[1])
