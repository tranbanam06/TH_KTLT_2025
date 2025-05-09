print ("Sinh Viên: Trần Bá Nam")
print ("MSV: 235752020710046")

import tkinter as tk#nhập thư viện Tkinter để tạo giao diện đồ họa (GUI)

"""Hàm xử lý sự kiện khi phím được bấm"""
def on_key_press(event):#Định nghĩa một hàm tên on_key_pressHàm nhận đối số event, là đối tượng chứa thông tin về sự kiện phím được nhấn (như phím nào, vị trí chuột, thời gian...).
    print(f"Bạn đã bấm phím: {event.char}")#event.char là ký tự tương ứng với phím được nhấn (ví dụ: a, b, 1,...).

"""Hàm thay đổi màu button khi nhấn"""
def change_button_color():#Định nghĩa một hàm không có tham số.Hàm này được gán cho thuộc tính command của Button, nên sẽ được gọi khi nút được nhấn.
    button.config(bg="yellow",fg="black")#Sử dụng phương thức .config() để thay đổi thuộc tính của button:bg="yellow": đặt màu nền của nút thành vàng.fg="black": đặt màu chữ của nút thành đen
"""Tạo một cửa sổ chính"""
window = tk.Tk()#tk.Tk() tạo ra một đối tượng cửa sổ chính (root window) trong ứng dụng Tkinter.
window.title("Ứng dụng Tkinter")#Đặt tiêu đề của cửa sổ thành "Ứng dụng Tkinter".
"""Thêm một button vào cửa sổ"""
button = tk.Button(window, text="Nhấn vào đây", command=change_button_color)#tk.Button(window, ...): Tạo một nút (button) trong cửa sổ window.
#text="Nhấn vào đây": Nội dung hiển thị trên nút
#command=change_button_color: Khi nút được nhấn, hàm change_button_color() sẽ được gọi (hàm này đã được định nghĩa ở đâu đó trong mã của bạn để thay đổi màu sắc của nút).
button.pack(pady=20) #.pack(): Phương thức này được sử dụng để thêm nút vào cửa sổ và hiển thị nó.
#pady=20: Tạo khoảng cách (padding) 20 pixel ở trên và dưới nút, giúp nút không bị dính vào các phần tử khác trong cửa sổ.

"""Đăng ký sự kiện bàn phím"""
window.bind("<KeyPress>", on_key_press)#window: là cửa sổ chính của ứng dụng Tkinter, được tạo bằng window = tk.Tk().
#Đăng ký trình xử lý sự kiện cho sự kiện nhấn phím (KeyPress).Khi người dùng nhấn một phím bất kỳ trong cửa sổ, Tkinter sẽ gọi hàm on_key_press(event).
"""thiết lập màu nền cho cửa sổ"""
window.config(bg="lightblue")
#.config(): là phương thức cho phép bạn cấu hình lại các thuộc tính của widget (ở đây là cửa sổ window).
#bg là viết tắt của background (nền)."lightblue" là tên một màu hợp lệ trong Tkinter
"""chạy vòng lặp chính""" 
window.mainloop()#.mainloop():Bắt đầu vòng lặp sự kiện: lắng nghe và xử lý các hành động của người dùng như:Nhấn nút....Giữ cho cửa sổ luôn hiển thị cho đến khi người dùng chủ động đóng nó.
