list1=[1,2,1]
list2=[3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")
copy_list2=list2.copy()
copy_list2.reverse()
if(copy_list2==list2):
    print("palindrome")
else:
    print("not a palindrome")