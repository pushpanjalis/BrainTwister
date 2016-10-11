from time import sleep
　
　
def again():
	print('select a number from 1 to 10 \n')
	sleep(3)
	print('multiply the number with 2 \n')
	sleep(3)
	print('add 2 to the result \n')
	sleep(3)
	print('multiply the number with 5 \n')
	sleep(3)
	print('add 5 to the result \n')
	sleep(3)
	print('multiply the number with 10 \n')
	sleep(3)
	print('add 10 to the result \n')
	sleep(3)
def result(num):
	return int(num/100-1)
again();	
	
yes=input('are you done with the calucation.type done if yes \n')
if yes.lower() == "done":
	num=int(input('enter the final result \n'))
	if num%100==60:
		print('the no. is',result(num))
	else:
		print('yeduu..mistake in calculation.do it again \n')
else:
	print('take your time \n');
	
play=input("you wanna play? Type Y if yes otherwise N for No \n")
if play.lower()=='y':
	again()
if play.lower()=="n":
	print ('Thank you for your time.Hope you enjoyed')
else:
	print('wrong input')
