import sys
import maya.api.OpenMaya as OpenMaya
import maya.OpenMayaMPx as mpx
kCmdName = 'printSelection'
class PrintSeelctionCmd(mpx.MPxCommand):
    def __init__(self):
        mpx.MPxCommand.__init__(self)
        self.name = ''
    def parse_syntax(self,arg_list):
        parse = OpenMaya.MArgDatabase(self.syntax(),arg_list)
        if parse.isFlagSet('-n'):
            self.name = parse.flagArgumentString('-n',0)
    def doIt(self,arg_list):
        self.parse_syntax(arg_list)
        print('Hello %s' % self.name)
def command_creator():
    return mpx.asMPxPtr(PrintSeelctionCmd)
def new_syntx():
    syntx = OpenMaya.MSyntax()
    syntx. addFlag('-n','name',OpenMaya.MSyntax.kString)
def initializePlugin(mobject):
    fn_plugin = mpx.MFnPlugin(mobject)
    try:
        fn_plugin.registerCommand(
            kCmdName,
            command_creator,
            new_syntx
        )
    except:
        sys.stderr.write('Filed to register command'+kCmdName)
def uninitializePlugin(mobject):
    fn_plugin = mpx.MFnPlugin(mobject)
    try:
        fn_plugin.deregister(
            kCmdName
        )
    except:
        sys.stderr.write('Field to deregister command'+kCmdName)