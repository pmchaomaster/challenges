list1 =['9','5','4','6']
list2 =['1','3','5','5']
final_list=[]
n=-1
carry_over =0

while n >=-len(list1):
    sum=int(list1[n])+int(list2[n])+carry_over
    singleDigit=sum %10
    final_list.insert(0,singleDigit)
    carry_over = sum//10
    n-=1
final_list.insert(0, carry_over)

print (final_list)