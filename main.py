from tkinter import *
from time import time
from tkinter import messagebox as mb
from typing import List


def clicker():
    counter = 0
    start = time()
    def check_recods (nickname:str, score:int) -> None:
        with open('ClickerRecord.txt', 'r+', encoding='utf-8') as f:
            record_list = f.readlines()
            new_record_list = [line.strip('\n').split(" ") for line in record_list]

            for index, line_num in enumerate(new_record_list):
                if score > int(line_num[2]):
                    new_record_list.insert(index, [str(index + 1), nickname, str(score)])
                    break
            for line_num in range(index + 1, len(new_record_list)):
                new_record_list[line_num][0] = str(line_num + 1)
            record_list = [' '.join(i) + '\n' for i in new_record_list]
            f.seek(0)

            f.writelines(record_list)

    def on_click():
        nonlocal counter,start
        if time()-start<3:
            counter += 1
            lbl2.config(text=f'За Путина\n{counter} млн.чел')
        else:
            confirm = mb.showinfo(message=f"Опа,\nПутин набрал {counter} млн.голосов")

            if confirm=='ok':
                start = time()
                counter = 0
                confirm

    root = Tk()
    root.resizable(False, False)
    root.geometry('400x300+460+200')
    icon_img = PhotoImage(file="pngegg.png")
    root.iconphoto(False, icon_img)

    btn = Button(text = "Голосуй!",
                 font=("Italicka",15,'bold'),
                 width=40,
                 height = 5,
                 bg='red',
                 fg='white',
                 relief=GROOVE,
                 command=on_click
                 )
    lbl2 = Label(text="За Путина\n0",
                font=("Comic Sans", 15, 'bold'),
                width=40,
                height=4,
                bg='white',
                fg='black')
    lbl = Label(text = "Эй,ты",
                 font=("Comic Sans",15,'bold'),
                 width=40,
                 height = 3,
                 bg='blue',
                 fg='white')
    lbl2.pack()
    lbl.pack()
    btn.pack()




    root.mainloop()


























if __name__=="__main__":
    clicker()
   #  nickname = input('Введите имя ')
   #  score = int(input('Введите очки '))
   #
   #
   #
   #      print(new_record_list)











