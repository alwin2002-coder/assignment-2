a=input("enter the word:")
def has_duplicate(a):
    for i in a:
        if a.count(i) > 1:
            return True
    

if has_duplicate(a):
  print("the word has duplicate characters")
else:
     print("the word has unique characters")


