import pluggy
import os
import string
import random

hookimpl = pluggy.HookimplMarker("tox")

@hookimpl
def tox_addoption(parser):
   print("In local tox_addoption hook")
   os.environ['LOCAL_PLUGIN_ADDOPTION'] = 'local_addoption'
   parser.add_testenv_attribute(
       "randpwdenv",
       type="string",
       help="Environmental variable carrying the random password"
   )


@hookimpl
def tox_configure(config):
    print("In local tox_configure hook")
    for env in config.envconfigs:
        print("Env", env)
        envConf = config.envconfigs[env]
        for e in ['LOCAL_PLUGIN_' + x for x in ['ADDOPTION','GET_PYTHON_EXECUTABLE','RUNENVREPORT']]:
            envConf.passenv.add(e)
        envConf.setenv['LOCAL_PLUGIN_CONFIGURE'] = 'local_configure'
        if envConf.randpwdenv:
            pwd = ''.join(random.choice(string.ascii_letters) for _ in range(10))
            envConf.setenv[envConf.randpwdenv] = pwd

def gen_rand_pwd(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@hookimpl
def tox_get_python_executable(envconfig):
    print("In local tox_get_python_executable hook")
    os.environ['LOCAL_PLUGIN_GET_PYTHON_EXECUTABLE'] = 'local_get_python_executable'


@hookimpl
def tox_runenvreport(venv, action):
    print("In local tox_runenvreport")
    os.environ['LOCAL_PLUGIN_RUNENVREPORT'] = 'local_runenvreport'
