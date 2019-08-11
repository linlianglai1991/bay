from Libs.tools import BaseHttp


class LoginClass(BaseHttp):

    cookies = {
        'PHPSESSID': ''
    }

    # 封装公共业务模块
    def loginApi(self):
        # 登录接口
        lgn_path = '/index.php?ctl=user&act=dologin'
        # 登录数据
        lgn_data = {
            'email': 'rocky111',
            'user_pwd': 'aVFnSE9mYmtGSld1bWJISVZSRHFDWmpaRURwR2JRYnV0Vk1HY29McE9jY25RZGlZYkslMjV1NjVCOSUyNXU3RUY0QUJDRDEyMzQlMjV1OEY2RiUyNXU0RUY2',
            'ajax': 1,
        }
        lgn_result = self.sendHttp(path=lgn_path, data=lgn_data)
        phpid = lgn_result.cookies['PHPSESSID']
        self.cookies['PHPSESSID'] = phpid
        return lgn_result

