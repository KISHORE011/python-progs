class laptop:
    def __init__(self):
        self.ram=''
        self.processor=''
    def display(self):
        print('ram', self.ram)
        print('processor',self.processor)

hp=laptop()
dell=laptop()

hp.ram='32gb'
hp.processor='i7'

dell.ram='16gb'
dell.processor='i9'

hp.display()
dell.display()
