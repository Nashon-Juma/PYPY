majinaa={}
Active=True

while majinaa:
    name=input('\n who are u ? ')
    answer=input("what's yr favorite animal ? ")
    repeat=input('would u like to continue')
    majinaa[name]=answer
    if repeat=='no':
        Active=False
print('-----------POLLS RESULTS---------------')
for name,answer in majinaa.items():
    print(name+ 'would like to have'+ answer)
