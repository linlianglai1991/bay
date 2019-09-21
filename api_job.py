import requests

# 获取登录接口
login_url = 'http://127.0.0.1/admin.php?m=mgr/admin.chklogin&ajax=1'
# 登录数据
lgn_data = {
    'username': 'admin',
    'password': 'admin',
}

# 发送登录请求
r = requests.post(url=login_url, data=lgn_data)

# 获取登录请求中的Phpid值
data = r.headers
cookie_data = data.get('Set-Cookie')
phpid_list = cookie_data.split(';')
phpid1 = phpid_list[0]
phpid2 = phpid_list[1].split(', ')[1]


# 获取添加教师接口
add_teacher_url = 'http://127.0.0.1/admin.php?m=mgr/member2.saveMemberInfo&id='

headers = {
    'Cookie': '{}'.format(phpid2)
}

# 添加教师数据
teacher_data = {
    'username':'13700803107',
    'realname':'nidaye009',
    'password':'123456',
    'sex':'0',
    'roleid':'5',
    'orid1':'25',
    'email':'test@qq.com',
    'phone':'13755555155',
    'location_p':'北京市',
    'location_c':'市辖区',
    'location_a':'东城区',
    'address':'你家',
    'introduce':'我是你爸爸',
    'type':'1',

}

# 发送添加教师请求
r2 = requests.post(url=add_teacher_url, data=teacher_data, headers=headers)

print(r2.text)