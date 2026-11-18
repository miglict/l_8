import tkinter as tk
import math

# 1. Считаем ряд y(x) с точностью 0.001
def calc_y(x, eps=0.001):
    s, n, term = 0, 0, x
    while abs(term) > eps:
        s += term
        n += 1
        term = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    return s

# 2. Рисуем графики
def draw():
    canvas.delete("all")
    w, h = canvas.winfo_width(), canvas.winfo_height()
    b, dx = 0.5, 0.05  # параметр b и шаг

    # Собираем точки для обоих графиков в списки
    pts_y, pts_z = [], []
    x = -1.0
    while x <= 1.0:
        # переводим координаты в пиксели (ось Y посередине, масштаб по Y = h/6)
        px = (x + 1) * (w / 2)
        pts_y += [px, h / 2 - calc_y(x) * (h / 6)]
        pts_z += [px, h / 2 - (math.atan(x) + b) * (h / 6)]
        x += dx

    # Рисуем оси
    canvas.create_line(0, h / 2, w, h / 2, width=2)  # X
    canvas.create_line(w / 2, 0, w / 2, h, width=2)  # Y

    # Рисуем графики (create_line принимает список координат: x1,y1, x2,y2...)
    canvas.create_line(pts_y, fill="blue", width=2)  # y(x) через ряд
    canvas.create_line(pts_z, fill="red", width=2)  # z(x) = arctg(x) + b

# 3. Окно
root = tk.Tk()
root.geometry("800x600")
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
root.after(100, draw)  # ждем 100мс, чтобы холст понял размеры, и рисуем
root.mainloop()