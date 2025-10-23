#o=input();s=int(input());s=-s if o=='d'else s;m=input();r=[chr((ord(c)-97+s)%26+97)if 'a'<=c<='z'else chr((ord(c)-65+s)%26+65)if 'A'<=c<='Z'else c for c in m];print(''.join(r)) 176 characters

#s=int(input());s=-s if input()=="d"else s;r=[chr((ord(c)-97+s)%26+97)if 'a'<=c<='z'else chr((ord(c)-65+s)%26+65)if 'A'<=c<='Z'else c for c in input()];print(''.join(r)) 168 characters