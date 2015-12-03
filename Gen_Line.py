import pygal
def bar_graph():
    """Return bar graph as svg file."""
    lst = ['mor chit', 11, 12, 13, 14, 20, 10, 5, 6, 11, 15, 19, 14]
    chart = pygal.Line()
    chart.title = (lst[0])
    chart.add('Jan', lst[1])
    chart.add('Feb', lst[2])
    chart.add('Mar', lst[3])
    chart.add('Apr', lst[4])
    chart.add('May', lst[5])
    chart.add('Jun', lst[6])
    chart.add('Jul', lst[7])
    chart.add('Aug', lst[8])
    chart.add('Sep', lst[9])
    chart.add('Oct', lst[10])
    chart.add('Nov', lst[11])
    chart.add('Dec', lst[12])
    chart.render_to_file("BarBTS.svg")
bar_graph()
