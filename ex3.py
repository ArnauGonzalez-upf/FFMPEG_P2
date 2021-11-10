import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmd = 'ffmpeg -i BBB_CUT.mp4 -vf scale=1280:720 BBB_CUT_720p.mp4'
    os.system(cmd)
    cmd = 'ffmpeg -i BBB_CUT.mp4 -vf scale=640:480 BBB_CUT_480p.mp4'
    os.system(cmd)
    cmd = 'ffmpeg -i BBB_CUT.mp4 -vf scale=320:240 BBB_CUT_320x240.mp4'
    os.system(cmd)
    cmd = 'ffmpeg -i BBB_CUT.mp4 -vf scale=160:120 BBB_CUT_160x120.mp4'
    os.system(cmd)