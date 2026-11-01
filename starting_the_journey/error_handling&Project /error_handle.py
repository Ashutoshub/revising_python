file = open('youtube.txt', 'w')
try:
    file.write('This is a test.')
finally:
    file.close()
with open('youtube.txt', 'w') as file:
    file.write('This is a test.')