def roman_to_integer(x):
    roman_numerals_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    if len(x) >= 1 and len(x) <= 15:
        try:
            for i in range(len(x)):
                if (x[i:i+4] in ["MMMM", "CCCC", "XXXX", "IIII"]
                or any(list(x).count(ixcm) > 4 for ixcm in ["I", "X", "C", "M"])
                or any(list(x).count(vld) > 1 for vld in ["V", "L", "D"])
                or (x[i] == "I" and ("V" in list(x[i+2:]))) or (x[i] == "I" and ("X" in list(x[i+2:])))
                or (x[i] == "I" and ("L" in list(x[i+1:]))) or (x[i] == "I" and ("C" in list(x[i+1:])))
                or (x[i] == "I" and ("D" in list(x[i+1:]))) or (x[i] == "I" and ("M" in list(x[i+1:])))
                or (x[i] == "V" and ("X" in list(x[i+1:]))) or (x[i] == "V" and ("L" in list(x[i+1:])))
                or (x[i] == "V" and ("C" in list(x[i+1:]))) or (x[i] == "V" and ("D" in list(x[i+1:])))
                or (x[i] == "V" and ("M" in list(x[i+1:]))) or (x[i] == "X" and ("L" in list(x[i+2:])))
                or (x[i] == "X" and ("C" in list(x[i+2:]))) or (x[i] == "X" and ("D" in list(x[i+1:])))
                or (x[i] == "X" and ("M" in list(x[i+1:]))) or (x[i] == "L" and ("C" in list(x[i+1:])))
                or (x[i] == "L" and ("D" in list(x[i+1:]))) or (x[i] == "L" and ("M" in list(x[i+1:])))
                or (x[i] == "C" and ("D" in list(x[i+2:]))) or (x[i] == "C" and ("M" in list(x[i+2:])))
                or (x[i] == "D" and ("M" in list(x[i+1:]))) or (x[i:i+2] == "IV" and ("I" in list(x[i+2:])))
                or (x[i:i+2] == "IX" and ("I" in list(x[i+2:]))) or (x[i:i+2] == "XL" and ("X" in list(x[i+2:])))
                or (x[i:i+2] == "XC" and ("X" in list(x[i+2:]))) or (x[i:i+2] == "CD" and ("C" in list(x[i+2:])))
                or (x[i:i+2] == "CM" and ("C" in list(x[i+2:])))):
                    print("Not a roman numeral")
                    exit()
                elif i + 1 == len(x):
                    result += roman_numerals_dict[x[i]]
                elif roman_numerals_dict[x[i]] < roman_numerals_dict[x[i+1]]:
                    result -= roman_numerals_dict[x[i]]
                elif roman_numerals_dict[x[i]] >= roman_numerals_dict[x[i+1]]:
                    result += roman_numerals_dict[x[i]]
            print(x, "=", result)
        except KeyError:
            print("Not a roman numeral")
    elif len(x) > 15:
        for j in x:
            if j not in roman_numerals_dict.keys():
                print("Not a roman numeral")
            else:
                print("Too long")
            break
    elif x == "":
        print("No letters inputted")

roman = input("Enter a roman numeral: ").upper()
roman_to_integer(roman)