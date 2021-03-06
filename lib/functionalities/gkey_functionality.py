import subprocess
import inspect
import time
from lib.data_mappers import hotkey_type, config_reader
from lib.misc import logger, paths
from lib.uinput_keyboard import keyboard

log = logger.logger(__name__)


def execute_writing(string_to_write: str, device):
    keyboard.writeout(string_to_write,config_reader.read()['keyboard_mapping'],device)

def execute_hotkey(string_for_hotkey: str, device):
    keyboard.shortcut(string_for_hotkey, config_reader.read()['keyboard_mapping'], device)

def execute_release(device):
    keyboard.release(device)

def execute_command(command):
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def execute_config_swap(config):
    subprocess.call(["cp", paths.config_dir + "/" + config, paths.config_path])
    if paths.color != "":
        time.sleep(0.5)
        subprocess.call(["g910-led", "-fx", "breathing", "logo", paths.color, "0a"])

def resolve_config(key):


    config = config_reader.read()

    if key not in config.keys():
        log.info(key+" pressed, unbound in config, doing nothing!")
        return lambda _: None

    key_config : dict = config[key]
    command = key_config.get("hotkey_type","nothing")
    try:
        command = hotkey_type.type[command]
    except:
        raise Exception("hotkey_type: \""+command+"\" for key "+key+" not known! hotkey_types can only be: nothing, typeout, shortcut and run!")
    if command == 0:

        log.info(key+" pressed, typing out: "+repr(key_config["do"]))
        return lambda device: execute_writing(key_config["do"], device)
    if command == 1:
        log.info(key+" pressed, pressing: "+key_config["do"])
        return lambda device: execute_hotkey(key_config["do"], device)
    if command == 2:
        log.info(key+" pressed, running: "+key_config["do"])
        return lambda _: execute_command(key_config["do"])
    if command == 3:
        log.info(key + " pressed, swapping config to " + key_config["do"])
        return lambda _: execute_config_swap(key_config["do"])
    if command == -1:
        log.info(key+" pressed, doing nothing!")
        return lambda _: None



def release(device):
    execute_release(device)

def g1(device):
    resolve_config(inspect.stack()[0][3])(device)

def g2(device):
    resolve_config(inspect.stack()[0][3])(device)


def g3(device):
    resolve_config(inspect.stack()[0][3])(device)


def g4(device):
    resolve_config(inspect.stack()[0][3])(device)


def g5(device):
    resolve_config(inspect.stack()[0][3])(device)


def g6(device):
    resolve_config(inspect.stack()[0][3])(device)


def g7(device):
    resolve_config(inspect.stack()[0][3])(device)


def g8(device):
    resolve_config(inspect.stack()[0][3])(device)

def g9(device):
    resolve_config(inspect.stack()[0][3])(device)

def m1(device):
    resolve_config(inspect.stack()[0][3])(device)

def m2(device):
    resolve_config(inspect.stack()[0][3])(device)

def m3(device):
    resolve_config(inspect.stack()[0][3])(device)

def mr(device):
    resolve_config(inspect.stack()[0][3])(device)

