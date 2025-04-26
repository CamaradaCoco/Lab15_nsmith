from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_values) < self.num_points:
            x_dir = choice([-1, 1])
            x_dis = 1
            x_step = x_dir * x_dis

            y_dir = choice([-1, 1])
            y_dis = 1
            y_step = y_dir * y_dis

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)


rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
    