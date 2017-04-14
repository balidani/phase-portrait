from functools import partial

import io
import numpy
import matplotlib.cm
import matplotlib.colors
import phaseplot
import scipy.misc
import stream

E = numpy.e
PI = numpy.pi
BOX = (-2, 2, -2, 2)
PLOT_MODULUS = False

def polyfun(z, t=0.0):
  i = complex(0, 1)
  '''
  return numpy.piecewise(z, [abs(z) < 2, abs(z) >= 2], [(lambda z: 
    
    ), 0])
  '''
  return (
    z * (z - 1)
  )

def main():
  t = 0.0

  bw_values = (
    [(1, 1, 1)] * 16 +
    [(0, 0, 0)] * 16)
  bw_values = bw_values * 8
  cmap = matplotlib.colors.ListedColormap(bw_values)
  # cmap = matplotlib.cm.hsv

  plot = phaseplot.phase_portrait(partial(polyfun, t=t),
    box=BOX, delta=0.005, cmap=cmap, plot_modulus=PLOT_MODULUS)
  scipy.misc.imsave('output.png', plot, format='png')


if __name__ == '__main__':
    main()
