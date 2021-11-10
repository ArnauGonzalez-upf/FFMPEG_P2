import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("How many seconds do you want to cut?")
    seconds = input()
    cmd = 'ffmpeg -ss 00:00:00 -i BBB.mp4 -t ' + seconds + ' -c copy BBB_CUT.mp4'
    os.system(cmd)
