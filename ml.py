'''import numpy
a=[12,23,34,45,56,57]
av=numpy.mean(a)
print(av)'''


from scipy import stats
a=[12,23,34,45,56]
m=stats.mode(a)
print(a)