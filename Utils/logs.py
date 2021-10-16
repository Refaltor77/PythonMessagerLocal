from time import *
import simple_chalk
c = simple_chalk.newChalk()


def info(msg):
    msg = c.blueBright.bold('[') + c.blueBright.bold(strftime("%H:%M:%S", gmtime())) + c.blueBright.bold(
        ']') + c.green.bold(
        ' [INFO] ') + c.gray.bold(msg)
    return msg


def warn(msg):
    msg = c.blueBright.bold('[') + c.blueBright.bold(strftime("%H:%M:%S", gmtime())) + c.blueBright.bold(
        ']') + c.yellow.bold(
        ' [WARN] ') + c.yellow.bold(msg)
    return msg


def critical(msg):
    msg = c.blueBright.bold('[') + c.blueBright.bold(strftime("%H:%M:%S", gmtime())) + c.blueBright.bold(
        ']') + c.red.bold(
        ' [CRITICAL] ') + c.red.bold(msg)
    return msg


def error(msg):
    msg = c.blueBright.bold('[') + c.blueBright.bold(strftime("%H:%M:%S", gmtime())) + c.blueBright.bold(
        ']') + c.red.bold(
        ' [ERROR] ') + c.yellow.bold(msg)
    return msg


def debug(msg):
    msg = c.blueBright.bold('[') + c.blueBright.bold(strftime("%H:%M:%S", gmtime())) + c.blueBright.bold(
        ']') + c.blue.bold(
        ' [DEBUG] ') + c.yellow.bold(msg)
    return msg
