import paramiko
from readData import read_data

class Connection:
    def __init__(self):
        self.read_data = read_data()

    def connect_server_majiang(self,commd,output_flag=False,connect_local=True):
        """连接麻将本地服务器"""

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if connect_local:
                ssh.connect(hostname = self.read_data["majiang_local_server_host"],
                            port = self.read_data["majiang_local_server_port"],
                            username = self.read_data["majiang_local_server_user"],
                            password = self.read_data["majiang_local_server_password"])
            else:
                ssh.connect(hostname=self.read_data["majiang_test_server_host"],
                            port=self.read_data["majiang_test_server_port"],
                            username=self.read_data["majiang_test_server_user"],
                            password=self.read_data["majiang_test_server_password"])

        except:
            return
        if output_flag:
            stdin, stdout, stderr = ssh.exec_command(commd)
            return stdout.readlines()
        else:
            stdin, stdout, stderr = ssh.exec_command(commd)

        ssh.close()
        return "cmd: %s"%commd

    # ------------主版本--------------------------
    def main_local_paohuzi_restart_commd(self):
        """本地跑胡子启动"""
        _commd = self.read_data["Main_local_paohuzi"]
        self.connect_server_majiang(commd=_commd)
    def main_test_paohuzi_restart_commd(self):
        """测试服跑胡子启动"""
        _commd = self.read_data["Main_test_paohuzi"]
        self.connect_server_majiang(commd=_commd,connect_local=False)


    def main_local_majiang_restart_commd(self):
        """本地麻将启动"""
        _commd = self.read_data["Main_local_majiang"]
        self.connect_server_majiang(commd=_commd)
    def main_test_majiang_restart_commd(self):
        """测试服麻将启动"""
        _commd = self.read_data["Main_test_majiang"]
        self.connect_server_majiang(commd=_commd,connect_local=False)


    def main_local_runfast_restart_commd(self):
        """本地跑得快启动"""
        _commd = self.read_data["Main_local_runfast"]
        self.connect_server_majiang(commd=_commd)
    def main_test_runfast_restart_commd(self):
        """测试服跑得快启动"""
        _commd = self.read_data["Main_test_runfast"]
        self.connect_server_majiang(commd=_commd,connect_local=False)

    #------------长沙--------------------------
    def changsha_local_paohuzi_restart_commd(self):
        """本地跑胡子启动"""
        _commd = self.read_data["changsha_local_paohuzi"]
        self.connect_server_majiang(commd=_commd)

    def changsha_test_paohuzi_restart_commd(self):
        """测试服跑胡子启动"""
        _commd = self.read_data["changsha_test_paohuzi"]
        self.connect_server_majiang(commd=_commd,connect_local=False)

    def changsha_local_majiang_restart_commd(self):
        """本地麻将启动"""
        _commd = self.read_data["changsha_local_majiang"]
        self.connect_server_majiang(commd=_commd)

    def changsha_test_majiang_restart_commd(self):
        """测试服麻将启动"""
        _commd = self.read_data["changsha_test_majiang"]
        self.connect_server_majiang(commd=_commd,connect_local=False)

    def changsha_local_runfast_restart_commd(self):
        """本地跑得快启动"""
        _commd = self.read_data["changsha_local_runfast"]
        self.connect_server_majiang(commd=_commd)
    def changsha_test_runfast_restart_commd(self):
        """测试服跑得快启动"""
        _commd = self.read_data["changsha_test_runfast"]
        self.connect_server_majiang(commd=_commd,connect_local=False)

    # ------------常德--------------------------
    def changde_local_paohuzi_restart_commd(self):
        """本地跑胡子启动"""
        _commd = self.read_data["changde_local_paohuzi"]
        self.connect_server_majiang(commd=_commd)
    def changde_test_paohuzi_restart_commd(self):
        """测试服跑胡子启动"""
        _commd = self.read_data["changde_test_paohuzi"]
        self.connect_server_majiang(commd=_commd,connect_local=False)

    def changde_local_majiang_restart_commd(self):
        """本地麻将启动"""
        _commd = self.read_data["changde_local_majiang"]
        self.connect_server_majiang(commd=_commd)
    def changde_test_majiang_restart_commd(self):
        """测试服麻将启动"""
        _commd = self.read_data["changde_test_majiang"]
        self.connect_server_majiang(commd=_commd,connect_local=False)

    def changde_local_runfast_restart_commd(self):
        """本地跑得快启动"""
        _commd = self.read_data["changde_local_runfast"]
        self.connect_server_majiang(commd=_commd)
    def changde_test_runfast_restart_commd(self):
        """测试服跑得快启动"""
        _commd = self.read_data["changde_test_runfast"]
        self.connect_server_majiang(commd=_commd,connect_local=False)



    def card_write_file(self,version,write_data,version_name,version_sign):
        if version_sign == "local":
            write_file = "cd /home/caocheng/{2}/{0}/; echo '{1}' >testcard.json".format(version_name,write_data,version)
            print(write_file)
            self.connect_server_majiang(commd=write_file)
        elif version_sign == "test":
            write_file = "cd /mydata/user_02/{2}/{0}/; echo '{1}' >testcard.json".format(version_name, write_data,version)
            print(write_file)
            self.connect_server_majiang(commd=write_file,connect_local=False)








#
# if __name__ == "__main__":
#     c = Connection()
#                                                                                                                                                                                                         '''