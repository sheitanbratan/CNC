file = open("G-code.txt", "w")

ZSP = float(input('Enter Z axis start point:'))
XSP = float(input('Enter X axis start point:'))
ZFP = float(input('Enter Z axis finish point:'))
XFP = float(input('Enter X axis finish point:'))
DOC = float(input('Enter depth of cut:'))
F = float(input('Enter feed:'))
QOC = (XFP-XSP)/DOC     #Quantity of cuts

X = "X"
Z = "Z"
CUT = (XSP)


file.write(f"G0 Z{ZSP}\n") # go to Z start point
file.write(f"G0 X{XSP}\n") # go to X start point


while CUT<XFP:
    CUT+=DOC
    SFV = round(CUT, 2)
    if SFV>XFP:
        SFV = XFP
    SET = "X" + str(SFV)



    file.write(f"{SET}\n") # go to X work point
    file.write(f"G1 Z{ZFP} F{F}\n") # go to Z finish point with feed
    file.write(f"G0 X{XSP}\n") # exit to the X start point
    file.write(f"Z{ZSP}\n") # fast travel to Z start point

file.close()

