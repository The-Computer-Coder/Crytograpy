from string import punctuation as punct 

def decrypt(text,s):
   result = ""
   for i in range(len(text)):
      char = text[i]
     
      if char in punct or ord(char) == 32 :
         result += char 
      
      elif (char.isupper()):
         result += chr((ord(char) - s-65) % 26 + 65)

      else:
         result += chr((ord(char) - s - 97) % 26 + 97)
      
      
   return result
def encrypt(text,s):
   result = ""
   for i in range(len(text)):
      char = text[i]
      
      if char in punct or ord(char) == 32 :
         result += char 
      
      elif (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)

      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      
      
   return result


if __name__ == "__main__":
   option = int(input('''
      1) Encrypt the message : 
      2) Decrypt the message :
      
'''))
   text = input("Enter the message :\n")
   key =  int(input("Enter the Key :\n"))
   if option == 1:
      print( "Encrypted Message is " ,  encrypt(text , key) )
   elif option == 2:
      print( "Decryted message is", decrypt(text , key) )
