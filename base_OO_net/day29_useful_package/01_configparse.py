"""configparse 仅了解
处理配置文件，用的较少
"""

# 生成配置文件
# import configparser
# config = configparser.ConfigParser()  # 实例化了一个config对象
# config["DEFAULT"] = {'ServerAliveInterval': '45',  # config[组名] = {键值对}
#                       'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11':'yes'
#                      }
# config['bitbucket.org'] = {'User':'hg'}
# config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
# with open('example.ini', 'w') as configfile:  # 写入文件
#    config.write(configfile)

# 从配置文件中查找
# import configparser
#
# config = configparser.ConfigParser()

#---------------------------查找文件内容,基于字典的形式
# print(config.sections())        #  []
# config.read('example.ini')
# print(config.sections())    # 打印所有组名（除了default）    #   ['bitbucket.org', 'topsecret.server.com']
# print('bytebong.com' in config) # False  # 组名是否存在
# print('bitbucket.org' in config) # True
# print(config['bitbucket.org']["user"])  # hg  # 通过字典访问数据
# print(config['DEFAULT']['Compression']) #yes
# print(config['topsecret.server.com']['ForwardX11'])  #no
# print(config['bitbucket.org'])          #<Section: bitbucket.org>
# for key in config['bitbucket.org']:     # 注意,有default会默认default的键  # 无论通过那个组名访问，都能访问到default组名下的数据
#     print(config['bitbucket.org'][key])
# print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
# print(config.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对
# print(config.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的value

# 增删改
import configparser

config = configparser.ConfigParser()

config.read('example.ini') # 读文件

config.add_section('yuan') # 增加一个组名

config.remove_section('bitbucket.org')  # 删除组名
config.remove_option('topsecret.server.com',"forwardx11")  # 删除一个键名


config.set('topsecret.server.com','k1','11111')  # 新增键值对
config.set('yuan','k2','22222')

config.write(open('new2.ini', "w"))  # 写入文件