import tkinter as tk
from tkinter.simpledialog import askstring
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from io import BytesIO

import os

class TextController:
    def render_latex_to_image(self, formula, fontsize=12, dpi=200, padding=0.1):
        """
        Render LaTeX formula into an image with dynamic sizing and white background.
        
        Parameters:
        - formula: str, the LaTeX formula to render
        - fontsize: int, the font size for the formula
        - dpi: int, the dots per inch resolution of the figure
        - padding: float, the padding used in the figure
        
        Returns: 
        - Image object containing the rendered LaTeX formula with dynamic sizing.
        """
        # Initialize a matplotlib figure
        fig = plt.figure()
        # fig.patch.set_facecolor('white')
        
        # Add text to the figure to estimate the size needed
        text = fig.text(0, 0, f'${formula}$', fontsize=fontsize, ha='left', va='bottom')
        
        # Use the bounding box of the text to set the figure size
        fig_width, fig_height = text.get_window_extent(renderer=fig.canvas.get_renderer()).size / dpi
        fig_width /= fig.dpi
        fig_height /= fig.dpi
        fig.set_size_inches(fig_width + 2 * padding, fig_height + 2 * padding)

        # Remove all axes and whitespace to fit the formula
        plt.axis('off')
        plt.tight_layout(pad=0)

        # Save the figure to a buffer
        buf = BytesIO()
        plt.savefig(buf, format='png', transparent=True, bbox_inches='tight', pad_inches=0.0)
        buf.seek(0)
        plt.close(fig)
        
        # Load the image from the buffer
        image = Image.open(buf)
        return image
    def update_button_image(self, button):
        """Update the image on the button."""
        print('try to update the button')
        formula = askstring("Input LaTeX Formula", "Enter your LaTeX formula:")
        if not formula:
            print("No formula entered.")
            return

        image = self.render_latex_to_image(formula)
        if image:
            photo = ImageTk.PhotoImage(image)
            button.config(image=photo,bg='white')
            button.image = photo  # Keep a reference!
        else:
            print("Failed to render formula.")

# #Create the main window
# root = tk.Tk()
# root.title("LaTeX in Tkinter")
# canvas = tk.Canvas(root,width=800,height=800,background='white')
# canvas.grid(column=1,row=1)


# print("Current Working Directory:", os.getcwd())

# # Create a default image for the button
# default_image_path = './feynman_diagram/resources/default_tex.png'
# default_image = Image.open(default_image_path)
# # default_image = Image.new('RGB', (100, 30), color = (255, 255, 255))  # White image
# default_photo = ImageTk.PhotoImage(default_image)

# # Button to update the image
# tex_controller = TextController()
# button = tk.Button(canvas, image=default_photo, command=lambda: tex_controller.update_button_image(button))
# button.grid(column=0, row=0)

# # Start the GUI event loop
# root.mainloop()