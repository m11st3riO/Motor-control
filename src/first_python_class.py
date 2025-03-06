first_name="emilio"
midde_name='sergio'
last_name="palacios"
fullname=first_name.title()+" "+ midde_name.title()+' '+last_name.title()
moto= ['Italika', 'BMW','Kawasaki']


print(first_name.title(), midde_name.rstrip())
print(last_name.upper())
print(last_name.lower())
print(fullname)

print(moto)
moto.insert(1,"vespa")
moto.pop()
print(moto)
for moto in moto:
    print(moto)