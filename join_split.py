#split
text = "pythonisfun"
text1 ="python is fun"
word = text.split('y')
word1= text1.split()
print(word)
print(word1)

info = "2025-10-30"
parts = info.split("-")
print(parts)



#join
words = ['Python', 'is', 'fun']
sentence = " ".join(words)
print(sentence)

#" ".join(["Hello", "Preeti"])
# Output: Hello Preeti
print(" ".join(["Hello", "Preeti"]))


date_parts = ['2025', '10', '30']
date = "-".join(date_parts)
print(date)