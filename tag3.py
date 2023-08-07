file_path = '/Users/dennis.vonderstueck/Ausbildung/Advent/3tag.txt'

with open(file_path, 'r') as test_file:
        lines = test_file.readlines()
        rucksacks = [line.strip() for line in lines]

        rucksack_sum = 0
for rucksack in rucksacks:
    
        first_half = set(rucksack[:len(rucksack)//2])
        second_half = set(rucksack[len(rucksack)//2:])

overlap_chars = (first_half.intersection(second_half)).pop()

if overlap_chars.isupper():
     rucksack_sum += ord(overlap_chars) 






print(rucksack_sum)