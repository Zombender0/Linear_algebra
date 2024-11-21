from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QPropertyAnimation, QSize
from functools import wraps

def property_handler(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        widget:QWidget = args[0]
        
        if widget.property('state') is None:
            widget.setProperty('state','expanded')

        state = 'expanded' if widget.property('state') == 'collapsed' else 'collapsed'
        widget.setProperty('state',state)

        function(*args,**kwargs)
    return wrapper

@property_handler
def animate_side_bar(side_widget: QWidget, start_size: QSize, end_size: QSize):
    animation = QPropertyAnimation(side_widget, b"maximumSize")
    animation.setDuration(150)
    if side_widget.property('state') == 'expanded':
        animation.setStartValue(start_size)
        animation.setEndValue(end_size)
    else:
        animation.setStartValue(end_size)
        animation.setEndValue(start_size)
    side_widget.animation = animation
    animation.start()