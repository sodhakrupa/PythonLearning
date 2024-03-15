
def prime_checker(number):
    is_prime = True
    for n in range(2,number):
        if num % n == 0:
            is_prime = False
            break

    print(f"Is Prime {is_prime}")

num = int(input("Enter any number between 1 to 100\n"))
prime_checker(num)