"""BTS line graph."""
import pygal
import csv

def bar_graph():
    """Return bar graph as svg file."""
    with open('BTS20xx.txt') as bts:
        for data in csv.reader(bts):
            lst = data[0].split()
            chart = pygal.Line()
            chart.title = lst[0]
            chart.x_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',\
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            chart.add(lst[0], [int(lst[1]), int(lst[2]), int(lst[3]),
            int(lst[4]), int(lst[5]), int(lst[6]), int(lst[7]), int(lst[8]),\
            int(lst[9]), int(lst[10]), int(lst[11]), int(lst[12])])
            chart.render_to_file(lst[0]+"BarBTS.svg")
bar_graph()
