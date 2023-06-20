import difflib
  
with open('lab2_laksa/39_gen/test.out') as file_1:
    file_1_text = file_1.readlines()
  
with open('testniFile.txt') as file_2:
    file_2_text = file_2.readlines()
  
# Find and print the diff:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='test.out', 
        tofile='testniFile.txt', lineterm=''):
    print(line)