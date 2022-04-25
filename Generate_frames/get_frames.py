import argparse
from FFMPEGFrames import FFMPEGFrames

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True)
ap.add_argument("-f", "--fps", required=True)
args = vars(ap.parse_args())

input = args["input"]
fps = args["fps"]

f = FFMPEGFrames("data/images_frames/")
f.extract_frames(input, fps)