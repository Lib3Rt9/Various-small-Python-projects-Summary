import os

# place the all willing-to-rename files and this z1.py file into the same folder
os.chdir('D:\RenameMultiFile')                # change this path to where this file is located
print(os.getcwd())
COUNT = 0

#function to increment count to make the files sorted0
def increment():
  global COUNT
  COUNT = COUNT + 1

for f in os.listdir():
  f_name, f_ext = os.path.splitext(f)
  f_name = "000" + str(COUNT)                 # "000" is the prefix, change to whatever is ok, then the suffix is the number incresing from the COUNT in line 6
  increment()
  new_name = '{} {}'.format(f_name, f_ext)
  os.rename(f, new_name)