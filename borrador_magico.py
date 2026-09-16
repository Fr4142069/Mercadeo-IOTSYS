import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import sys
import os

class ImageEditor:
    def __init__(self, root, image_paths):
        self.root = root
        self.image_paths = image_paths
        self.current_idx = 0
        self.ratio = 1.0
        
        # Botones arriba
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(side="top", fill="x")
        
        self.undo_btn = tk.Button(self.btn_frame, text="Deshacer", command=self.undo_all, font=("Arial", 12))
        self.undo_btn.pack(side="left", padx=10, pady=10)
        
        self.zoom_in_btn = tk.Button(self.btn_frame, text="Acercar (+)", command=self.zoom_in, font=("Arial", 12, "bold"))
        self.zoom_in_btn.pack(side="left", padx=10, pady=10)
        
        self.zoom_out_btn = tk.Button(self.btn_frame, text="Alejar (-)", command=self.zoom_out, font=("Arial", 12, "bold"))
        self.zoom_out_btn.pack(side="left", padx=10, pady=10)
        
        self.next_btn = tk.Button(self.btn_frame, text="Guardar y Siguiente", command=self.save_and_next, font=("Arial", 12, "bold"), bg="green", fg="white")
        self.next_btn.pack(side="right", padx=10, pady=10)
        
        # Contenedor del canvas con scroll
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(fill="both", expand=True)
        
        self.vbar = tk.Scrollbar(self.canvas_frame, orient="vertical")
        self.hbar = tk.Scrollbar(self.canvas_frame, orient="horizontal")
        
        self.canvas = tk.Canvas(self.canvas_frame, cursor="cross", bg="gray", xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        
        self.vbar.pack(side="right", fill="y")
        self.hbar.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.vbar.config(command=self.canvas.yview)
        self.hbar.config(command=self.canvas.xview)
        
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        
        self.load_current_image()

    def load_current_image(self):
        if self.current_idx >= len(self.image_paths):
            messagebox.showinfo("Listo", "Ambas imágenes han sido procesadas. Ya puedes cerrar esta ventana.")
            self.root.destroy()
            return
            
        self.image_path = self.image_paths[self.current_idx]
        self.original_image = Image.open(self.image_path).convert("RGB")
        self.edited_image = self.original_image.copy()
        
        # Calcular zoom inicial
        screen_width = self.root.winfo_screenwidth() - 100
        screen_height = self.root.winfo_screenheight() - 150
        img_width, img_height = self.original_image.size
        
        ratio = min(screen_width/img_width, screen_height/img_height)
        if ratio > 1:
            ratio = 1
        self.ratio = ratio
        
        self.root.title(f"Borrador Mágico ({self.current_idx+1}/{len(self.image_paths)}): {os.path.basename(self.image_path)}")
        self.update_canvas()

        self.start_x = None
        self.start_y = None
        self.rect = None

    def zoom_in(self):
        self.ratio *= 1.3
        self.update_canvas()

    def zoom_out(self):
        self.ratio /= 1.3
        self.update_canvas()

    def update_canvas(self):
        img_width, img_height = self.edited_image.size
        display_width = int(img_width * self.ratio)
        display_height = int(img_height * self.ratio)
        
        self.display_image = self.edited_image.resize((display_width, display_height), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.display_image)
        
        self.canvas.delete("all")
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)
        self.canvas.config(scrollregion=(0, 0, display_width, display_height))

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red', width=2)

    def on_move_press(self, event):
        if self.rect:
            cur_x = self.canvas.canvasx(event.x)
            cur_y = self.canvas.canvasy(event.y)
            self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x = self.canvas.canvasx(event.x)
        end_y = self.canvas.canvasy(event.y)
        
        if self.rect:
            self.canvas.delete(self.rect)
        
        if abs(end_x - self.start_x) < 5 or abs(end_y - self.start_y) < 5:
            return # Área muy pequeña
            
        x1 = int(min(self.start_x, end_x) / self.ratio)
        y1 = int(min(self.start_y, end_y) / self.ratio)
        x2 = int(max(self.start_x, end_x) / self.ratio)
        y2 = int(max(self.start_y, end_y) / self.ratio)
        
        # Limites seguros
        img_width, img_height = self.edited_image.size
        x1 = max(0, min(x1, img_width-1))
        y1 = max(0, min(y1, img_height-1))
        x2 = max(0, min(x2, img_width-1))
        y2 = max(0, min(y2, img_height-1))
        
        # Tomar color del fondo (un poco afuera y arriba a la izquierda de la caja)
        sample_x = max(0, x1 - 5)
        sample_y = max(0, y1 - 5)
        bg_color = self.edited_image.getpixel((sample_x, sample_y))
        
        draw = ImageDraw.Draw(self.edited_image)
        draw.rectangle([x1, y1, x2, y2], fill=bg_color)
        
        self.update_canvas()

    def save_and_next(self):
        save_path = self.image_path # Sobreescribir
        self.edited_image.save(save_path)
        print(f"Guardado: {save_path}")
        self.current_idx += 1
        self.load_current_image()
        
    def undo_all(self):
        self.edited_image = self.original_image.copy()
        self.update_canvas()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Faltan imagenes")
        sys.exit(1)
        
    root = tk.Tk()
    app = ImageEditor(root, sys.argv[1:])
    root.mainloop()
