name = input("Write your name: ")
date = input("Write date (dd/mm/yy): ")
letter = f'''Dear {name} 
You are Selected.
Date : {date}'''
print(letter)
print()
letter = f'''Dear <|Name|> 
You are Selected.
Date : <|Date|>'''
print(letter.replace("<|Name|>",name).replace("<|Date|>",date))