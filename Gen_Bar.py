"""BTS bar graph."""
import pygal
import csv

def bar_graph():
    """Return bar graph as svg file."""
    year = int(input())
    with open(str(year)+'.txt') as bts:
        for data in csv.reader(bts):
            lst = data[0].split()
            bar_chart = pygal.Bar()
            bar_chart.title = lst[0]
            bar_chart.x_labels =([str(year)])
            bar_chart.add('Jan', [int(lst[1])])
            bar_chart.add('Feb', [int(lst[2])])
            bar_chart.add('Mar', [int(lst[3])])
            bar_chart.add('Apr', [int(lst[4])])
            bar_chart.add('May', [int(lst[5])])
            bar_chart.add('Jun', [int(lst[6])])
            bar_chart.add('Jul', [int(lst[7])])
            bar_chart.add('Aug', [int(lst[8])])
            bar_chart.add('Sep', [int(lst[9])])
            bar_chart.add('Oct', [int(lst[10])])
            bar_chart.add('Nov', [int(lst[11])])
            bar_chart.add('Dec', [int(lst[12])])
            bar_chart.render_to_file(lst[0]+str(year)+".svg")
bar_graph()
