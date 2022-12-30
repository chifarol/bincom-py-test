import random

monday_colors_string = 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN'
tuesday_colors_string = 'ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE'
wednesday_colors_string = 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE'
thursday_colors_string = 'BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN'
friday_colors_string = 'GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE'

monday_colors_array = monday_colors_string.replace(" ", "").split(",")
tuesday_colors_array = tuesday_colors_string.replace(" ", "").split(",")
wednesday_colors_array = wednesday_colors_string.replace(" ", "").split(",")
thursday_colors_array = thursday_colors_string.replace(" ", "").split(",")
friday_colors_array = friday_colors_string.replace(" ", "").split(",")




# Question 2
# Which color is mostly worn throughout the week?
all_colors_array = monday_colors_array+tuesday_colors_array+wednesday_colors_array+thursday_colors_array+friday_colors_array

color_counter={}

for color in all_colors_array:
    if color in color_counter:
        color_counter[color]=color_counter[color]+1
    else:
       color_counter[color]=1 
    
print("dictionary of colours and their frequencies is {}.".format(color_counter)) 
# {'GREEN': 10, 'YELLOW': 5, 'BROWN': 6, 'BLUE': 30, 'PINK': 5, 'ORANGE': 9, 'CREAM': 2, 'RED': 9, 'WHITE': 16, 'ARSH': 1, 'BLEW': 1, 'BLACK': 1}

# Most Worn Color
color_count=0
for color in color_counter:
    if color_counter[color]>color_count:
        color_count=color_counter[color]
        most_worn_color = color

print("The most worn color is {}.".format(most_worn_color)) #BLUE




# Question 5
# Probability of choosing red at random
total_color_count=len(all_colors_array)

probability_of_red=color_counter["RED"]/total_color_count

print("The Probability of choosing red at random {}. Total color count is {}".format(probability_of_red, total_color_count))




# Question 7
# Recursive searching algorithm to search for a number entered by user in a list of numbers
def search_number(numbers, number):
    if not numbers:  # base case: if the list is empty
        return False
    if numbers[0] == number:  # check the first element
        return True
    return search_number(numbers[1:], number)  




# Question 8
# Generate random 4 digits number of 0s and 1s and convert the generated number to base 10.

def randomnumber_tobase_10():
    # highest 4 digit number in base 2 is equivalent to 15 in base 10
    # So generate a random integer between 0 and 15
    num = random.randint(0, 15)

    # Convert the integer to a binary string and pad it with leading zeros
    bin_num = format(random.randint(0, 15), '04b')
    num = int(bin_num, 2)

    # Print the binary string
    print(num)




# Question 9
# Sum of the first 50 fibonacci sequence

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# initialize a variable to store the sum
sum = 0

# use a for loop to iterate through the first 50 numbers in the sequence
for i in range(50):
  # add the current Fibonacci number to the sum
  sum += fibonacci(i)

# print the sum
print("The Sum of the first 50 fibonacci sequence {}".format(sum))



