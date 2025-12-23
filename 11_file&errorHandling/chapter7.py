# File Handling with try except and with
# file=open("order.txt","w")
# try:
#     file.write("Masala chai - 2")
    
# finally:
#     file.close()


# Modern Method
# with tackles exception handling and close() in the back side for you!
with open("order2.txt","w") as file:
    #safe
    file.write("ginger tea - 4 cups")
