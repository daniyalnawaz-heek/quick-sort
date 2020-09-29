def sort_it(list1,start,end):
  #print(list1)
  
  if start==end:
    return
  pivot=end
     
  i=0
  j=pivot-1
    
  while i<=j:
      while i<=j and list1[i]<=pivot:
        i=i+1
    
      while i<=j and list1[j]>=pivot:
        j=j-1
        
      if i<=j: 
        list1[i],list1[j]=list1[j],list1[i] 
        
      
      
  
  if i>j:
      list1[end],list1[i]=list1[i],list1[end]
      
    
      
    
    
  sort_it(list1,start,i-1)
  sort_it(list1,i+1,end)  
    
    
    
    
    
    
    
  
  
    
  

  
list2=[58,37,85,27,48,47,7,76]
n=len(list2)-1
sort_it(list2,0,n-1)
print(list2)  
  
      