number = int(input("Enter a number: "))
digits_count = len(str(number))
even_counter = 0

for i in range(1, digits_count + 1):
    current_digit = (number // 10 ** (digits_count - i)) % 10
    
    if current_digit % 2 == 0:
        even_counter += 1
        print(even_counter, "-th even digit is ", current_digit, sep='')

if even_counter == 0:
    print("There are no even digits in the number.")
