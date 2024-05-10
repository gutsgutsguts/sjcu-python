import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1, 100, size = 30)
y = np.random.randint(1, 100, size = 30)

plt.scatter(x,y)
plt.show()

data = {'X data' : [1,2,3,4,5], 'Y data' : [2, 4, 8, 10, 3]}

plt.plot('X data', 'Y data', data= data)
plt.show()

plt.plot('X data', 'Y data', data= data)
plt.xlabel('X Lable', labelpad=10)
plt.ylabel('Y Lable', labelpad=10)
plt.show()

plt.plot('X data', 'Y data', data= data, label = 'My Data')
plt.xlabel('X Label', labelpad=10, fontdict={'color' : 'red'}, loc='right')
plt.ylabel('Y Label', labelpad=10, fontdict={'color' : 'blue'}, loc='top')
plt.legend()
plt.show()


plt.plot([1, 2, 3, 4], [2, 3, 7, 9], linestyle='dashed', marker='o', label='Up')
plt.plot([1, 2, 3, 4], [9, 6, 5, 2], linestyle='dotted', label = 'Down')
plt.xlabel('Up Data')
plt.ylabel('Down Data')
plt.grid(True)
plt.title('Up & Down')
plt.legend(loc='best', ncol=2, fontsize=10, frameon=True, shadow=True)

plt.show()

x = np.arange(3)
years = ['2021', '2022', '2023']
values = [100, 200, 500]

plt.bar(x, values)
plt.xticks(x, years)
plt.show()

y = np.arange(3)
plt.barh(y, values)
plt.yticks(y, years)
plt.show()

ratio = [10, 30, 40, 20]
labels = ['chris', 'tommy', 'harry', 'hans']
explode = [0, 0.10, 0 , 0.10]

plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode)
plt.show

#plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode)
#plt.savefig('pie.png')

x = np.arange(1, 5)

fig, ax = plt.subplots(2,2)
ax[0][0].plot(x, np.sqrt(x))
ax[0][1].plot(x, -x)
ax[1][0].plot(x, 2*x)
ax[1][1].plot(x, 3*x)

plt.show()