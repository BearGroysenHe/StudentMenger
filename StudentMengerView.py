#学生管理系统界面模块
class StudentMengerView:
    def __init__(self,StudentMengerController):
        self.__controller = StudentMengerController
        print('请输入指令进行学生系统管理。')
        print('1：添加学生信息。2:显示所有学生信息。3:删除学生信息.4,修改学生信息.')

    def check_input(self,value):
        if value == '1':
            self.__controller.add_student()
        elif value == '2':
            self.__controller.print_students()
        elif value == '3':
            self.__controller.remove_student()
        elif value == '4':
            self.__controller.update_student()