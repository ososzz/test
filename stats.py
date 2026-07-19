# write a python script to calculate the stats of a file. Use python language.

import os

def stats(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
            print(f"Lines: {num_lines}")
            print(f"Words: {num_words}")
            print(f"Characters: {num_chars}")
    else:
        print("File not found.")

if __name__ == "__main__":
    file_path = input("Enter file path: ")
    stats(file_path)    
