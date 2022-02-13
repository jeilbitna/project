string = input()
croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for word in croatia_alphabet:
    if word in string:
        string = string.replace(word,'*') 

print(len(string))