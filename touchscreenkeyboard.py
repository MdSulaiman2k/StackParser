def orde(st , st1) :
  for i in range(len(st)) :
    if(ord(st1[i]) > ord(st[i])):
      return False
    elif(ord(st1[i]) < ord(st[i])) :
      return True 

  return False

lis = [ ['q' ,'w' , 'e' , 'r' , 't' , 'y' , 'u' , 'i' , 'o' , 'p'] , ['a' , 's' , 'd' ,'f' , 'g' ,'h'  ,'j' , 'k' , 'l'] , ['z' , 'x' , 'c' , 'v' , 'b' , 'n' , 'm'] ]

n = int(input())
for i in range(n) :
  st , num = input().split()
  a = [0]*int(num)
  mincount = [0] *int(num)
  for j in range(int(num)):
    a[j] = input()
    c = 0
    cnt = 0 
    for k in st :
      if(a[j][c] != k) :
        row , row1 , col , col1 = 0 , 0, 0,0
        ck = 0 
        for l in range(len(lis)):
          for m in range(len(lis[l])):
            if(a[j][c] == lis[l][m]):
              row = l
              col = m
              ck += 1
            elif(k == lis[l][m]) :
              row1 = l
              col1 = m
              ck += 1
            elif(ck == 2):
              break
          if(ck == 2 ) :
            break 
              
        cnt += abs(row-row1) + abs(col-col1)
      c += 1
    mincount[j] = cnt
    j+= 1
  for i in range(int(num)-1) :
    for j in range(int(num)-1):
      if(mincount[j] > mincount[j+1]):
        mincount[j] , mincount[j+1] = mincount[j+1] , mincount[j]
        a[j] , a[j+1] = a[j+1] , a[j]
  
  setvalue = set(mincount)
  dif =  len(mincount)- len(setvalue) 
  for k in range(dif) :
    for i in range(int(num)-1):
      for j in range(int(num)-1):
        if(mincount[j] == mincount[j+1]) :
          if(orde(a[j] , a[j+1])):
            mincount[j] , mincount[j+1] = mincount[j+1] , mincount[j]
            a[j] , a[j+1] = a[j+1] , a[j]
          
            
            
          






    


  
 
        



  for j in range(int(num)) :
    print(a[j] , mincount[j]) 
      



        

          
        
      

