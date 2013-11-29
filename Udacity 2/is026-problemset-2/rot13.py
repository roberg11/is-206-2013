def rot_text(s):
    result = ''
    for character in s:
        o = ord(character)
        if o >= 65 and o <= 90:
            result += chr((((o - 65) + 13) % 26) + 65)
        elif o >= 97 and o <= 122:
            result += chr((((o - 97) + 13) % 26) + 97)
        else:
            result += character
    return result

s1 = "something"
print rot_text('Hello!\nHello"> %f') % str(s1)
