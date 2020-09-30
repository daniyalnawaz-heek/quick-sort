def quick_sort(list1,start,end):
  if start>=end:
    return
  
  k=partiton(list1,0,end)
  quick_sort(list1,0,k-1)
  quick_sort(list1,k+1,end)    
  
  
def partiton(list1,start,end):
  pivot=list1[end]
  i=start
  j=end-1 
  while True:
    while i<=j and list1[i]<pivot:
      i=i+1 
    
    while i<=j and list1[j]>pivot:
      j=j-1 
    if i<=j:
      list1[i],list1[j]=list1[j],list1[i]   
   
  if i>j:
    list1[i],list1[end]=list1[end],list1[i]
    
  return i      
    
    
    
    
list2=[54,74,997,36,478,9792,58,0,6,163,6,85,1] 
end=len(list2)-1
print(quick_sort(list2,0,end))   