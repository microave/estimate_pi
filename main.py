import numpy as np

class Point():
    """
    A point in a 2D (xy) space
    properties:
        x: float, x-coordinate
        y: float, y-coordinate
    """

    def __init__(self, xy=None):
        """
        Constructor
        If xy is not provided, randomly generate xy coordiantes.
        Otherwise, xy can be assigned by a tuple (e.g., (2, 3))
        """

        # assign values to x and y
        if xy is None:
            self.x = np.random.uniform(0, 2)
            self.y = np.random.uniform(0, 2)
        else:
            self.x, self.y = xy

    def __repr__(self):
        """
        Allow the xy-coordinates to be printed when the point is called
        """
        return "Point: %.2f, %.2f" % (self.x, self.y)

    def distance(self, point):
        """
        input: a Point() object
        output: Euclidean distance between self point and the input point
        """
        return np.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

def estimate_pi(n_points):
    """
    input: number of points to be generated
    output: estimated pi through the simulation
    """
    center = Point((1, 1))
    count_inside = 0

    for _ in range(n_points):
        point = Point()
        if point.distance(center) <= 1:
            count_inside += 1

    return 4 * count_inside / n_points

# estimate pi for 100 iterations
n_iter = 100
n_points = 1000
pi_estimates = np.zeros(n_iter)
for i in range(n_iter):
    pi_estimates[i] = estimate_pi(n_points)

#calculate 95% confidence interval
mean_pi = np.mean(pi_estimates)
std_pi = np.std(pi_estimates)
conf_interval = (mean_pi - 1.96 * std_pi / np.sqrt(n_iter), mean_pi + 1.96 * std_pi / np.sqrt(n_iter))

print("Estimated Pi:", mean_pi)
print("95% Confidence Interval:", conf_interval)

