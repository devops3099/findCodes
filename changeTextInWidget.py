from tkinter import *
 
root = Tk()
 
e = Entry(width=20)
b = Button(text="Преобразовать")
l = Label(bg='black', fg='white', width=20)
global textForListForDeleteFromTuple_1
textForListForDeleteFromTuple_1 = '234' 
def strToSortlist(event):
	textForListForDeleteFromTuple_1 = '123'
	# s = e.get()
	# s = s.split()
	# s.sort()
	l['text'] = textForListForDeleteFromTuple_1# + ' ' +' '.join(s)
	print('l [] = ', l)
	#print('s = ', s)

 
b.bind('<Button-1>', strToSortlist)
 
e.pack()
b.pack()
l.pack()
root.mainloop()