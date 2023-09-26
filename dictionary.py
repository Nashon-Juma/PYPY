def noD():
    no=dict()
    no['1']='one'
    no['2']='two'
    no['3']='three'
    no['4']='four'
    return no

def main():
    dictionary=noD()
    print(dictionary['1'])
    print(dictionary['2'])
    print(dictionary['3'])
    print(dictionary['4'])

def man():
    dictionary=noD()
    print('thi is th most absurd thing '+dictionary['1']+' thig I have seen this year')

def other():
    sentence='no in words: {i88},{i90},{i78}.'
    subs=sentence.format (i88='three',i90='phor',i78='five')
    print(subs)

def noj():
    dictionary=noD()
    Nfor='spanish numbers: {1},{2},{3}'
    subst=Nfor.format(**dict)
    print(subst)
noj()