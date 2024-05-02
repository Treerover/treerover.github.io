def decode(message_file):
  with open(message_file, 'r') as file:
    lines = file.readlines()

  decoded_message = []
  for i, line in enumerate(lines):
    num, word = line.split()
    num = int(num)
    if num== (i+1):
      decoded_message.append(word)
  return ' '.join(decoded_message)

print(decode('message.txt'))