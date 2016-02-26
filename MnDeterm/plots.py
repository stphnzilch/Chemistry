from numpy import *
from matplotlib.pyplot import *
x = linspace(-2, 2, 100)

figure()

semilogy(x, 2**x, "r-", label=r"$2^x$")

semilogy(x, 3**x, "g-", label=r"$3^x$")

semilogy(x, 4**x, "b-", label=r"$4^x$")

semilogy(x, 5**x, "c-", label=r"$5^x$")

semilogy(x, 6**x, "m-", label=r"$6^x$")

semilogy(x, 7**x, "y-", label=r"$7^x$")

grid(True)

legend(loc="lower right")

savefig("plot_semilogy.png")
