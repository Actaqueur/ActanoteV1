import os 
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Actanote - Actadite")
        self.root.geometry("644x788")
        self.root.wm_iconbitmap("1.ico")

        self.filename = None

        self.title = tkinter.StringVar()
        self.title.set("Untitled")

        self.statusbar = tkinter.Label(self.root, text="Actanote > Bloc-Note", anchor="w", font="lucida 10 italic")
        self.statusbar.pack(side="bottom", fill="x")

        self.menubar = tkinter.Menu(self.root)

        self.filemenu = tkinter.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.newfile)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_command(label="Save", command=self.savefile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quitapp)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = tkinter.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut", command=self.cut)
        self.editmenu.add_command(label="Copy", command=self.copy)
        self.editmenu.add_command(label="Paste", command=self.paste)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Find", command=self.find)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = tkinter.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About Actanote", command=self.showabout)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.root
        self.root.config(menu=self.menubar)

        self.scrollbar = tkinter.Scrollbar(self.root)
        self.scrollbar.pack(side="right", fill="y")

        self.textarea = tkinter.Text(self.root, font="lucida 13")
        self.textarea.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=self.scrollbar.set)

    def newfile(self, *args):
        self.root.title("Actanote - Actadite")
        self.filename = None
        self.textarea.delete(1.0, tkinter.END)

    def openfile(self, *args):
        self.filename = tkinter.filedialog.askopenfilename(title="Select File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if self.filename:
            self.root.title(os.path.basename(self.filename) + " - Actanote")
            self.textarea.delete(1.0, tkinter.END)
            file = open(self.filename, "r")
            self.textarea.insert(1.0, file.read())
            file.close()

    def savefile(self, *args):
        if self.filename:
            try:
                content = self.textarea.get(1.0, tkinter.END)
                file = open(self.filename, "w")
                file.write(content)
                file.close()
            except Exception as e:
                tkinter.messagebox.showerror("Error", e)
        else:
            self.saveasfile()

    def saveasfile(self, *args):
        try:
            newfile = tkinter.filedialog.asksaveasfilename(initialfile="Untitled.txt", title="Save File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
            content2 = self.textarea.get(1.0, tkinter.END)
            file = open(newfile, "w")
            file.write(content2)
            file.close()
            self.root.title(os.path.basename(newfile) + " - Actanote")
        except Exception as e:
            tkinter.messagebox.showerror("Error", e)

    def quitapp(self, *args):
        self.root.destroy()

    def cut(self, *args):
        self.textarea.event_generate("<<Cut>>")

    def copy(self, *args):
        self.textarea.event_generate("<<Copy>>")

    def paste(self, *args):
        self.textarea.event_generate("<<Paste>>")

    def find(self, *args):
        findstring = tkinter.simpledialog.askstring("Find...", "Enter Text")
        self.textarea.tag_remove("match", "1.0", tkinter.END)
        matches = 0
        if findstring:
            start_pos = "1.0"
            while True:
                start_pos = self.textarea.search(findstring, start_pos, stopindex=tkinter.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(findstring)}c"
                self.textarea.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                self.textarea.tag_config("match", foreground="red", background="yellow")

    def showabout(self, *args):
        tkinter.messagebox.showinfo("Actanote", "Created By: Actaruss")

if __name__ == "__main__":
    root = tkinter.Tk()
    notepad = TextEditor(root)
    root.mainloop()