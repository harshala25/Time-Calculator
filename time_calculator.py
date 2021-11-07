def add_time(start, duration,day=False):
  hrs=int(start[:-6])
  mins=int(start[-5:-3])
  clk=start.split()[1]
  clk1=clk
  time=["PM","AM"]
  hrs1=int(duration.split(':')[0])
  mins1=int(duration.split(':')[1])
  q=['Monday','tuesday','Wednesday','Thursday','Friday','saturDay','Sunday']
  mins+=mins1
  if mins>=60:
    hrs+=1
    mins=mins%60
  hrs+=hrs1
  x=(hrs/24)
  if hrs>12:
    while hrs>12:
       hrs=int(hrs-12)
       if clk==time[0]:
        clk=time[1]
       else:
        clk=time[0] 
  y=hrs
  if hrs==12 and mins>0:
    if clk==time[0]:
      clk=time[1]
    else:
      clk=time[0]
  if day:
    v=q.index(day)+round(x)
    if v>6:
      day=q[int(v%7)]
    else:
      day=q[int(v)]
    if x<1 and (clk1==clk or clk=="PM"):
      result=str(y)+':'+str(mins).zfill(2)+" "+str(clk)+','+" "+day
      return result
    elif round(x)==1:
      result=str(y)+':'+str(mins).zfill(2)+" "+str(clk)+','+" "+ day+" "+'(next day)'
      return result
    elif round(x)>1:
     result=str(y)+':'+str(mins).zfill(2)+" "+str(clk)+','+" "+day+" "+'('+str(round(x))+' days later)'
     return result
  else:
    if x<1 and (clk1==clk or clk=="PM"):
      result=str(y)+':'+str(mins).zfill(2)+" "+str(clk)
      return result
    elif round(x)==1:
      result=str(y)+':'+str(mins).zfill(2)+" "+str(clk)+" "+'(next day)'
      return result
    elif round(x)>1:
      result=str(y)+':'+str(mins).zfill(2)+" "+str(clk)+" "+'('+str(round(x))+' days later)'
      return result



  

          

        
    
    



  

  
