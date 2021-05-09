
#function number 1
def main_fun():
	
	def uni_fun():
		print ()
		print ()
		print ("qq) Quit")
		print ("00) Back")
		uni_input=input ("Please Select any option: ")
		uni_str=str(uni_input)
		uni_array=["qq","00"]
		uni_data=uni_str in uni_array
		qq="qq"
		bck="00"
		if uni_data == True:
			uni_in_str=str(uni_input)
			if uni_in_str == qq:
							
				print ("You are exit from Cli-Calculator")
				
			elif uni_in_str == bck:
							
				main_fun()
		else:
			print (">>Please select right option")
			uni_fun()
			
	def help_fun():
					
		print (">>You select Help & Feedback")
		print ()
		print ()
		print ()
		print ("              H E L P ")
		print ("             ---------")
		print ()
		print ("a) To make a command shortcut and use cli-calculator from any session. Follow these steps ↓↓")
		print ()
		print (" 1. First exit this tool by typing: qq")
		print (" 2. Then type this command: sh install.sh ")
		print (" 3. Now you can open cli-calculator from any session by type this command: cli-cal ")
		print ()
		print ()
		print (" b) To update cli-calculator Follow these steps ↓↓")
		print ()
		print (" 1. First exit this tool by typing: qq")
		print (" 2. Then type this command: sh update.sh ")
		print ()
		print ()
		print ()
		print ("If you want to connect with us and share your feedback:")
		print ()
		print ("Our YouTube channel: https://www.youtube.com/channel/UCOBl9rXezNE5caIb1KeNiOg/")
		print ()
		print ("Our Website Link: https://sci-techstudio.blogspot.com")
		print ()
		print ("Our Telegram channel: https://t.me/scitechsolution")
		uni_fun()
			
	print ()
	print ("     ____Welcome to CLI Calculator___")
	print ()
	print ("     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
	print ("     | C L I   C a l c u l a t o r |")
	print ("     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
	print ()
	print ("                               v 0.1")
	print ()
	print ()
	print ("What operation do you want?")           
	print ()
	print ("---------------------------------------")
	print ("i) Mathematical Operations")
	print ("---------------------------------------")
	print (" 1) Summation        2) Subtraction")
	print (" 3) Multiplication   4) Division")
	print (" 5) Square  6) Cube  7) Discount")
	print ()
	print ()
	print ("---------------------------------------")
	print ("ii) Convert ")
	print ("---------------------------------------")
	print (" 21) Temperature      22) Length")
	print ()
	print () 
	print ("---------------------------------------")
	print ("iii) Other's")
	print ("---------------------------------------")
	print (" q) Exit     u) Update     h) Help ") 
	print (" d) Developer info      a) About it")
	print ()
	
	def input_fun():
		
		i=input ("Please Select any option: ")
		print ()
		ww=str(i)
		array=["1","2","3","4","5","6","7","21","22","q","d","h","u","a"]
		w=ww in array
	
		one="1"
		two="2"
		three="3"
		four="4"
		five="5"
		six="6"
		seven="7"
		twenty_one="21"
		twenty_two="22"
	
	
		q="q" 
		u="u"
		h="h"
		d="d"
		a="a"
		if w == True:
		
			m=str(i)
			print ()
			print ()
		
			if m == one:
		
				print (">You choose Summation...")
				print ("Now input two number")
				f=int(input("1st number: "))
				s=input("2nd number: ") 
				ff=int(f)
				ss=int(s)
				sum=float(ff+ss)
				print ("Your result: " + str(sum))
				
				uni_fun()
				
				
			elif m == two:
				print (">You choose Subtraction...")
				print ("Now input two number")
				f=input("1st number: ")
				s=input("2nd number: ") 
				ff=int(f)
				ss=int(s)
				sub=float(ff-ss)
				print ("Your result: " + str(sub))
				uni_fun()
			elif m == three:
				print (">You choose Multiplication...")
				print ("Now input two number")
				f=input("1st number: ")
				s=input("2nd number: ") 
				ff=int(f)
				ss=int(s)
				multi=float(ff*ss)
				print ("Your result: " + str(multi))
				uni_fun()
			elif m == four:
				print (">You choose Division...")
				print ("Now input two number")
				f=input("1st number: ")
				s=input("2nd number: ") 
				ff=int(f)
				ss=int(s)
				divi=float(ff/ss)
				print ("Your result: " + str(divi))
				uni_fun()
			elif m == five:
				print (">You choose Square...")
				print ("Now input one number")
				f=input("Target number: ")
				ff=int(f)
				sq=ff*ff
				print ("Your result: " + str(sq))
				uni_fun()
			elif m == six:
				print (">You choose Cube...")
				print ("Now input one number")
				f=input("Target number: ")
				ff=int(f)
				cu=ff*ff*ff
				print ("Your result: " + str(cu))
				uni_fun()
			elif m == seven:
				print (">You choose Discount...")
				print ("Now input two number")
				hh=input("Target Amount : ")
				gg=input("Discount rate in %: ") 
		
				hhh=int(hh)
				ggg=int(gg)
		
				dd=float(ggg/100)
				ddd=hhh*dd
		
				dddd=hhh-ddd
		
				print ("Amount in " + str(ggg) +"% Discount : " + str(dddd))
				uni_fun()
		
#convert part
		
###$$ temperature start from here 

			elif m == twenty_one:
				def uni_temp_fun():
					def uni_t_fun():
						print ()
						print ()
						print ("qq) Quit")
						print ("00) Back")
						print ("hh) Home")
						uni_input=input ("Please Select any option: ")
						uni_str=str(uni_input)
						uni_array=["qq","00","hh"]
						uni_data=uni_str in uni_array
						qq="qq"
						bck="00"
						hh="hh"
						if uni_data == True:
							uni_in_str=str(uni_input)
							if uni_in_str == qq:
							
								print ("You are exit from Cli-Calculator")
				
							elif uni_in_str == bck:
							
								uni_temp_fun()
								
							elif uni_in_str == hh:
								main_fun()
								
						else:
							print (">>Please select right option")
							uni_t_fun()
					print(">>You select Temperature")
					print ()
					print (" 31) Celsius to Fahrenheit")         
					print (" 32) Fahrenheit to Celsius")
					print (" 33) Celsius to Kelvin")
					print (" 34) Fahrenheit to Kelvin")
					print (" 35) Kelvin to Celsius")
					print (" 36) Kelvin to Fahrenheit")
					print (" 00) Back" )
					print ()
				
					def temp_fun():
					
						j=input ("Please Select any option: ")
						print ()
						print()
						wee=str(j)
						array=["31","32","33","34","35","36","00"]
						we=wee in array
						t_one="31"
						t_two="32"
						t_three="33"
						t_four="34"
						t_five="35"
						t_six="36"
						bck="00"
		
		
						if we == True:
							mm = str(j)
							if mm == t_one:
								print (">You select Celsius to Fahrenheit")
								print ()
								cel_in=float(input ("Input Your °C temp: "))
								ccel=cel_in*1.8
								ccl=ccel+32
								print ("Your temp result: " + str(ccl) + " °F")
								uni_t_fun()
							elif mm == t_two:
								print (">You select Fahrenheit to Celsius")
								print ()
								far_in=float(input ("Input Your °F temp: "))
								far_out=5*(far_in-32)  
								far_outt=far_out/9                                                         
								print ("Your temp result: " + str(far_outt) + " °C")                     #uii
								uni_t_fun()
							elif mm == t_three:
								print (">You select Celsius to Kelvin")
								print ()
								cel_in=float(input ("Input Your °C temp: "))
								cel_out=cel_in+273.15                                                       
								print ("Your temp result: " + str(cel_out) + " K")   #uiii
								uni_t_fun()
							elif mm == t_four:
								print (">You select Fahrenheit to Kelvin")
								print ()
								far_in=float(input ("Input Your °F temp: "))
								far_out=5*(far_in-32)  
								far_outt=far_out/9 
								far_outtt=far_outt+273.15
								print ("Your temp result: " + str(far_outtt) + " K") 
								uni_t_fun()
				
							elif mm == t_five:
								print (">You select Kelvin to Celsius")
								print ()
								kel_in=float(input ("Input Your K temp: "))
								kel_out=kel_in-273.15                                                    
								print ("Your temp result: " + str(kel_out) + " °C") 
								uni_t_fun()
							elif mm == t_six:
								print (">You select Kelvin to Fahrenheit")
								print ()
								kel_in=float(input ("Input Your K temp: "))
								kel_out=(kel_in-273.15)*1.8
								kel_final_out=kel_out+32
								print ("Your temp result: " + str(kel_final_out) + " °F")#uiii
								uni_t_fun()
							elif mm == bck:
								main_fun()
		
						else:
							print (">>Please select right option")
							temp_fun()
						
					temp_fun()
				uni_temp_fun()
				
###### temperature end here
				
###### length star here 
			elif m == twenty_two:
				def uni_lnth_fun():
					def uni_l_fun():
						print ()
						print ()
						print ("qq) Quit")
						print ("00) Back")
						print ("hh) Home")
						uni_input=input ("Please Select any option: ")
						uni_str=str(uni_input)
						uni_array=["qq","00","hh"]
						uni_data=uni_str in uni_array
						qq="qq"
						bck="00"
						hh="hh"
						if uni_data == True:
							uni_in_str=str(uni_input)
							if uni_in_str == qq:
							
								print ("You are exit from Cli-Calculator")
				
							elif uni_in_str == bck:
							
								uni_lnth_fun()
								
							elif uni_in_str == hh:
								main_fun()
								
						else:
							print (">>Please select right option")
							uni_l_fun()
					print(">>You select Length and Distance")
					print ()
					print (" 41) Kilometers to Miles")         
					print (" 42) Miles to Kilometers")
					print (" 43) Centimeters to Inch")
					print (" 44) Inch to Centimeters")
					print (" 45) Feet to Centimeters")
					print (" 46) Centimeters to Feet")
					print (" 00) Back" )
					print ()
				
					def lnth_fun():
					
						j=input ("Please Select any option: ")
						print ()
						print()
						wee=str(j)
						array=["41","42","43","44","45","46","00"]
						we=wee in array
						t_one="41"
						t_two="42"
						t_three="43"
						t_four="44"
						t_five="45"
						t_six="46"
						bck="00"
		
		
						if we == True:
							mm = str(j)
							if mm == t_one:
								print (">You select Kilometers to Miles")
								print ()
								cel_in=float(input ("Input Your km value: "))
								ccel=cel_in*0.621371192
								ccl=float(ccel)
								print ("Your result in miles: " + str(ccl) + " Mi")
								uni_l_fun()
							elif mm == t_two:
								print (">You select Miles to Kilometers")
								print ()
								far_in=float(input ("Input Your Mi value: "))
								far_out=far_in*1.609344
								far_outt=float(far_out)                                                    
								print ("Your result in km: " + str(far_outt) + " km")                     #uii
								uni_l_fun()
							elif mm == t_three:
								print (">You select Centimeters to Inch")
								print ()
								cel_in=float(input ("Input Your cm value: "))
								cel_out=float(cel_in*0.393700787)                                           
								print ("Your result in Inch: " + str(cel_out) + " in")   #uiii
								uni_l_fun()
							elif mm == t_four:
								print (">You select Inch to Centimeters")
								print ()
								far_in=float(input ("Input Your Inch value: "))
								far_out=float(far_in*2.54)
								print ("Your result in cm: " + str(far_out) + " cm") 
								uni_l_fun()
				
							elif mm == t_five:
								print (">You select Feet to Centimeters")
								print ()
								kel_in=float(input ("Input Your Feet value: "))
								kel_out=float(kel_in*30.48)                                            
								print ("Your result in cm: " + str(kel_out) + " cm") 
								uni_l_fun()
							elif mm == t_six:
								print (">You select Centimeters to Feet")
								print ()
								kel_in=float(input ("Input Your cm value: "))
								kel_out=kel_in*0.032808399
								kel_final_out=float(kel_out)
								print ("Your result in Feet: " + str(kel_final_out) + " ft")#uiii
								uni_l_fun()
							elif mm == bck:
								main_fun()
		
						else:
							print (">>Please select right option")
							lnth_fun()
						
					lnth_fun()
				uni_lnth_fun()
				
				
#########  length end here   
				
		
#others part 

			elif m==q:
	  
				print ("You are successfully exit from Cli Calculator ") 
		
			elif m==u:
				
				print (">>You select Update")
				print ()
				print ()
				print ("Use latest features of this tool must update it.")
				print ()
				print ("Automatic update system currently under maintenance")
				print ("Please manually update this tool")
				print ()
				print()
				print ("To manually update cli-calculator Follow these steps ↓↓")
				print ()
				print (" 1. First exit this tool by typing: qq")
				print (" 2. Then go cli-calculator directory: cd cli-calculator")
				print (" 3. Now type this command: sh update.sh ")
				uni_fun()
				
			elif m==h:
				help_fun()
			elif m==d:
				print (">>You select Developer Info")
				print ()
				print ()
				print ("...About Developer... ")
				print ()
				print ("Hi, My name is Alamin Sarkar. I'm a student of python Programming language.And this is my first tool which is write on python. In future I would add more features add on it.If you want to help me or share your feedback please visit help & feedback page.")
				print () 
				print ()
				print (" Thanks for using this tool")
				print ()
				print ("    _____Donate me____")
				print ("Litecoin address: MAtrCHMWqMv2R5C3oRxG33Vh4MMjTqfCSC")
				print ()
				print ()
				print ("hf) Help & Feedback")
				print ("00) Back")
				def dev_fun():
					
					dev_input=input ("Please Select any option: ")
					dev_str=str(dev_input)
					dev_array=["hf","00"]
					dev_data=dev_str in dev_array
					hf="hf"
					bck="00"
					if dev_data == True:
						dev_in_str=str(dev_input)
						if dev_in_str == hf:
							help_fun()
						elif dev_in_str == bck:
							
							main_fun()
						
					else:
						print (">>Please select right option")
						dev_fun()
						
				dev_fun()
				
				
			elif m==a:
				print (">>You Select About Cli-Calculator Tool")
				print ()
				print ()
				print ("This is a command line based calculator. You can use this calculator in any where with this shortcut command: cli-cal")        
				uni_fun()
		
		
		else:
			print (">>Please select right option")
			input_fun()
			
		
	input_fun()
main_fun()



