#Шифратор Цезаря
#Роль 2 — Шифратор Цезаря. Выполняет шифрование/дешифрование текста сдвигом по алфавиту (с сохранением регистра и знаков препинания)

def cipher(text:str,shift:int, decrypt: bool = False)->str:
    stroke=""
    if(decrypt):
        shift=-shift
    for char in text:
        if 'A' <= char <= 'Z':
            stroke += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            stroke += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'А' <= char <= 'Я':
            stroke += chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
        elif 'а' <= char <= 'я':
            stroke += chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
        else:
            stroke+=char
        
    return stroke

def test():
    result = cipher("Hello, world!",3,False)
    print(result)
    result2 = cipher(result,3,True)
    print(result2)
    
    result = cipher("Привет, мир!",3,False)
    print(result)
    result2 = cipher(result,3,True)
    print(result2)

test()