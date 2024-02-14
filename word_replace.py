sent=input("Enter a sentence\n")

rep1=input("Enter a word to replace in the string\n")

rep2=input("Enter the word to be replaced with\n")

news=""

array=sent.split(" ")

for i in array:

if i==rep1:

news+=rep2+""

else:

news+=i+" "

print(f"New sentence: {news}")

print("Number of words in ",news,"is",len(array))
