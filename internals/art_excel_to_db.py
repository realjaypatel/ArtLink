# LEONARDO da Vinci
# (b. 1452, Vinci, d. 1519, Cloux, near Amboise)
# Mona Lisa (detail)
# 1503-5	
# Oil on panel	
# Musée du Louvre, Paris	
# https://www.wga.hu/html/l/leonardo/04/1monali2.html	
# art link: https://www.wga.hu/detail/l/leonardo/04/1monali2.jpg
# author link: https://www.wga.hu/frames-e.html?/bio/l/leonardo/biograph.html
# author img: https://www.wga.hu/biojpg/l/leonardo/biograph.jpg
# painting	
# portrait	
# Italian	
# 1451-1500


d = 'https://www.wga.hu/html/z/zwirner/moyland3.html'.split('/')[5]

# print(d)

d = 'https://www.wga.hu/html/a/aachen/allegorz.html'
e = 'https://www.wga.hu/detail/a/aachen/allegorz.jpg'
f = 'https://www.wga.hu/art/a/aachen/allegorz.jpg'
d=d.split('html')
d = d[0]+'detail'+d[1]+'jpg'
# print(d)


import random, datetime

x = datetime.datetime.today().strftime("%Y:%m:%d")
random.seed(x)

r_int = random.randint(1, 52000)
print(r_int)