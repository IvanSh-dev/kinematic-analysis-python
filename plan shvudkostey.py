import tkinter as tk
import math

root = tk.Tk()
root.title("План швидкостей кривошипно-шатунного механізму")
root.geometry("1920x1080")

canvas = tk.Canvas(root, width=1900, height=800, bg="white")
canvas.place(x=10, y=10, width=1900, height=800)

crank_label = tk.Label(root, text="Довжина кривошипа (мм):")
crank_label.place(x=700, y=830)
crank_entry = tk.Entry(root, width=10)
crank_entry.place(x=860, y=830)

rod_label = tk.Label(root, text="Довжина шатуна (мм):")
rod_label.place(x=950, y=830)
rod_entry = tk.Entry(root, width=10)
rod_entry.place(x=1100, y=830)

angle_label = tk.Label(root, text="Кут кривошипа (градуси):")
angle_label.place(x=700, y=870)
angle_entry = tk.Entry(root, width=10)
angle_entry.place(x=860, y=870)

angular_velocity_label = tk.Label(root, text="Кутова швидкість (рад/с):")
angular_velocity_label.place(x=950, y=870)
angular_velocity_entry = tk.Entry(root, width=10)
angular_velocity_entry.place(x=1100, y=870)

def calculate_velocity_plan():
    try:
        
        crank_length = float(crank_entry.get())
        rod_length = float(rod_entry.get())
        crank_angle_deg = float(angle_entry.get())
        angular_velocity = float(angular_velocity_entry.get())

        crank_angle_rad = math.radians(crank_angle_deg)
        gamma = math.radians(90-crank_angle_deg)

        v_ax = angular_velocity * crank_length * math.cos(gamma)
        v_ay = angular_velocity * crank_length * math.sin(gamma)

        o1b = crank_length * math.cos(crank_angle_rad) + (((rod_length**2)-((crank_length * math.sin(crank_angle_rad))**2))**0.5)
        o2b = o1b * (math.sin(crank_angle_rad) / math.cos(crank_angle_rad))
        o1o2 = ((o1b**2) + (o2b**2))**0.5
        angular_velocity_AB = (angular_velocity * crank_length) / (o1o2 - crank_length)
        v_bx = angular_velocity_AB * o2b


        origin_x, origin_y = 950, 400
        scale = 5

        a_x = origin_x + v_ax * scale
        a_y = origin_y - v_ay * scale

        b_x = origin_x + v_bx * scale
        b_y = origin_y

        canvas.delete("all")

        canvas.create_line(0, origin_y, 1900, origin_y, fill="black", arrow=tk.LAST)
        canvas.create_line(origin_x, 800, origin_x, 0, fill="black", arrow=tk.LAST)

        canvas.create_line(origin_x, origin_y, a_x, a_y, fill="red", arrow=tk.LAST, width=2)
        canvas.create_line(origin_x, origin_y, b_x, b_y, fill="blue", arrow=tk.LAST, width=2)
        canvas.create_line(a_x, a_y, b_x, b_y, fill="green", arrow=tk.LAST, width=2)
        
        canvas.create_rectangle(10, 10, 180, 90, outline="black", fill="white")
        canvas.create_line(20, 20, 40, 20, fill="red", arrow=tk.LAST, width=2)
        canvas.create_text(50, 20, text="- Швидкість точки A", anchor="w", fill="black")
        canvas.create_line(20, 50, 40, 50, fill="blue", arrow=tk.LAST, width=2)
        canvas.create_text(50, 50, text="- Швидкість точки B", anchor="w", fill="black")
        canvas.create_line(20, 80, 40, 80, fill="green", arrow=tk.LAST, width=2)
        canvas.create_text(50, 80, text="- Швидкість ланки AB", anchor="w", fill="black")

    except ValueError:
        show_error("Будь ласка, введіть коректні числові значення.")

def clear_canvas():
    canvas.delete("all")

def show_error(message):
    error_window = tk.Toplevel(root)
    error_window.title("Помилка")
    tk.Label(error_window, text=message).pack(padx=10, pady=10)
    tk.Button(error_window, text="Закрити", command=error_window.destroy).pack(pady=5)

calculate_button = tk.Button(root, text="Побудувати план швидкостей", command=calculate_velocity_plan)
calculate_button.place(x=960, y=910, width=200, height=30)

clear_button = tk.Button(root, text="Очистити", command=clear_canvas)
clear_button.place(x=700, y=910, width=200, height=30)

root.mainloop()
