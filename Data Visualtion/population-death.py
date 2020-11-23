import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1970, 1975, 1980,
         1985, 1990, 1995, 2000, 2005, 2010, 2015]

pops = [2.525, 2.758, 3.018, 3.322, 3.682, 4.061, 4.440,
        4.853, 5.310, 5.735, 6.157, 6.520, 6.930, 7.349]

deaths = [1.525, 1.758, 2.018, 2.322, 2.682, 3.061, 3.440,
          4.853, 6.310, 4.735, 7.157, 7.520, 6.930, 6.349]

line = plt.plot(years, pops, years, deaths)
plt.grid(True)
plt.setp(line, marker="o")
plt.show()

# plt.plot(years, pops, "--", color=(255/255, 100/255, 100/255))
# plt.plot(years, deaths, color=(0.6, 0.6, 1))

# plt.title("Population Growth")
# plt.xlabel("Population growth by years")
# plt.ylabel("Population in billions")
