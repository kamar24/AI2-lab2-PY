tab1=[0,1,2,3]
tab2=[3,5,9,8]
tab3=["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]
tab4=['apple', 'orange', 'pear']

print([x+x+1 for x in tab1])
print([x%3==0 for x in tab2])
print([x[3:-1]+x[-1] for x in tab3 if x[0]=="T" and x[1]=="A"])
print([x[0].upper() for x in tab4])
print([x for x in tab4 if x[0]=="a"or x[0]=="p"])
print([[x,x.__len__()] for x in tab4])

arr={}
for x in tab4:
    arr[x]=arr.get(x,x.__len__())
print(arr)