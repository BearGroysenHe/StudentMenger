#学生管理系统控制器模块
class StudentMengerController:
    def __init__(self,StudentMengerMode):
        self.__mode = StudentMengerMode
        self.__mode.load_mode()

    def save_mode(func):
        def wrapper(self):
            func(self)
            with open('mode.txt','w',encoding='utf-8') as mode:
                for student in self.__mode.student_list:
                    mode.write("cls('%s', '%s', '%s', '%s')\n"%(student.id,student.name,student.age,student.score))
        return wrapper

    @save_mode
    def add_student(self):
        id = input('请输入学生的ID:')
        if self.__mode.check_repeat(id):
            print('您输入的id重复，请重新输入')
            return
        name = input('请输入学生的名字:')
        age = input('请输入学生的年龄:')
        score = input('请输入学生的成绩:')
        new_student = self.__mode(id,name,age,score)
        self.__mode.student_list.append(new_student)

    def print_students(self):
        for mode in self.__mode.student_list:
            print('学生的ID为：%s'%(mode.id))
            print(mode.name,mode.age,mode.score)

    @save_mode
    def remove_student(self):
        id = input('请输入要删除的学生的编号')
        index = self.__mode.find_student_by_id(id)
        del self.__mode.student_list[index]

    @save_mode
    def update_student(self):
        id = input('请输入要修改的学生编号:')
        item = input('请输入要修改的项目(name,age,score):')
        value = input('请输入要修改的值：')
        if item == 'name':
            self.__mode.student_list[id-1].name = value
        elif item == 'age':
            self.__mode.student_list[id-1].age = value
        elif item == 'score':
            self.__mode.student_list[id-1].score = value

