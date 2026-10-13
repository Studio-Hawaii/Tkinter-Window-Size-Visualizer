import tkinter as tk

DEFAULT_WIDTH = 400
DEFAULT_HEIGHT = 400
SIZE_FONT_SIZE = 20

def on_configure(event):
     print(f"Size String: {event.width}x{event.height}")
     print(f"Size String (Position Included): {event.width}x{event.height}+{event.x}+{event.y}")
     size_label.config(text=f"{event.width}x{event.height}\nX: {event.x}, Y: {event.y}")

root = tk.Tk()
root.geometry(f"{DEFAULT_WIDTH}x{DEFAULT_HEIGHT}")
root.title("Size Visualizer")

size_label = tk.Label(root, font=("Arial Bold", SIZE_FONT_SIZE))
size_label.place(relx=0.5, rely=0.5, anchor="center")

root.bind_class("Tk","<Configure>", on_configure)

if __name__ == "__main__":
    root.update_idletasks()
    root.mainloop()