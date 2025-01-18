#Copyright Bail&Will&loaf0808
#SkyNet:install_requires 依赖安装脚本

PIP_REQUIRE = ['playsound','edge-tts']
##LINUX_REQUIRE = ['python3-gst-1.0']

import sys,os

def isinst():
    if sys.argv[-1] == '-p':
        return True
    else:
        return False
"""def linux_install():
    res = os.system('sudo apt install '+' '.join(LINUX_REQUIRE))
    if res != 0:
        res = os.system('sudo yum install '+' '.join(LINUX_REQUIRE))
        if res != 0:
            raise OSError('Linux依赖安装失败')"""
def pip_install():
    if '--termux' in sys.argv:  # 判定为termux安装，使用自编的playsound
        PIP_REQUIRE.remove('playsound')
    os.system(f'{sys.executable} -m pip install -i https://mirrors.aliyun.com/pypi/simple/ --break-system-packages --upgrade pip wheel setuptools')    # 更新pip组件，防止安装失败
    os.system(f'{sys.executable} -m pip install -i https://mirrors.aliyun.com/pypi/simple/ --break-system-packages '+' '.join(PIP_REQUIRE))
def main():
##    if os.name == 'posix' and not isinst():
##        linux_install()
    pip_install()
    return 0

if __name__ == '__main__':
    sys.exit(main())

