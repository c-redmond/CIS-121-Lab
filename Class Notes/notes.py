class Star:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self, name_2):
        self.name = name_2
    def __str__(self):
        msg = ''
        msg += f'the star known as {self.name}'
        return msg

sun = Star('sol')