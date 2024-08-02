file = open('youtube.txt', 'w')

try:
    file.write('Python Code with Muhammad Mubeen')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('Python Code with Muhammad Mubeen')