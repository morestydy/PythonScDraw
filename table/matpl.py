# from matplotlib import pyplot
import matplotlib.pyplot as plt

time = range(0,24,3)
temp = [36.8, 37.2, 38.5, 38.2, 38.0, 37.5, 37.6, 36.8]

# plt.plot(time,temp,color='g',linestyle = '--',marker = '*',linewidth = 2.0)
# plt.plot(time, 
#          temp, 
#          color='r', 
#          linestyle = '--', 
#          marker = '*',
#          )
# plt.xlabel('Time')
# plt.ylabel('Temperture')
# plt.title('Figure 1: Sample_Figure')
# date = ['8‐1', '8‐2', '8‐3', '8‐4',
# '8‐5', '8‐6', '8‐7', '8‐8']
# plt.xticks(time, date, color='b', rotation=60)
# plt.yticks([36, 38, 40, 42])
# date = [11, 13, 15, 17, 19, 21, 23]
# alice_temp = [36.8, 37.2, 38.5, 38.2, 38.0, 37.5, 37.6]
# Bob_temp = [38.1, 38.5, 39, 39.2, 38.5, 38.5, 38.6]
# plt.plot(date, alice_temp, c='r', ls='--', marker='*', label='Alice')
# plt.plot(date, Bob_temp, c='g', ls='-', marker='o', label='Bob')
# plt.legend()

# plt.legend()
x1 = [0.1, 0.3, 0.3, 0.5, 0.9, 0.1, 0.6, 0.7, 0.8, 0.9]
y1 = [0.8, 0.6, 0.7, 0.2, 0.6, 0.1, 0.3, 0.8, 0.5, 0.9]
x2 = [0.7, 0.1, 0.9, 0.8, 0.3, 0.5, 0.4, 0.6, 0.7, 0.4]
y2 = [0.2, 0.3, 0.4, 0.3, 0.9, 0.1, 0.2, 0.8, 0.1, 0.9]
area = [50,300,200,50,900,100,600,700,800,1200]
color = ['r','g','y','r','g','y','r','g','y','r']
# plt.scatter(x, y,s=area,marker='o',c=color,cmap='coolwarm')
plt.scatter(x1,y1,c='r',label='X1‐Y1',marker='+')
plt.scatter(x2,y2,c='b',label='X2‐Y2',marker='^')
plt.xlabel('Variables x')
plt.ylabel('Variables y')
plt.title('Figure3:XXX')
plt.legend()

plt.show()