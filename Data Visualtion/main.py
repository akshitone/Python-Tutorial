import matplotlib.pyplot as plt
import numpy as np

korea = (554, 536, 538)
canada = (518, 523, 525)
china = (613, 570, 580)
france = (495, 505, 499)

count = len(korea)
index = np.arange(count)
bar_width = 0.2

korea_bar = plt.bar(index, korea,
                    bar_width, alpha=0.4, label="Korea")
canada_bar = plt.bar(index + bar_width, canada,
                     bar_width, alpha=0.4, label="Canada")
china_bar = plt.bar(index + (bar_width*2), china,
                    bar_width, alpha=0.4, label="China")
france_bar = plt.bar(index + (bar_width*3), france,
                     bar_width, alpha=0.4, label="France")


def create_labels(data):
    for item in data:
        height = item.get_height()
        width = item.get_width()
        x_axis = item.get_x()
        plt.text(x_axis + width / 2., height + 1.05,
                 '%d' % int(height), ha="center", va="bottom")


create_labels(korea_bar)
create_labels(canada_bar)
create_labels(china_bar)
create_labels(france_bar)


plt.title("TEst Scores by Countries")
plt.xticks(index + (bar_width*3) / 2, ("Mathematics", "Reading", "Science"))
plt.xlabel("Subjects")
plt.ylabel("Mean score in PISA 2012")
plt.legend(loc=2, bbox_to_anchor=(1, 1), frameon=False)
plt.grid(True)
plt.show()
