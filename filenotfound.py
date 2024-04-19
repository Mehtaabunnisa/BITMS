file_path="example"
try:
    with open(file_path,"r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurd:{e}")#here f is format
finally:
    print("Closing the file.")