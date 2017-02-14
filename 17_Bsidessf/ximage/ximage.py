import Image #Need PIL

r_list = []
g_list = []
b_list = []

img = Image.open("neoncow_change.bmp")
w, h = img.size

for z in range(8):
	str_r = ''
	str_g = ''
	str_b = ''
	for x in range(w):
		for y in range(h):
		color = img.getpixel((x, y))
		r, g, b = color
		if r==0 and g==0 and b==0: #dark
			continue
		else:
			r = r >> z
			g = g >> z
			b = b >> z
			str_r += str(r%2)
			str_g += str(g%2)
			str_b += str(b%2)
	r_list.append(str_r)
	g_list.append(str_g)
	b_list.append(str_b)

print r_list
print g_list
print b_list
