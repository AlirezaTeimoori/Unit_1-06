#Created by: Alireza Teimoori
#Created on: 28 Sep 2017
#Created for: ICS3UR-1
#Lesson: Unit 1-06
#This program is for learing that we can use local and global variables

import ui

variableX = 25

def local_button_touch_up_inside(sender):
    #shows what happens to local variable
	
    variableX = 10
    variableY = 30
    variableZ = variableX + variableY	
    view['local_answer_lable'].text = str(variableZ)
	
def global_button_touch_up_inside(sender):
    #shows what happens to global variable

    global variableX
    variableX = variableX+1
    variableY = 30
    variableZ = variableX+variableY	

    view['global_answer_lable'].text = str(variableZ)
    
view = ui.load_view()
view.present('sheet')
