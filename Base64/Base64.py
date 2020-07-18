import base64

def decode(text):
    try :
        decoded_data = base64.b64decode(text)
    except :
        print("Enter the Proper Hash")
    print("decoded text is " , str(decoded_data))

def encode(text):
    encoded_data = base64.b64encode(text)
    print("Encoded text with base 64 is" , encoded_data)

if __name__ == "__main__":
        option = int(input('''
        1) Encode the text : 
        2) Decode the text : 
'''))

        
        if option == 1:
            text = input("Enter the Encode :\n")
            text  = str.encode(text)
            encode(text ) 
        elif option == 2:
            text = input("Enter the decode :\n")
            decode(text )
