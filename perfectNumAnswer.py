def check_perfect_number(n: int) :
    sum_variable = 0
    for i in range(1, n):
        if n % i == 0:
            sum_variable = sum_variable + i
    if sum_variable == n:
        print(f"The number {input_number} is perfect number")
    else:
        print(f"The number {input_number} is not a perfect number")
    
input_number = int(input("Enter number to be checked: "))
check_perfect_number(input_number)
