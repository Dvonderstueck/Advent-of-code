file_path = '/Users/dennis.vonderstueck/Ausbildung/Advent/2tag.txt'

with open(file_path, 'r') as test_file:
    lines = test_file.readlines()
    Highscore = 0
    for line in lines:
        if "A" in line and "X" in line:
            line = line.replace("X", "C")
            Highscore += 3
            
        if "B" in line and "X" in line:
            line = line.replace("X", "A")
            Highscore += 1
            
        if "C" in line and "X" in line:
            line = line.replace("X", "B")
            Highscore += 2

        if "A" in line and "Y" in line:
            line = line.replace("Y", "A")
            Highscore += 1
            Highscore += 3

        if "B" in line and "Y" in line:
            line = line.replace("Y", "B")
            Highscore += 2
            Highscore += 3

        if "C" in line and "Y" in line:
            line = line.replace("Y", "C")
            Highscore += 3
            Highscore += 3

        if "A" in line and "Z" in line:
            line = line.replace("Z", "B")
            Highscore += 2
            Highscore += 6

        if "B" in line and "Z" in line:
            line = line.replace("Z", "C")
            Highscore += 3
            Highscore += 6

        if "C" in line and "Z" in line:
            line = line.replace("Z", "A")
            Highscore += 1
            Highscore += 6
            

       

print(Highscore)
