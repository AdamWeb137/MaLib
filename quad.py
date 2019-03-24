
def iseval(num):
    try:
        eval(num)
        return True
    except (ValueError, SyntaxError):
        print("error")
        return False

def QuadStandConv(anum,bnum,cnum):
    anum = anum.replace("^", "**")
    bnum = bnum.replace("^", "**")
    cnum = cnum.replace("^", "**")
    if iseval(anum) and iseval(bnum) and iseval(cnum):
        a = eval(anum)
        b = eval(bnum)
        c = eval(cnum)

        #Factored Form conversion
        r1 = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
        r2 = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)

        if b**2 - 4*a*c < 0:
            r1 = "na"
            r2 = "na"

        factored = {
            "a":a,
            "r1":r1,
            "r2":r2
        }

        #Vertex Form Conversion

        vertex = {
            "a":a,
            "h":(-b/(2*a)),
            "k":a*(-b/(2*a))**2 + b*(-b/(2*a)) + c
        }

        return {
            "factor_form":factored,
            "vertex_form":vertex
        }
    else:
        return "error"

def QuadVertConv(anum,hnum,knum):
    anum = anum.replace("^", "**")
    bnum = bnum.replace("^", "**")
    cnum = cnum.replace("^", "**")
    if iseval(anum) and iseval(hnum) and iseval(knum):
        a = eval(anum)
        h = eval(hnum)
        k = eval(knum)

        standard = {
            "a":a,
            "b":-2*a*h,
            "c":a*(h**2) + k
        }

        factored = QuadStandConv(str(standard["a"]),str(standard["b"]),str(standard["c"]))["factor_form"]

        return {
            "standard_form":standard,
            "factor_form": factored
        }
    else:
        return "error"

def QuadFacConv(anum,r1n,r2n):
    anum = anum.replace("^", "**")
    bnum = bnum.replace("^", "**")
    cnum = cnum.replace("^", "**")
    if iseval(anum) and iseval(r1n) and iseval(r2n):
        a = eval(anum)
        r1 = eval(r1n)
        r2 = eval(r2n)

        standard = {
            "a":a,
            "b":a*(-r1-r2),
            "c":a*(r1*r2)
        }

        vertex = QuadStandConv(str(standard["a"]),str(standard["b"]),str(standard["c"]))["vertex_form"]

        return {
            "standard_form":standard,
            "vertex_form": vertex
        }
    else:
        return "error"
