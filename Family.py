class Father:
    father_name=""
    father_age=None

    def __init__(self,name="",age=""):
        self.father_name=name
        self.father_age=age

    def set_father_age(self,name):
        if name is not " ":
          self.father_name=name

    def set_father_age(self,age):
        if age is not None:
            self.father_age=age

    def get_father_name(self):
        return self.father_name

    def get_father_age(self):
        return self.father_age

class Mother:
    mother_name = ""
    mother_age = None

    def __init__(self, name="", age=""):
        self.mother_name = name
        self.mother_age = age

    def set_mother_name(self, name):
        if name is not " ":
            self.mother_name = name

    def set_mother_age(self, age):
        if age is not None:
            self.mother_age = age

    def get_mother_name(self):
        return self.mother_name

    def get_mother_age(self):
        return self.mother_age

class Child(Father,Mother):
    child_name = ""
    child_age = None
    f = Father()
    m = Mother()

    def __init__(self, name, age):
        super(Father, self).__init__()
        super(Mother, self).__init__()
        self.child_name = name
        self.child_age = age

    def set_child_name(self,name):
        if name is not "":
            self.child_name=name

    def get_child_name(self):
        return self.child_name

    def get_child_age(self):
        return self.child_age

    def set_father(self, father_name, father_age):
        if father_name is not "":
            self.father_name=father_name
        if father_age is not None:
            self.father_age=father_age

    def set_mother(self, mother_name, mother_age):
        if mother_name is not "":
            self.mother_name = mother_name
        if mother_age is not None:
            self.mother_age = mother_age

    def set_parents(self, father_details, mother_details):
        self.father_name=father_details['name']
        self.father_age=father_details['age']
        self.mother_name = mother_details['name']
        self.mother_age = mother_details['age']

class Family(Child):
    # parents={"father_name": self.father_name ,"mother_name":mother_name,"father_age":father_age,"mother_age":mother_age}
      #parent = {'father': father_details, 'mother': mother_details}

    parents={}
    children=list()
    last_name=""

    def __init__(self, parents, children, last_name=''):
        super(Child, self).__init__()
        self.parents=parents
        self.children.append(children)
        self.last_name=last_name

    def add_child(self, child_name, child_age):
        child={child_name:child_age}
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_child(self, i):
        return self.children[i]

    def get_parents_names(self):
        return self.father_name,self.mother_name

if __name__ == '__main__':
    children =dict()
    father_name=input("enter father name...")
    father_age=input("enter father age...")
    mother_name = input("enter mother name...")
    mother_age = input("enter mother age...")
    num_child=int(input("enter the num of children..."))
    while num_child>0:
        child_name = input("enter the name child...")
        child_age = input("enter the age child...")
        children[child_name]=child_age
        num_child-=1
    last_name=input("enter the last name...")
    father_details={'father_name':father_name,'father_age':father_age}
    mother_details={'mother_name':mother_name,'mother_age':mother_age}
    parent={'father':father_details,'mother':mother_details}
    f=Family(parent,children,last_name)
    print(f.parents,f.children,f.last_name)
