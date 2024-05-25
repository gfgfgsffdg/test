import pydub
import customtkinter
import time
# customtkinter CTKhead
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x500")
root.title("Wetter app")


# def converter(name_plus_format, output_format):
#     format_input = name_plus_format[name_plus_format.find(
#         ".") + 1:name_plus_format.find(".") + 4]
#     audio = pydub.AudioSegment.from_file(
#         str(name_plus_format), str(format_input))
#     audio.export(name_plus_format[:name_plus_format.find(
#         ".") + 1] + output_format, format=str(output_format))


# main
textbox = customtkinter.CTkEntry(root, placeholder_text="test")
textbox.pack()
root.mainloop()
time.sleep(999999999)
# converter(path, format_output)
