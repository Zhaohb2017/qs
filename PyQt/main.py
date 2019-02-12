# -*- coding: utf-8 -*-
__author__ = '...'

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow,QMessageBox

from WeatherWin import *
from ServerConnection import Connection
import time
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._connect_majiang = Connection()
        self._main_version = 9037
        self._changsha_version = 9011
        self._changde_version = 9010
        self._version_paohuzi = "paohuzi"
        self._version_majiang = "majiang"
        self._version_runfast = "runfast"
        self._main_path_name = "newworkspace"
        self._changsha_path_name = "csworkspace"
        self._changde_path_name = "cdworkspace"
        self._test_main_path_name = "majiang_worspace"
        self._test_changsha_path_name = "majiangcs_worspace"
        self._test_changde_path_name = "majiangcd_worspace"
        self._version_sign_test = "test"  #测试服标志
        self._version_sign_local = "local"  # 本地服标志


    def stack_card(self,version,version_name,version_sign):
        """做牌"""
        card_data = self.ui.plainTextEdit.toPlainText()
        if len(card_data) == 0:
            return False
        else:
            if card_data[0] != "{" or card_data[-1] != "}":
                return False
            else:
                upload_data = '''%s''' % card_data
                print(upload_data)
                self._connect_majiang.card_write_file(version=version,write_data=upload_data,version_name=version_name,version_sign=version_sign)
        return True

    def show_message(self):
        QMessageBox.critical(self,"错误","请输入json格式数据")


    def startService(self):
        versionsName = self.ui.weatherComboBox.currentText()
        portNumber = self.ui.portComboBox.currentText()

        data = ""
        if int(portNumber) == self._main_version:   #主版本
            if versionsName == "本地跑胡子":
                stack_checkout = self.stack_card(self._main_path_name,self._version_paohuzi,self._version_sign_local)
                if stack_checkout:
                    self._connect_majiang.main_local_paohuzi_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success "%(versionsName,portNumber))
                else:
                    self.show_message()

            elif versionsName == "本地麻将":
                stack_checkout = self.stack_card(self._main_path_name,self._version_majiang,self._version_sign_local)
                if stack_checkout:
                    self._connect_majiang.main_local_majiang_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))

                else:
                    self.show_message()
            elif versionsName == "本地跑得快":
                stack_checkout = self.stack_card(self._main_path_name,self._version_runfast,self._version_sign_local)
                if stack_checkout:
                    self._connect_majiang.main_local_runfast_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()
            elif versionsName == "测试服麻将":
                stack_checkout = self.stack_card(self._test_main_path_name,self._version_majiang,self._version_sign_test)
                if stack_checkout:
                    self._connect_majiang.main_test_majiang_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()
            elif versionsName == "测试服跑胡子":
                stack_checkout = self.stack_card(self._test_main_path_name,self._version_paohuzi,self._version_sign_test)
                if stack_checkout:
                    self._connect_majiang.main_test_paohuzi_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()

            elif versionsName == "测试服跑得快":
                stack_checkout = self.stack_card(self._test_main_path_name,self._version_runfast,self._version_sign_test)
                if stack_checkout:
                    self._connect_majiang.main_test_runfast_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()


        elif int(portNumber) == self._changsha_version: #长沙版本
            if versionsName == "本地跑胡子":
                stack_checkout = self.stack_card(self._changsha_path_name, self._version_paohuzi,self._version_sign_local)
                if stack_checkout:
                    self._connect_majiang.changsha_local_paohuzi_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()
            elif versionsName == "本地麻将":
                stack_checkout = self.stack_card(self._changsha_path_name, self._version_majiang,self._version_sign_local)
                if stack_checkout:
                    self._connect_majiang.changsha_local_majiang_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()

            elif versionsName == "本地跑得快":
                stack_checkout = self.stack_card(self._changsha_path_name, self._version_runfast,self._version_sign_local)
                if stack_checkout:
                    self._connect_majiang.changsha_local_runfast_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()

            elif versionsName == "测试服麻将":
                stack_checkout = self.stack_card(self._test_changsha_path_name, self._version_majiang, self._version_sign_test)
                if stack_checkout:
                    self._connect_majiang.changsha_test_majiang_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()
            elif versionsName == "测试服跑胡子":
                stack_checkout = self.stack_card(self._test_changsha_path_name, self._version_paohuzi, self._version_sign_test)
                if stack_checkout:
                    self._connect_majiang.changsha_test_paohuzi_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()

            elif versionsName == "测试服跑得快":
                stack_checkout = self.stack_card(self._test_changsha_path_name, self._version_runfast, self._version_sign_test)
                if stack_checkout:
                    self._connect_majiang.changsha_test_runfast_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()


        elif int(portNumber) == self._changde_version:  # 常德版本
            if versionsName == "本地跑胡子":
                stack_checkout = self.stack_card(self._changde_path_name, self._version_paohuzi,self._version_sign_local)
                if stack_checkout:
                    self._connect_majiang.changde_local_paohuzi_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()

            elif versionsName == "本地麻将":
                stack_checkout = self.stack_card(self._changde_path_name, self._version_majiang,self._version_sign_local)
                if stack_checkout:
                    self._connect_majiang.changde_local_majiang_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()

            elif versionsName == "本地跑得快":
                stack_checkout = self.stack_card(self._changde_path_name, self._version_runfast,self._version_sign_local)
                if stack_checkout:
                    self._connect_majiang.changde_local_runfast_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()

            elif versionsName == "测试服麻将":
                stack_checkout = self.stack_card(self._test_changde_path_name, self._version_majiang, self._version_sign_test)
                if stack_checkout:
                    self._connect_majiang.changde_test_majiang_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()
            elif versionsName == "测试服跑胡子":
                stack_checkout = self.stack_card(self._test_changde_path_name, self._version_paohuzi, self._version_sign_test)
                if stack_checkout:
                    self._connect_majiang.changde_test_paohuzi_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()
            elif versionsName == "测试服跑得快":
                stack_checkout = self.stack_card(self._test_changde_path_name, self._version_runfast, self._version_sign_test)
                if stack_checkout:
                    self._connect_majiang.changde_test_runfast_restart_commd()
                    self.ui.resultText.setText("%s:%s service restart success " % (versionsName, portNumber))
                else:
                    self.show_message()


    def clearResult(self):
        self.ui.resultText.clear()
        self.ui.plainTextEdit.clear()

if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())