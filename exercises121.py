def nhap_Dict():
    try:
        l1 = list(map(int,input('Nhập các giá trị key cho dict: ').split()))
    except:
        print('Giá trị key là một số nguyên dương')
        return None

    l2 = input('Hãy nhập các giá trị value cho dict: ').split()

    if len(l1) != len(l2):
        print('Số lượng key và value phải bằng nhau')
        return None
    else: 
        dictKetQua = dict(zip(l1,l2))
    return dictKetQua
    
def sap_Xep_Key(dictA):
    xepKey = sorted(dictA.keys())
    dictB = {}
    for key in xepKey:
        dictB[key] = dictA[key]
    return dictB

dictA = nhap_Dict()
if dictA is not None:
    dictB = sap_Xep_Key(dictA)
    print(dictA)
    print(dictB)