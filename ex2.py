import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmd = 'ffmpeg -i BBB_CUT.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" BBB_CUT_HIST.mp4'
    os.system(cmd)
