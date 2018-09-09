import tkinter as tk
import tkinter.messagebox

def close_window():
    tkinter.messagebox.showwarning('WARNING', 'NO CLOSE')
def hit_me():

    root1 = tk.Tk()
    root1.title('不同意不行！')
    root1.geometry('250x150')
    root1.attributes("-topmost", True)
    for i in range(2):
        tk.Label(root1, text='          ').grid(row=i, column=0)
        tk.Label(root1, text='          ').grid(row=i, column=1)
    tk.Button(root1, text='后悔了!', fg='black', command = root1.destroy, width = 10, height = 2).grid(row = 2, column = 2)

root = tk.Tk()
# top = tk.Toplevel(root)
# w = root.winfo_screenwidth()
# h = root.winfo_screenheight()
# root.geometry('%dx%d' %(800,800))
root.attributes("-topmost",True)
root.attributes("-fullscreen", True)
# top.overrideredirect(boolean=True)
for i in range(50):
    tk.Label(root, text = '                   ').grid(row = i, column = 0)
    tk.Label(root, text = '                   ').grid(row = i, column = 1)
photo = tk.PhotoImage(file="1.png")
imgLabel = tk.Label(root,image=photo)
imgLabel.grid(row = 1, column = 3)
tk.Label(root, text = ( '请....请做我女朋友吧！！'), width = 30, height = 10, fg = 'red', font =('宋体', 20, 'normal')).grid(row = 2, column = 4)
tk.Button(root, text = '不同意', fg = 'black', command = hit_me, width = 15, height = 2).grid(row = 3, column = 5)
tk.Button(root, text = '同意', fg = 'black', command = root.destroy, width = 15, height = 2).grid(row = 3, column = 4)
root.protocol('WM_DELETE_WINDOW', close_window)
# root.protocol('WM_SIZE_WINDOW', size_window)

root.mainloop()
