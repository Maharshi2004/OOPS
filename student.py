class student:
    school_name="XYZ School"
    def set_details(self):
        self.name = "Vamsi"
        self.marks = 85
    def display(self):
        print(self.name)
        print(self.marks)
s=student()
s.set_details()
s.display()