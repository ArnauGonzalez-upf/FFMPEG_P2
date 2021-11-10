import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    select = 100
    while select != "0":
        print("Select:")
        print("0) Exit")
        print("1) Cut BBB video")
        print("2) Video Histogram:")
        print("3) Resize Video:")
        print("4) Audio Mono and Audio Codec Change:")
        select = input()

        if (select == "0"):
            cmd = ''
        elif (select == "1"):
            cmd = 'python3 ex1.py'
        elif (select == "2"):
            cmd = 'python3 ex2.py'
        elif (select == "3"):
            cmd = 'python3 ex3.py'
        elif (select == "4"):
            cmd = 'python3 ex4.py'
        else:
            print("Not an option!")

        os.system(cmd)
    exit()
