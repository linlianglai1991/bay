import unittest
from Libs.business import LoginClass
from Po.MyP2P.BankCard import BankCardApi

class TestBankCard(unittest.TestCase):

    def test001(self):
        # 实例化绑定银行卡类
        bc = BankCardApi()
        result = bc.bindBankCard()
        # 该接口返回的数据是json格式，所以通过转换最后会变成字典
        json_result = result.json().get('info', '找不到这个数据')
        # 校验字典中包含的值是否存在
        self.assertEqual('保存成功', json_result)

    def test002(self):
        # 实例化绑定银行卡类
        bc = BankCardApi()
        result = bc.bindBankCard()
        json_result = result.json().get('info', '找不到这个数据')
        self.assertEqual('该银行卡已存在', json_result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
