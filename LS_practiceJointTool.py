#creates a set of three proxies first, then finalize it to a set of three joints
import maya.cmds as cmds
def proxJnt_UI():
    UIWindow = "proxJnt_Window"
    UITitle = "Proxy-based Joint Creator"
    UISize = (400, 400)
    #close old window if opened
    if cmds.window(UIWindow, exists = True):
        cmds.deleteUI(UIWindow, window = True)
    
    #create new window
    cmds.window(UIWindow, title=UITitle, widthHeight=UISize)
    
    cmds.columnLayout(adjustableColumn = True)
    cmds.text(UITitle)
    cmds.separator(height=20)
    
    jnt_1_name = cmds.textFieldGrp(label="Joint 1 Name:")
    jnt_2_name = cmds.textFieldGrp(label="Joint 2 Name:")
    jnt_3_name = cmds.textFieldGrp(label="Joint 3 Name:")
    
    #define make proxy function
    def make_proxies(*args):
        global PROXY
    #retreive proxy/joint names
        proxName_1 = cmds.textFieldGrp(jnt_1_name, q=True, text=True)
        proxName_2 = cmds.textFieldGrp(jnt_2_name, q=True, text=True)
        proxName_3 = cmds.textFieldGrp(jnt_3_name, q=True, text=True)
    #create proxies of 3 joints
        prox_1 = cmds.spaceLocator(n=proxName_1+"_proxy")[0]
        prox_2 = cmds.spaceLocator(n=proxName_2+"_proxy")[0]
        prox_3 = cmds.spaceLocator(n=proxName_3+"_proxy")[0]
    #move proxies to default locations
        cmds.setAttr(prox_1+'.translate', 0, 1, 0)
        cmds.setAttr(prox_2+'.translate', 2, 1, 0)
        cmds.setAttr(prox_3+'.translate', 4, 1, 0)
    #define global variable containing the proxies for the next step
        PROXY = [prox_1, prox_2, prox_3]
      
    #make button
    cmds.button(label="Create Proxies", command=make_proxies)
    
    #define make joint function
    def make_jnts(*args):
        global PROXY
        cmds.select(cl=True)
        for everyItem in PROXY:
            loc = cmds.xform(everyItem, q=True, t=True)
            jnt = cmds.joint(n= everyItem.replace('_proxy','_jnt'), position=loc)
        cmds.delete(PROXY)
   
    #make button
    cmds.button(label="Create Joints", command=make_jnts)
    
    #display new window
    cmds.showWindow()

proxJnt_UI()