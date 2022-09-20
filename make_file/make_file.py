import sys
import os

number_of_files = int(sys.argv[1])

path = os.getcwd()
path2 = fr'{path}'

for file_num in range(number_of_files):
    file_name = (f'file{file_num}.txt')
    file_path = (f'{path2}\{file_name}')

    f = open(path2, 'w')
    f.write(f'File number is {file_num}')
    f.close()
