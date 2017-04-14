from functools import partial

import io
import matplotlib.cm
import matplotlib.colors
import numpy
import phaseplot
import scipy.misc
import stream


PI = numpy.pi
E = numpy.e

# DELTA=0.005
DELTA=0.01
PLOT_MODULUS = True

T_START = 0
T_END = 2*PI+DELTA+DELTA/2
T_STEP = 0.01
BOX = (-2, 2, -2, 2)

def polyfun(z, t=0.0):
  i = complex(0, 1)
  return numpy.piecewise(z, [abs(z) < 2, abs(z) >= 2], [(lambda z: 
    # Function goes here
    z
    # Function end
  ), 0])

def main():
  bw_values = (
  [(1, 1, 1)] * 8 +
  [(0, 0, 0)] * 8)
  bw_values = bw_values * 16
  cmap = matplotlib.colors.ListedColormap(bw_values)
  # cmap = matplotlib.cm.hsv
  # cmap = matplotlib.cm.rainbow

  pipe = stream.start_stream(filename='output.avi')

  t = T_START
  while t < T_END:
    print (str.format('t = {:.3f}', t))
    plot = phaseplot.phase_portrait(partial(polyfun, t=t),
      box=BOX, delta=DELTA, cmap=cmap, plot_modulus=PLOT_MODULUS)

    bio = io.BytesIO()
    scipy.misc.imsave(bio, plot, format='png')
    bio.seek(0)
    pipe.stdin.write(bio.read())

    t += T_STEP

  stream.end_stream(pipe)


if __name__ == '__main__':
    main()
