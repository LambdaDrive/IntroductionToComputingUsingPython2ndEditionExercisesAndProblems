def pay(wage, hours):
    if hours>40:
        overtime = hours - 40
        pay = (40*wage)+((wage*1.5)*overtime)
        return pay
    else:
        pay = hours*wage
        return pay
