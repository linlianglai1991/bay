from Libs.business import LoginClass


class BankCardApi(LoginClass):

    # 绑定银行卡业务
    def bindBankCard(self):

        # 调用登录
        self.loginApi()

        # 绑定数据接口的path
        bind_path = '/member.php?ctl=uc_money&act=savebank'

        # 绑定数据接口的数据
        bind_data = {
            'real_name': 'rocky',
            'bank_id': '1',
            'otherbank': '',
            'region_lv1': '1',
            'region_lv2': '2',
            'region_lv3': '52',
            'region_lv4': '500',
            'bankzone': '建设银行五和支行',
            'bankcard': '6223 0066 2346 6664 4325',
            'reBankcard': '6223 0066 2346 6664 4325'
        }
        # 发送请求
        result = self.sendHttp(path=bind_path, data=bind_data, cookies=self.cookies)
        return result