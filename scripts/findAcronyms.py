#!python3

# XXX: This script is very lousy and should be used with caution!

import subprocess
import re

acronyms = set()

utf8_result = subprocess.run(["detex", "matrixRTC.tex"], stdout=subprocess.PIPE).stdout.decode('utf-8')

result_without_newlines = utf8_result.replace("\n", " ").replace("\t", " ")
clean_result = re.sub(r'[\[\]\"\(\)\\/,?|$|.|!]',r'', result_without_newlines)
word_list = clean_result.split(" ")

for word in word_list:
  for character in word:
    if word.isnumeric():
      continue
    if len(word) < 2:
      continue
    if word[0].islower():
        continue
    if word[1].islower():
        continue

    acronyms.add(word)

print(acronyms)
