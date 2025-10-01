import taichi as ti
import tifonts

ti.init(arch=ti.gpu)

# Canvas dimensions
WIDTH, HEIGHT = 800, 600
canvas = ti.Vector.field(3, dtype=ti.f32, shape=(WIDTH, HEIGHT))

@ti.kernel
def clear_canvas():
    for i, j in canvas:
        canvas[i, j] = ti.math.vec3(0.0, 0.0, 0.0) # Black background

def main():
    clear_canvas()

    # --- Example 1: Using the default font ---
    print("Rendering with default font...")
    try:
        # No font_path argument, uses the default font (pixels5x7)
        tifonts.text(canvas, "Default Font!", 50, 50, 5, (1.0, 1.0, 1.0)) # White color
        print("Default font example rendered.")
    except FileNotFoundError as e:
        print(f"Error loading default font: {e}")
        print("Please ensure the default font directory and its JSON files exist.")
        return
    except ValueError as e:
        print(f"Error in default font data: {e}")
        return

    # --- Example 2: Loading a specific font ---
    print("Rendering with explicitly loaded font...")
    explicit_font_path = 'tifonts/fonts/pixels5x7' # Path relative to project root
    try:
        my_font = tifonts.load(explicit_font_path)
        tifonts.text(canvas, "Explicit Font!", 50, 150, 3, (0.0, 1.0, 0.0), my_font) # Green color
        print(f"Explicit font '{explicit_font_path}' example rendered.")
    except FileNotFoundError as e:
        print(f"Error loading explicit font '{explicit_font_path}': {e}")
        print("Please ensure the font directory and its JSON files exist.")
        return
    except ValueError as e:
        print(f"Error in explicit font data: {e}")
        return

    # Display with GUI
    gui = ti.GUI("Taichi Text Renderer", res=(WIDTH, HEIGHT))
    while gui.running:
        gui.set_image(canvas)
        gui.show()

if __name__ == '__main__':
    main()
