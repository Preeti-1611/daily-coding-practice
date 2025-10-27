#vowels in the given string
name = "preetiNagarale"
vowels ="aeiou"
count =0
vowels_in_name =""
for i in name:
    if i  in vowels:
        count = count+1
        vowels_in_name+=i

print(f"the given string has {count} vowels and that are '{vowels_in_name}' vowels")