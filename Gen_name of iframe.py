"""Gen HTML for iframe"""
def html_iframe(year, name, num):
    print("---------------------------------")
    for i in range(1, num+1):
        keep = "%02i"%i
        print('<div align="center">')
        print('<iframe class="centre" src="http://gun.infiteam.in.th/Genesis/New%20Doc/'+year+'\/'+name+'/'+str(keep)+'.svg" scrolling="no" frameborder="no" height="600" width="700" align="centre" >')
        print('</iframe></div>')
        print('<p> </p>')
html_iframe(input(), input(), int(input()))
