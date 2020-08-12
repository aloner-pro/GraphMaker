# author = @gunjitsinha


import matplotlib.pyplot as plt
import numpy as np
import time as t


class Plot():
	def plot(self, func):
		func()
		plt.xlabel('x axis')
		plt.ylabel('y axis')
		plt.axhline(y=0, color='orange')
		plt.axvline(x=0, color='orange')
		plt.show()


class Trigo(Plot):
	def sine(self):
		x = np.arange(-4 * np.pi, 4 * np.pi, 0.1)
		return plt.plot(x, np.sin(x))

	def cosine(self):
		x = np.arange(-4 * np.pi, 4 * np.pi, 0.1)
		return plt.plot(x, np.cos(x))

	def tangent(self):
		x = np.arange(0, 4 * np.pi, 0.1)
		return plt.plot(x, np.tan(x))

	def cosec(self):
		x = np.arange(-4 * np.pi, 4 * np.pi, 0.1)
		return plt.plot(x, 1/(np.sin(x)))

	def sec(self):
		x = np.arange(-4 * np.pi, 4 * np.pi, 0.1)
		return plt.plot(x, 1/(np.cos(x)))

	def cot(self):
		x = np.arange(-4 * np.pi, 4 * np.pi, 0.1)
		return plt.plot(x, 1/(np.tan(x)))


class Maths(Plot):
	def expo(self):
		x = np.arange(0, 100)
		return plt.plot(x, np.exp(x))

	def log(self):
		x = np.arange(1, 100)
		return plt.plot(x, np.log(x))

	def line(self):
		x = np.arange(0, 100)
		return plt.plot(x, (x*3+5))


graphy1 = Trigo()
graphy1.plot(graphy1.tangent)
t.sleep(2)
graphy2 = Maths()
graphy2.plot(graphy2.log)
