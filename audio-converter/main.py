import pydub

path = input("Wass ist the datei name?")
#format_input = input("wass ist das datei format von der datei?")
format_output = input("In welches format soll es geändert werden?")
def converter(name_plus_format, output_format):
    format_input = name_plus_format[name_plus_format.find(".") + 1:name_plus_format.find(".") + 4]
    audio = pydub.AudioSegment.from_file(str(name_plus_format), str(format_input))
    audio.export(name_plus_format[:name_plus_format.find(".") + 1] + output_format, format=str(output_format))
    
#main
converter(path, format_output)