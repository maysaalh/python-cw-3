# write your code here
#part1
Favourite_animals = ['dog', 'cat', 'monkey', 'rabbit']
print(Favourite_animals)
Favourite_animals.remove('monkey')
print(Favourite_animals)
#part2
Favourite_animals.append('hamster')
print(Favourite_animals)
for favourite_animal in Favourite_animals:
 print(f"I LOVE {favourite_animal}")
#PART3
numbers=[5,4,3,2,1]
number_sum=0
for nums in numbers:
    number_sum=number_sum + nums
print(number_sum)