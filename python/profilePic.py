l=input()
n = input()
ok=0
while (ok ==0):
    w,h =raw_input().split()


    if w<l:
        print ("UPLOAD ANOTHER")
    elif h<l:
	print ("UPLOAD ANOTHER")
    elif (w!=h):
	print ("CROP IT")
    else :
        ok=1

print ("ACCEPTED")



