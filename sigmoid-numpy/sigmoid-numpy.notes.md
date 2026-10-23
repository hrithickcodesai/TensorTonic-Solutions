As we go further on the X-axis's direction on graph y = e ^ (-x) the values grow very very fast and the result goes past the largest value float64 can hold. So large value for x makes e ^ (-x)  ~ inf so the value of sigmoid becomes 0



But this is numerically unstable so we can multiply both the denominator and numerator by e ^ (-x) and convert it into a numerically stable format.