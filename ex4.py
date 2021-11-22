import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmd = 'ffmpeg -i BBB_CUT.mp4 -ac 1 -acodec mp3 -vcodec copy BBB_CUT_MONO.mp4'
    os.system(cmd)
