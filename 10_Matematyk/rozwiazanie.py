def onp(text):
    OPERATORS = ("+", "-", "*", "//")

    split_text = text.split()
    stos = []

    for i in split_text:
        if i not in OPERATORS:          # dodawanie na stos
            stos.append( int(i) )
        else:
            a = stos.pop()              # wykonywanie działań
            b = stos.pop()
            
            if i == "+":
                stos.append(b+a)
            elif i == "-":
                stos.append(b-a)
            elif i == "*":
                stos.append(b*a)
            elif i == "//":
                stos.append(b//a)

    return stos[0]

