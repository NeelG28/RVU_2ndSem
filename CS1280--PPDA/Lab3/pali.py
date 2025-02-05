sent=input("Enter a sentence : ")
sent.lower()
a=list(sent)

a.reverse()
testst=''.join(a)
if testst==sent:
     print("it is a palindrome")
else: 
     print("it is not a palindrome")
