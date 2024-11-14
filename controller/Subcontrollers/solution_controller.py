from views.modified_python_files.solution_window import SolutionWindow

class SolutionController():
    def __init__(self)->None:
        self.solution_window = None

    def set_window(self,window:SolutionWindow)->None:
        if isinstance(self.solution_window,SolutionWindow): 
            self.solution_window.deleteLater()
        self.solution_window = window

    def connect_buttons(self)->None:
        self.solution_window.back_tab_button.clicked.connect(lambda: self.solution_window.previous_tab())
        self.solution_window.next_tab_button.clicked.connect(lambda: self.solution_window.next_tab())
        self.solution_window.tab_widget.currentChanged.connect(lambda: self.solution_window.show_step_property())
    
    def open_window(self):
        self.connect_buttons()
        self.solution_window.show()

    def open_solution_window(self,config:dict)->None:
        self.solution_window.create_tab_solutions(config)
        self.open_window()

    def open_determinant_window(self,config:dict)->None:
        self.solution_window.create_determinant_step(config)
        self.open_window()

    def open_cramer_window(self,config:dict)->None:
        self.solution_window.create_cramer_solution(config)
        self.open_window()

    def open_invertible_matrix_window(self,config:dict)->None:
        self.solution_window.create_invertable_solution(config)
        self.open_window()

    def open_bisection_equation_window(self,config:dict)->None:
        self.solution_window.create_bisection_solution(config)
        self.open_window()

    def open_newton_equation_window(self,config:dict)->None:
        self.solution_window.create_newton_solution(config)
        self.open_window()

    def open_false_position_equation_window(self,config:dict)->None:
        self.solution_window.create_false_position_solution(config)
        self.open_window()
