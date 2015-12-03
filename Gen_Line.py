"""BTS line graph."""
import pygal
def bar_graph():
    """Return bar graph as svg file."""
    with open('BTS.txt') as bts:
        for data in csv.reader(bts):
            lst = data[0].split()
            chart = pygal.Line()
            chart.title = lst[0]
            chart.add('Jan', int(lst[1]))
            chart.add('Feb', int(lst[2]))
            chart.add('Mar', int(lst[3]))
            chart.add('Apr', int(lst[4]))
            chart.add('May', int(lst[5]))
            chart.add('Jun', int(lst[6]))
            chart.add('Jul', int(lst[7]))
            chart.add('Aug', int(lst[8]))
            chart.add('Sep', int(lst[9]))
            chart.add('Oct', int(lst[10]))
            chart.add('Nov', int(lst[11]))
            chart.add('Dec', int(lst[12]))
            chart.render_to_file("BarBTS.svg")
bar_graph()
