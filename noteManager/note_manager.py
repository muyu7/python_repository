from tkinter import *
note_file = open('bb.md','r',encoding='utf-8')
notes=note_file.readline()
print('first line:',notes)
note_file.close()

window = Tk()
text=Text(window)
text.insert(INSERT,notes)
text.pack()
window.mainloop()