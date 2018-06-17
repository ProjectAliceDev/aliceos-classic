import os

# Set this variable equal to the location of where your Ren'Py install is!
renpy = "/home/marquiskurt/Desktop/renpy-6.99.14.3-sdk/renpy.sh"

print("Running AliceOS in developer mode...")

try:
    os.system(renpy + " .")
except:
    print("Whoops, something went wrong.")
    print("Check your RENPY variable in run.py.")
