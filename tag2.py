file_path = '/Users/dennis.vonderstueck/Ausbildung/Advent/2tag.txt'

with open(file_path, 'r') as test_file:
    lines = test_file.readlines()
    Highscore = 0
    for line in lines:
        
         #Lose
        if "A" in line and "X" in line:
            Highscore += 3
            
        if "B" in line and "X" in line:
            Highscore += 1
            
        if "C" in line and "X" in line:
            Highscore += 2
         
         # Draw
        if "A" in line and "Y" in line:
         Highscore += 4

        if "B" in line and "Y" in line:
         Highscore += 5

        if "C" in line and "Y" in line:
         Highscore += 6
         
         # Winner
        if "A" in line and "Z" in line:
         Highscore += 8

        if "B" in line and "Z" in line:
         Highscore += 9

        if "C" in line and "Z" in line:
         Highscore += 7
           
            

       

print(Highscore)
