from StudentMengerController import StudentMengerController
from StudentMengerMode import StudentMengerMode
from StudentMengerView import StudentMengerView

#学生管理系统
view = StudentMengerView(StudentMengerController(StudentMengerMode))
while True:
    value = input('请输入指令(直接回车退出):')
    if value == '':
        break
    else:
        view.check_input(value)
