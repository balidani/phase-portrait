from subprocess import Popen
from subprocess import PIPE


def start_stream(filename='output.avi'):
  p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'png', '-r',
    '60', '-i', '-', '-vcodec', 'mpeg4', '-q:v', '0', '-r', '60',
    filename], stdin=PIPE)

  return p

def end_stream(p):
  p.stdin.close()
  p.wait()