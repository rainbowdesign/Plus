import timefrom threading import Timerfrom random import randomfrom functools import partialimport os, globimport kivyfrom kivy.app import Appfrom kivy.uix.button import Buttonfrom kivy.uix.floatlayout import FloatLayoutfrom kivy.uix.gridlayout import GridLayoutfrom kivy.lang import Builderfrom kivy.uix.image import AsyncImagefrom kivy.uix.boxlayout import BoxLayoutfrom kivy.uix.label import Labelfrom kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SwapTransition,WipeTransitionfrom kivy.uix.widget import Widgetkvs='''BoxLayout:		orientation: 'vertical'	BoxLayout:		canvas.before:			BorderImage:				# BorderImage behaves like the CSS BorderImage				border: 10, 10, 10, 10				source: 'numbers/menu.png'				pos: self.pos				size: self.size				id: 'border'			Color:				rgba: 0.5, 0, 1,0				id: 'color'			Rectangle:				# self here refers to the widget i.e BoxLayout				pos: self.pos				size: self.size		id:content	BoxLayout:		id: menu		size_hint_y: 0.1		Button:			text:'New'			id:bbt		BoxLayout:			size_hint_x: 0.8			id:next'''root = Builder.load_string(kvs)	gener = 0drop = 1class sButton(Button):	def __init__(self, **kwargs):		super(MPopup, self).__init__(**kwargs)		bname=0		bg=''		background=bg		self.background_normal = self.background		self.background_down = self.backgroundstack=[]def next():	while len(stack) <4:		stack.append(picnum())	a = stack.pop(0)	print 'nextret', a	return adef setnext(x,y,*a):	numarray[(x,y)]=next()	valnum(x,y,1)	addi()numbers= [1,2,3,4,5,6,7,8,9]def combnum():	for x in range(6): #friendstarget		for y in range(6):			valnum(x,y)def valnum(x,y,z=0):	z=2	print 'valnumz',z	if numarray[(x,y)] in numbers:		check = numarray[(x,y)] 		if z==2:						check2= (x,y)	else: return	global data	global data1	global check2	data = 0	data1 = 0	try: 		if 	numarray[(x-1,y)] == check:			datai (x-1,y,z)	except: pass	try:		if 	numarray[(x,y-1)] == check:			datai (x,y-1,z)	except: pass	try:		if 	numarray[(x+1,y)] == check:			datai (x+1,y,z)	except: pass		try:		if 	numarray[(x,y+1)] == check:			datai (x,y+1,z)	except: pass		if (data!=0)+(data1!=0)==2:		try:			numarray[check2] = (numarray[(x,y)] +1)		except:			numarray[(x,y)] = (numarray[(x,y)] +1)		numarray[data] ='empty'		numarray[data1] ='empty'def datai(payl,payl1,z):	global data	global data1	if data ==0:		data = (payl,payl1)	elif (data1 ==0) +(z==0)==2:		data1 = (payl,payl1)	elif z==2: data1 = (payl,payl1)	#else: valnum(payl,payl,z=2)def picnum():	for num, pic in enumerate(numbers):		ran = random()*(len(numbers))		if num+1 >= ran: return picl = 'numbers\\'def choosepic(picn):	pic = l+str(picn)+'.png'		print 'chret', pic	return pic	numarray = dict([((x, y),'empty') for x in range(6) for y in range(6)])def tsel(pnum,*a):	print pnumdef setfr2():	lay = GridLayout(cols= 6)	for x in range(6): #friendstarget		for y in range(6):			if gener==1:				pnum = picnum()				mre2 = Button(bname = pnum, background_normal=choosepic(pnum), background_down=choosepic(pnum),border= (0,0,0,0) )			elif drop == 1:				if numarray[(x,y)]=='empty':					nextn = partial(setnext,*(x,y))					mre2 = Button(on_press= nextn,bname = 'empty', background_normal=choosepic('empty'), background_down=choosepic('empty'),border= (0,0,0,0) )				else:						mre2 = Button(bname = numarray[(x,y)], background_normal=choosepic(numarray[(x,y)]), background_down=choosepic(numarray[(x,y)]),border= (0,0,0,0) )			lay.add_widget(mre2)			return laydef addnextn():	lay = BoxLayout()	for num, pnum in enumerate(stack):		mre2 = Button(bname = pnum, background_normal=choosepic(pnum), background_down=choosepic(pnum),border= (0,0,0,0) )		lay.add_widget(mre2)	return laydef addi(*a):	combnum()	root.ids.content.clear_widgets()	root.ids.content.add_widget(setfr2())	root.ids.next.clear_widgets()	root.ids.next.add_widget(addnextn())root.ids.bbt.bind(on_press=addi)class MainApp(App): #Main function#	def build(self):				return rootif __name__ == '__main__':    MainApp().run()