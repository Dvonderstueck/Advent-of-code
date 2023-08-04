file_path = '/Users/dennis.vonderstueck/Ausbildung/Advent/1tag.txt'

with open(file_path, 'r') as test_file:
    lines = test_file.readlines()
    ZwischenErgebniss = 0
    Highscore = 0
    meineListe = []  

    for line in lines:
        number = int(line.strip() or 0)
        ZwischenErgebniss += number
        if number == 0:
            if Highscore < ZwischenErgebniss:    
                Highscore = ZwischenErgebniss
            meineListe.append(ZwischenErgebniss)  
            ZwischenErgebniss = 0

    meineListe.sort(reverse=True)  
    last_three_highest = meineListe[:3] 

print("List:", meineListe)
print("Last three highest:", last_three_highest)
