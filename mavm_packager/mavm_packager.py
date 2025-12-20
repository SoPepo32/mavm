import argparse
import os

class create_mavm:
    def __init__(self, files="", file_out="video.mavm", r=None):
        self.file_out = file_out
        if r:
            files_names_txt = open(files, 'r')
            files_names     = files_names_txt.read().split('\n')
            files_names_txt.close()
            self.create_r(files=files_names) #aca se crea el archivo mavm en base a los otros archivos
        else:
            self.create_r(files=files)
    
    def create_r(self, files):
        files_d = []
        for file in files[0:]:
            try:
                file_f = open(file, 'rb')
                files_d.append([os.path.basename(file).encode("utf-8"),file_f.read()])
                file_f.close()
            except Exception as e:
                print(e)
        
        file_bits_list = []
        for file_d in files_d:
            try:
                file_name, file_data = file_d
                print(file_name)
                file = b"".join([b"-++", file_name, b"+--", file_data])
                file_bits_list.append(file)
            except Exception as e:
                print(e)
        
        file_bits = b"".join(file_bits_list)
        file_out = open(self.file_out, 'bw')
        file_out.write(file_bits)
        file_out.close()

def main():
    parser = argparse.ArgumentParser(description="mavm packager")
    parser.add_argument("--files_r", help="txt document with the files to import\n") #archivos a guardado
    parser.add_argument("--file", help="file to import (JSON/MKV/OPUS)\n") #archivos a importas
    parser.add_argument("--file_out", help="output file in .mavm format\n", default="video.mavm") #archivo de salida

    args = parser.parse_args()
    
    if not('.mavm' in args.file_out.lower()):
        print("The output file must be in .mavm format")
        exit()
    elif args.files_r == None and args.file == None:
        print("You need to set the input file(s).")
        exit()
    if args.files_r == None:
        create_mavm(files=args.file,file_out=args.file_out)
    elif args.file == None:
        create_mavm(files=args.files_r,file_out=args.file_out,r=True)

main()
