from views.modified_python_files.vector_window import VectorWindow

class VectorController():
    def __init__(self)->None:
        self.vector_window = None

    def set_window(self,window:VectorWindow):
        if isinstance(self.vector_window,VectorWindow):
            self.vector_window.deleteLater()
        self.vector_window = window
    
    def connect_buttons(self):
        self.vector_window.vxv_row_spinbox.valueChanged.connect(lambda: self.vector_window.vxv_change_row_vector())
        self.vector_window.vxv_solve_scalar_button.clicked.connect(lambda: self.vector_window.vxv_show_scalar())
        self.vector_window.mxv_column_add_vector_button.clicked.connect(lambda: self.vector_window.mxv_add_vector())
        self.vector_window.mxv_column_substact_vector_button.clicked.connect(lambda: self.vector_window.mxv_delete_vector())
        self.vector_window.mxv_solution_button.clicked.connect(lambda: self.vector_window.mxv_show_scalar())
        self.vector_window.mxm_add_column_button.clicked.connect(lambda: self.vector_window.mxm_add_column_table_b())
        self.vector_window.mxm_substract_column_button.clicked.connect(lambda: self.vector_window.mxm_substract_column_table_b())
        self.vector_window.mxm_solution_button.clicked.connect(lambda: self.vector_window.mxm_show_matrix_c())

    def open_vector_window(self):
        self.connect_buttons()
        self.vector_window.show()

    