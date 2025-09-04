try:
    while(1):
        orgtext = input()
        newtext = ""

        for i in orgtext:
            if(i=='e'):
                newtext += 'i'
            elif(i=='i'):
                newtext += 'e'
            elif(i=='E'):
                newtext += 'I'
            elif(i=='I'):
                newtext += 'E'
            else:
                newtext += i

        print(newtext)
except EOFError:
    pass