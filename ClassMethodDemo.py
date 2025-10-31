class student:
    subject = "python"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_subject(cls):
        return cls.subject

    @classmethod
    def set_subject(cls, new_subject):
        cls.subject = new_subject

print(student.get_subject())

student.set_subject("Java")
print(student.get_subject())
