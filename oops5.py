try:
    file=open('data.txt','r')
    info=file.read()
    print(info)
    line_count = len(info.split('\n'))
    print(f"Total number of lines: {line_count}")

except FileNotFoundError:
    print("File Not Found")