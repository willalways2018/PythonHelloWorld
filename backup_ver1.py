import os
import time

# 1.需要备份的文件与目录将被指定在一个列表中
# 例如在windows下：
source = ['"C:\\Downloads"', 'c:\\Code']
# 又例如在 Mac OS x 与 Linux 下
# source = ['/Users/swa/notes']
# 在这里要注意到我们必须在字符串中使用双引号
# 用以括起其中包含空格的名称

# 2.备份文件必须存储在一个主备份目录中
# 例如在 windows 下：
target_dir = 'E:\\backup'
# 又例如在Mac OS x 和 Linux 下：
# target_dir = '/User/swa/backup'
# 要记得将这里的目录地址修改至你将使用的路径

# 3.备份文件将打包压缩成 zip 文件
# 4.zip压缩文件的文件名由当前日期与时间构成。
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # 创建目录

# 5.我们使用zip名称将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
ll_ret = os.system(zip_command)
if ll_ret == 0:

    print('Successful backup to', target)
else:
    print('Backup FAILED')