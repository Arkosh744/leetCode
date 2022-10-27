def subtractProductAndSum(n: int) -> int:
    numbers = []
    product = 1
    summa = 0
    for i in str(n):
        numbers.append(int(i))
    for i in numbers:
        product *= i
    return product - sum(numbers)

