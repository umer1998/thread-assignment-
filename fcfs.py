pro = int(input("enter number of process >>>"))
bt = []
at = [] 
for i in range (0,pro): 
	c = int(input("enter arrval time >>>"))
	at.append(c)
	a = int(input("enter burst time >>>")) 
	bt.append(a)
if at[0]==0: 
	print (" ")
	print("process 1 wait for :" +str(0)) 
	print (" ") 
	print("process 1 start at :" +str(at[0])) 
	print (" ") print("process 1 ends at :" +str(bt[0])) 
	print (" ") 
if at[0]!=0: 
	print("process 1 wait for :" +str(at[0])) 
	print (" ") 
	print("process 1 start at :" +str(at[0])) 
	print (" ") 
	print("process 1 ends at :" +str(bt[0]+at[0])) 
	print (" ")
wait=at[0]
start= at[0] 
end = at[0]+bt[0] 
for i in range (1,pro):
if at[i]>end:	
	wait=at[i]-end
	start=at[i]
	end=at[i]+bt[i]
	
	print ("   ")
	print'process ' +str(i+1)   ,'wait for :' +str(wait)
	print ("   ")
	print 'process ' +str(i+1) ,' start at :' + str(start)
	
	print ("   ")
	print'process' +str(i+1) , 'ends at :' + str (end)
	print ("   ")
else:
	wait=0
	start=end
	end=end+bt[i]
	
	print ("   ")
	print 'process ' +str(i+1) , ' wait for : ' +str(wait)
	
	print ("   ")
	print 'process ' +str(i+1) ,' start at :' + str(start)
	
	print ("   ")
	print'process' +str(i+1) , 'ends at :' + str (end)
	print ("   ")

