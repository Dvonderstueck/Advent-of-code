file_path = '/Users/dennis.vonderstueck/Ausbildung/Advent/2tag.txt'

with open(file_path, 'r') as test_file:
    lines = test_file.readlines()
    Highscore = 0
    for line in lines:
            if "X" in line and "A" in line:
                Highscore += 3
            
            if "B" in line and "Y" in line:
                Highscore += 3
            
            if "C" in line and "Z" in line:
                Highscore += 3

            if "C" in line and "X" in line:
                Highscore += 6

            if "A" in line and "Y" in line:
                Highscore += 6

            if "B" in line and "Z" in line:
                Highscore += 6

    for line in lines:
        Rock = 1
        Paper = 2
        Scissors = 3
        A, X = Rock, Rock
        B, Y = Paper, Paper
        C, Z = Scissors, Scissors
        if "X" in line:
            Highscore += 1
        if "Y" in line:
            Highscore += 2
        if "Z" in line:
            Highscore += 3

    
print(Highscore)
