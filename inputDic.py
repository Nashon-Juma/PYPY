majina={}
Active=True

while majina:
    name=input('\n who are u ? ')
    answer=input("what's yr favorite animal ? ")
    repeat=input('would u like to continue')
    majina[name]=answer
    if repeat=='no':
        Active=False
print('-----------POLLS RESULTS---------------')
for name,answer in majina.items():
    print(name+ 'would like to have'+ answer)