import matplotlib.pyplot as plt

ind_var = range(1, 6)
dep_var = [x * x for x in ind_var]

fig, ax = plt.subplots()
ax.plot(ind_var, dep_var, linewidth=3, color='red')
ax.set_title("Squared Numbers", fontsize=14)

plt.show()