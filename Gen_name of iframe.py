"""Gen HTML for iframe"""
def html_iframe(num, name):
    for i in range(1, num+1):
        if i < 10:
            keep = "0"+str(i)
        else:
            keep = i
        print('<div align="center">')
        print('<iframe class="centre" src="http://gun.infiteam.in.th/Genesis/New%20Doc/2550/'+name+'/'+str(keep)+'.svg" scrolling="no" frameborder="no" height="600" width="700" align="centre" >')
        print('</iframe></div>')
        print('<p> </p>')
        print('')
html_iframe(int(input()), input())
