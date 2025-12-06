#Using dictionary in place of match case for better compatibility.
users=[
    {"id":1, "total":150,"coupon":"DISCOUNT10"},
    {"id":2, "total":80,"coupon":"NONE"},
    {"id":3, "total":200,"coupon":"DISCOUNT20"},
    {"id":4, "total":50,"coupon":"NONE"},
    {"id":5, "total":120,"coupon":"DISCOUNT15"},
    {"id":6, "total":300,"coupon":"DISCOUNT25"}
]
discounts={
    # Coupon code : (%age discount, min purchase amount)
    "DISCOUNT10":(0.25,50),
    "DISCOUNT15":(0.30,100),
    "DISCOUNT20":(0.35,150),
    "DISCOUNT25":(0.40,200),
    "NONE":(0,0)
}

for user in users:
    discount_percentage, min_amount=discounts.get(user["coupon"],(0,0)) #Default(0,0) to no discount if coupon not found
    discount = user["total"] * discount_percentage if user["total"] >= min_amount else 0
    print(f"User ID: {user['id']}, Original Total: ${user['total']:.2f}, Discount: ${discount:.2f}, Final Total: ${user['total'] - discount:.2f}")