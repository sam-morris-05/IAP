import customtkinter as ctk

from gui import PowerCalculatorGUI


def main():
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()

    PowerCalculatorGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()