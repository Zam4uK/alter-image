# -*- coding: utf-8 -*-

from PIL import Image as Imager


import os
from os.path import join,splitext
path = u''
i = 1

for f in os.listdir(path) :
	print join(path, f)
	

	try :
		image = Imager.open(join(path, f))
		file1, ext = splitext(f)
		#size = 618, 452
		#image.thumbnail(size, Imager.ANTIALIAS)
		#image.save(file1+'_re' + ext, "JPEG")
	
		



		#max_width = 635
		max_width = 618
		max_height = 452
		
		src_width, src_height = image.size
		src_ratio = float(src_width) / float(src_height)
		dst_width, dst_height = max_width, max_height
		dst_ratio = float(dst_width) / float(dst_height)
		
		if dst_ratio < src_ratio:
			crop_height = src_height
			crop_width = crop_height * dst_ratio
			x_offset = float(src_width - crop_width) / 2
			y_offset = 0

		else:
			crop_width = src_width
			crop_height = crop_width / dst_ratio
			x_offset = 0
			y_offset = float(src_height - crop_height) / 3
		image = image.crop((int(x_offset), int(y_offset), int(x_offset+crop_width), int(y_offset+crop_height)))
		image = image.resize((max_width, max_height), Imager.ANTIALIAS)
		image.save( 'djstation_'+ str(i) + ext, "JPEG")
		i = i + 1
	except :
		print u'Problem with '+ f
