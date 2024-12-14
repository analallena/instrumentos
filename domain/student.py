class Student:
    def __init__(self, email, class_group, preference1, preference2, preference3, excluded):
        self.email = email
        self.class_group = class_group
        self.preference1 = preference1
        self.preference2 = preference2
        self.preference3 = preference3
        self.excluded = excluded
        self.assigned = None

    def __str__(self):
        return "{}: {}".format(self.email, self.assigned)

    def __repr__(self):
        return "{}: {}".format(self.email, self.assigned)
