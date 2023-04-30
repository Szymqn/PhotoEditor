import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def brighten_image(image, brightness_factor):
    brightened_image = Image.new("RGB", image.size)

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))

            r = int(r * brightness_factor)
            g = int(g * brightness_factor)
            b = int(b * brightness_factor)

            brightened_image.putpixel((x, y), (r, g, b))

    return brightened_image


def save_image(image):
    filepath = asksaveasfilename(defaultextension=".jpg")

    if filepath:
        image.save(filepath)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.brighten_button = None
        self.dark_button = None
        self.save_button = None
        self.input = None
        self.title("Image Viewer")

        self.image_label = tk.Label(self)
        self.image_label.pack()

        self.load_button = tk.Button(self, text="Load Image", command=self.load_image)
        self.load_button.pack()

    def load_image(self):
        filepath = askopenfilename(filetypes=[("Image Files", "*.jpg")])

        image = Image.open(filepath)

        photo = ImageTk.PhotoImage(image)

        self.image_label.configure(image=photo)
        self.image_label.image = photo

        bright_factor = 10  # default
        tk.Label(self, text="Enter bright factor").pack()
        bright_factor = tk.Entry(self, width=35)
        bright_factor.pack()

        self.brighten_button = tk.Button(self, text="Brighten", command=lambda: self.brighten_image(image, float(bright_factor.get())))
        self.brighten_button.pack()

        dark_factor = .5  # default
        tk.Label(self, text="Enter dark factor").pack()
        dark_factor = tk.Entry(self, width=35)
        dark_factor.pack()

        self.dark_button = tk.Button(self, text="Dark",
                                     command=lambda: self.brighten_image(image, float(dark_factor.get())) if 0 < float(dark_factor.get()) <= 1 else .5)

        self.dark_button.pack()

    def brighten_image(self, image, bright_factor):
        brightened_image = brighten_image(image, bright_factor)

        photo = ImageTk.PhotoImage(brightened_image)

        self.image_label.configure(image=photo)
        self.image_label.image = photo

        self.save_button = tk.Button(self, text="Save Image", command=lambda: save_image(brightened_image))
        self.save_button.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
