"""BTS bar graph <sum>"""
import pygal
import csv
from pygal.style import DarkStyle
def bar_graph_sum():
    """Return bar graph as svg file."""
    with open('summary.txt') as bts:
        chart = pygal.Bar(fill=True, interpolate='cubic', style=DarkStyle)
        chart.title = "Summary between 2550-2558"
        chart.x_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',\
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for data in csv.reader(bts):
            lst = data[0].split()
            chart.add(str(lst[0]), [int(lst[1]), int(lst[2]), int(lst[3]),
            int(lst[4]), int(lst[5]), int(lst[6]), int(lst[7]), int(lst[8]),\
            int(lst[9]), int(lst[10]), int(lst[11]), int(lst[12])])
    chart.render_to_file("sum_bar.svg")
bar_graph_sum()
