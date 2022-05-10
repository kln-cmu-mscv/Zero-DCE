import os
import glob
import subprocess

class FFMPEGFrames:
    def __init__(self, output):
        self.output = output

    def extract_frames(self, input, fps):
        for dir in os.listdir(input):
            files = glob.glob(os.path.join(input,dir, '*.mp4'))

            for file in files:
                output = file.split('/')[-1].split('.')[0]
                if not os.path.exists(self.output + dir+'/' + output):
                    os.makedirs(self.output + dir+'/' + output)
                # query = "ffmpeg -i " + file + " -vf fps=" + str(fps) + " " + self.output + dir + '/' + output + "/%06d.png"
                query = "ffmpeg -i " + file +  " " + self.output + dir + '/' + output + "/%06d.png"
                response = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
                s = str(response).encode('utf-8')
                
            
    def extract_video(self, inp, fps):
        for dir in os.listdir(inp):
            
            vids = glob.glob(os.path.join(inp,dir,"*"))
            
            # for vid in vids:
            #     files = glob.glob(os.path.join(vid, '*.png'))
                
            for file in vids:
                
                output = file.split('/')[-1]
                
                if not os.path.exists(self.output + dir):
                    os.makedirs(self.output + dir)
                
                query = "ffmpeg -i " + inp + dir + '/' + output + "/%06d.png " +  self.output + dir + '/' + output + ".mp4"
                response = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
                s = str(response).encode('utf-8')
                    
                  