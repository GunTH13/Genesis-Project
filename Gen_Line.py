"""BTS line graph."""
import pygal
import csv
from pygal.style import DarkStyle
def bar_graph():
    """Return bar graph as svg file."""
    year = input()
    with open(year+'.txt') as bts:
        for data in csv.reader(bts):
            lst = data[0].split(fill=True, interpolate='cubic', style=DarkStyle)
            chart = pygal.Line()
            chart.title = lst[0] + ' ' + year
            chart.x_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',\
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            chart.add(lst[0], [int(lst[1]), int(lst[2]), int(lst[3]),
            int(lst[4]), int(lst[5]), int(lst[6]), int(lst[7]), int(lst[8]),\
            int(lst[9]), int(lst[10]), int(lst[11]), int(lst[12])])
            chart.render_to_file(lst[0]+year+".svg")
bar_graph()
