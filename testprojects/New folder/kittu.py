indian =["samosa","daal","naan"]
italian=["pizza","pasta","risotto"]
chinese=["egg role","pot stricker"," fried rice"]

dish =input("enter a dish name :")
if dish in indian :
    print("indian")
elif dish in italian :
    print("italian")
elif dish in chinese:
    print("chinese")
else:
    print("nothing")
