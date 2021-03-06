import importlib
from PyQt5 import QtWidgets
from GUI.week_window import Window
import help_file
import main_win


class WeekWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(WeekWindow, self).__init__()
        self.ui = Window()
        self.ui.setup_ui(self)

        self.ui.save_button.clicked.connect(self.save_and_close)

    def save_and_close(self):
        days = ''

        if self.ui.monday.isChecked():
            days += 'Mon '
        if self.ui.tuesday.isChecked():
            days += 'Tue '
        if self.ui.wednesday.isChecked():
            days += 'Wed '
        if self.ui.thursday.isChecked():
            days += 'Thu '
        if self.ui.friday.isChecked():
            days += 'Fri '
        if self.ui.saturday.isChecked():
            days += 'Sat '
        if self.ui.sunday.isChecked():
            days += 'Sun'

        clear_days = days.strip()  # удаление пробелов в конце строки на случай если последний день не воскресенье

        query = f"""
                    UPDATE data SET
                        name = '{self.ui.name.text()}',
                        days = '{clear_days}',
                        hour = '{self.ui.hour.text()}',
                        minutes = '{self.ui.minutes.text()}'
                    WHERE id = {int(help_file.active_id)}
                """
        help_file.database.update_data('data\\week.sqlite', query)

        # закрытие окон и открытие обновленного main_win
        help_file.main_class.close_main_window()
        help_file.main_class.close_week_window()
        importlib.reload(main_win)
        help_file.main_class.open_main_window()
