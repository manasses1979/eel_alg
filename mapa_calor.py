import matplotlib.pyplot as plt
from numpy import genfromtxt

for i in xrange(91):
	if (i % 9 == 0):	
		m = genfromtxt(('heat_%s.csv' % i), delimiter=',')
	
		fig = plt.figure(figsize=(6, 3.2))
		ax = fig.add_subplot(111)
		ax.set_title(('heat_%s' % i))
		ax.set_aspect('equal')

		plt.imshow(m)
		plt.clim(0,1)
		plt.colorbar(orientation='vertical')
		plt.savefig(('heat_%s.jpg' % i))

#		plt.show()

	
