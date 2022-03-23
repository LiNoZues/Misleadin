# -- coding: utf-8 --
# @Time : 2020/11/19 16:32
# @Author : 怃
# @Email : chenzhe12320@163.com
# @File : ldap3.py
# @Project : for_github


from ldap3 import Server, Connection, SUBTREE, ALL


#  登录查询
def ldap3_login(username, password):
    # 登录配置
    host = 'zzinfo.tzt.cn'
    port = 389
    admin_username = 'uid=root,cn=users,dc=zztzt,dc=cn'
    admin_password = 'zztzt2019xxxx!'
    conn_search = 'dc=zztzt,dc=com'

    # 建立配置连接
    server = Server(host=host, port=port, use_ssl=False, get_info=ALL)
    server_connection = Connection(server, admin_username, admin_password, auto_bind=True)
    # 连上bind获取值 必须
    server_connection.bind()
    #  查找 username DN数据
    #  验证用户名
    try:
        result = server_connection.search('dc=zztzt,dc=cn', '(&(objectClass=inetOrgPerson)(uid={}))'.format(username),
                                          search_scope=SUBTREE)
    except:
        return False
    if result:
        dn = server_connection.response[0]['dn']
        # 验证密码
        try:
            server_connection1 = Connection(server, user=dn, password=password, auto_bind=True)
            server_connection1.bind()
        except:
            return False
        else:
            if server_connection1.result["description"] == "success":
                return True
            else:
                return False
    else:
        return False
