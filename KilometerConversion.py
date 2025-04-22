import tkinter

class KiloConverterGUI:
    def __init__(self):
        # Set up the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("KM to Miles Converter")

        # Frames help organize the layout (top: input, mid: result, bottom: buttons)
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # --- Top Frame: Input ---
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter distance (km):')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # --- Middle Frame: Output ---
        self.descr_label = tkinter.Label(self.mid_frame, text='Converted to miles:')

        self.result_var = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.result_var)

        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        # --- Bottom Frame: Buttons ---
        self.convert_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.convert_button.pack(side='left', padx=5)
        self.quit_button.pack(side='left', padx=5)

        # Pack everything together
        self.top_frame.pack(pady=5)
        self.mid_frame.pack(pady=5)
        self.bottom_frame.pack(pady=10)

        # Keep the app running
        tkinter.mainloop()

    def convert(self):
        try:
            # Grab user input
            km = float(self.kilo_entry.get())

            # Do the conversion (1 km ≈ 0.6214 miles)
            miles = km * 0.6214

            # Display result (rounded to 2 decimals)
            self.result_var.set(f"{miles:.2f} miles")
        except ValueError:
            self.result_var.set("Invalid input!")

# Launch the app
if __name__ == '__main__':
    KiloConverterGUI()
