class goa:
    name=""
    drink=""
    def party(self):
        print('lets party..')
    def beach(self):
        print('enjoing the beach')

ramesh = goa()
suresh = goa()

ramesh.name= "RAMESH"
suresh.name= "SURESH"

ramesh.drink= "yes"
suresh.drink= "no"

print(ramesh.name)
print(ramesh.drink,'sure')
print(suresh.name)
print(suresh.drink,'i am not drink')
