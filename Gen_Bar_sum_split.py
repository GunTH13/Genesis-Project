"""BTS bar graph <sum_split>"""
import pygal
import csv
from pygal.style import Style
custom_style = Style(
background='#1C1C1C',
plot_background='#1C1C1C',
foreground='#53E89B',
foreground_strong='#53A0E8',
foreground_subtle='#630C0D',
colors=('#40FF00', '#088A08'))
def bar_graph_sum_split():
    """Return bar graph as svg file."""
    year = input()
    with open(year+'.txt') as bts:
        chart = pygal.Bar(fill=True, interpolate='cubic', style=custom_style)
        chart.title = 'Each line ' + year
        chart.x_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',\
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for data in csv.reader(bts):
            lst = data[0].split()
            chart.add(str(lst[0]), [int(lst[1]), int(lst[2]), int(lst[3]),
            int(lst[4]), int(lst[5]), int(lst[6]), int(lst[7]), int(lst[8]),\
            int(lst[9]), int(lst[10]), int(lst[11]), int(lst[12])])
    chart.render_to_file("sum_bar_split"+year+".svg")
bar_graph_sum_split()
