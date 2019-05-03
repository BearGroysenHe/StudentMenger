#学生管理系统数据库模块
class StudentMengerMode:
    student_list = []
    def __init__(self,id,name,age,score):
        self.name = name
        self.age = age
        self.score = score
        self.__id = id

    @classmethod
    def load_mode(cls):
        with open('mode.txt','r',encoding='utf-8') as mode:
            for info in mode:
                new_student = eval(info)
                cls.student_list.append(new_student)

    @classmethod
    def find_student_by_id(cls,id):
        index = 0
        for item in cls.student_list:
            if item.id == id:
                return index
            index += 1

    @classmethod
    def check_repeat(cls,id):
        for student in cls.student_list:
            if student.id == id:
                return True
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        self.__score = value

    @property
    def id(self):
        return self.__id
