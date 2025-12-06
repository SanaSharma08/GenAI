device_status="active"
temp=28

if device_status == "active":
    if temp > 35:
        print("Warning! High Temperature")
    else:
        print("Normal")
else:
    print("Device Offline")