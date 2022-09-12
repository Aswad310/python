class Workers:
    # setter
    def set_name(self, name):
        self.name= name

    def set_id(self, id):
        self.id= id

    # getter
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id

# object Instance
workers= Workers()

workers.set_name("Ali Hassan")
workers.set_id(123)

print("Your name is:",workers.get_name(),"and id is:",workers.get_id())