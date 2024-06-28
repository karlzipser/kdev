## 79 ########################################################################
#,a
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
# Heron's method

def h(S,xn):
	return (xn+S/xn)/2


S=25823
xn=[1]
n=10
for i in range(n):
	xn.append(h(S,xn[-1]))
figure(1);clf()
plot(xn,'b.-')
plot([0,n],[np.sqrt(S),np.sqrt(S)],'r')
plt.title(d2n('sqrt(',S,')=',np.sqrt(S),', xn=',xn[-1]))
plt.xlabel(n)
plt.ylabel(xn)
#,b