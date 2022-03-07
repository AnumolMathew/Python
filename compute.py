def compute_letter(str):
    upper=0
    lower=0
    for i in range(0, len(str)):
        if str[i] == 'A' or str[i] == "B" or str[i] == "C" or str[i] == "D" or str[i] == 'E' or str[i] == "F" or str[
            i] == "G" or str[i] == "H" or str[i] == "I" or str[i] == "J" or str[i] == 'K' or str[i] == "L" or str[
            i] == "M" or str[i] == "N" or str[i] == "O" or str[i] == "P" or str[i] == 'Q' or str[i] == "R" or str[
            i] == "S" or str[i] == "T" or str[i] == "U" or str[i] == "V" or str[i] == 'W' or str[i] == "X" or str[
            i] == "Y" or str[i] == "Z":
            upper += 1
        elif str[i] == 'a' or str[i] == "b" or str[i] == "c" or str[i] == "d" or str[i] == 'e' or str[i] == "f" or str[
            i] == "g" or str[i] == "h" or str[i] == "i" or str[i] == "j" or str[i] == 'k' or str[i] == "l" or str[
            i] == "m" or str[i] == "n" or str[i] == "o" or str[i] == "p" or str[i] == 'q' or str[i] == "r" or str[
            i] == "s" or str[i] == "t" or str[i] == "u" or str[i] == "v" or str[i] == 'w' or str[i] == "x" or str[
            i] == "y" or str[i] == "z":
            lower += 1
    print("number of uppercase letters in the string are:", upper)
    print("number of lowercase letters in the string are:", lower)