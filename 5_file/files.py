reding = open('text.txt')
amountChars = 100
text = reding.read(amountChars)
print(text)

for line in reding:
    print(line)

reding.close()

writing = open('text.txt', 'w')
writing.write('writing in file')

writing.close()