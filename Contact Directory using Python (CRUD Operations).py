

# Contact Directory using Python (CRUD Operations)

contact_list=[['ravi',7878900041,'ravi24@gmail.com'],
              ['prem',9444321049,'prem@gmail.com'],
              ['reenuka',8321421092,'renu@yahoo.com'],
              ['kavin',9546187307,'kavin@gmail.com'],
              ['Akalaya',8467135948,'aka789@hotmail.com']
              ]
print(contact_list)
#add item
contact_list.append(['john',9456713589,'john456@yahoo.com'])
print(contact_list)
#remove the last item
contact_list.pop()
print(contact_list)
#Adding new details
c1=input("enter your name")
print(c1)
c2=input("enter your number")
print(c2)
c3=input("enter your email")
print(c3)
contact_list.append([c1,c2,c3])
print(contact_list)
contact_asc=sorted(contact_list)
print(contact_asc)