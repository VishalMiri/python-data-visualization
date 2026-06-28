import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'sv', 'gt', 'hn', 'ni', 'pa', 'py'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'fk', 'gy', 'pe', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')