

file_path = '/Users/dennis.vonderstueck/Ausbildung/Advent/1tag.txt'

with open(file_path, 'r') as test_file:
    
    #lines = test_file.read().splitlines()
    lines = test_file.readlines()
    ZwischenErgebniss = 0
    Highscore = 0

    
    for number in lines:
     number = int(number.strip()or 0 )
     ZwischenErgebniss = ZwischenErgebniss + number
     if number == 0:
        if Highscore < ZwischenErgebniss:     
            Highscore = ZwischenErgebniss
        ZwischenErgebniss = 0

    
      
print(Highscore)
