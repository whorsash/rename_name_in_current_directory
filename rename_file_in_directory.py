from tkinter import Tk

import tkinter.filedialog as fd

from io import BytesIO

from barcode.codex import Code128
from barcode.writer import ImageWriter

import pandas as pd

import os
import fnmatch

from file_read_backwards import FileReadBackwards

Tk().withdraw()
print('Выберите файл')
filename = fd.askopenfilename()
if filename == '':
    print('Не выбран файл EXCEL')

print('Выберите путь c фотографиями')
read_directory = fd.askdirectory()


def reverse_string3(s):
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)



excel_data_df = pd.read_excel(filename)
rv = BytesIO()
count = 0
for df in excel_data_df['Наименование'].tolist():
    text = ''
    print(count, df)
    print(type(df))
    sku = ''
    count += 1
    for j in str(df):
        if j == ' ':
            break
        else:
            sku += j
    print('sku:', sku)
    data = reverse_string3(str(df))
    print('data_reverse:', data)
    for k in data:
        if k == ' ':
            break
        text = k + text
    print('text:', text)
    for filename in os.listdir(read_directory):
        print(filename)
        text_file = ''
        reversed_string = reverse_string3(str(filename))
        print('reversed name:', reversed_string)
        for i in reversed_string:
            #print('i:', i)
            if text_file == ' ':
                break
            elif text_file in ['.', 'j', 'p', 'g']:
                text_file = ''
            else:
                text_file = i + text_file
            print('type_text:', type(text), text)
            #print('type_text_file:', type(text_file), text_file)
            if text == text_file:
                os.rename(read_directory + '/' + filename, read_directory + '/' + sku + '.jpg')
                break


##        print(filename, end='\t\n')
##    wget.download(df, directory + '/' + text)
    #urllib.request.urlretrieve(df, directory + '/' + text)
##    print(count, text)


##for filename in os.listdir(read_directory):
##    print(filename, end='\t\n')
##print(os.listdir(directory), end='\t')


##for f in os.listdir(directory):
##    text = ''
##    reversed_string = f[::-1]
##    for k in reversed_string:
##        if k == ' ':
##            break
##        text = k + text
####        print(k, end = '')
##    print(text)
##    os.rename(directory + '/' + f, directory + '/' + text)




##if directory == '':
##    print('Не выбран путь для сохранения штрихкодов')
##
##excel_data_df = pd.read_excel(filename)
##
##rv = BytesIO()
##for df in excel_data_df['шк короба'].tolist() :
##    with open(directory +'/'+ df + ".jpeg", "wb") as f:
##        Code128(df, writer=ImageWriter()).write(f)
##
##print('Готово!')