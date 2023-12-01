import tkinter as ttk

def code(a, b):
    a = a.get().replace(" ", "")
    b = int(b.get()) + 1
    result_list = [[] for i in range(b)]
    c = 1
    c_step = 1
    for letter in combined_text:
        if letter.isalpha():
            result_list[c - 1].append(letter)
            if c == 1:
                c_step = 1
            elif c == b:
                c_step = -1
            c += c_step

    result = "".join(["".join(row) for row in reversed(result_list)])
    g.config(text=result)

root = ttk.Tk()
root.title("Чистокол")

d = ttk.Label(root, text="Text:")
d.grid(row=0, column=0, sticky="w")

a = ttk.Entry(root)
a.grid(row=0, column=1)

e = ttk.Label(root, text="Key:")
e.grid(row=1, column=0, sticky="w")

b = ttk.Entry(root)
b.grid(row=1, column=1)

f = ttk.Button(root, text="Результат:", command=lambda: code(a, b))
f.grid(row=2, column=0, columnspan=2, pady=10)

g = ttk.Label(root, text="")
g.grid(row=3, column=0, columnspan=2)

root.mainloop()
