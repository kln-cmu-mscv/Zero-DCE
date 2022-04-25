import argparse
from FFMPEGFrames import FFMPEGFrames

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True)
ap.add_argument("-f", "--fps", required=True)
args = vars(ap.parse_args())

inp = args["input"]
fps = args["fps"]

f = FFMPEGFrames("data/enhanced_videos/")
f.extract_video(inp, fps)