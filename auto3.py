import pyperclip
import time
inp=input()
str="""PrimeFaces.ab({s:"j_id_5x",f:"code",p:"j_id_5x",u:"codeeditorpanel"});\n
await new Promise(r => setTimeout(r, 1000));
document.getElementById('txtCode').innerHTML='\\n"""
while(inp!='S'):
 inp=inp.replace('\\','\\\\')
 inp=inp.replace('\'','\\\'')
 str+=inp
 str+="\\n"
 inp=input()
str+="""\\n';\nawait new Promise(r => setTimeout(r, 1000));\nPrimeFaces.ab({s:"j_id_b8",f:"code",p:"txtCode langs customtcpanel",u:"progresspanel srmsg"});"""
pyperclip.copy(str)

