import re

import PySimpleGUI as sg
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg


def captchaBuilder(resp):
    with open("captcha.svg", "w") as f:
        f.write(re.sub('(<path d=)(.*?)(fill="none"/>)', "", resp["captcha"]))

    drawing = svg2rlg("captcha.svg")
    renderPM.drawToFile(drawing, "captcha.png", fmt="PNG")

    layout = [
        [sg.Image("captcha.png")],
        [sg.Text("Enter Captcha Below")],
        [sg.Input(key="inp")],
        [sg.Button("Submit", bind_return_key=True)],
    ]

    window = sg.Window("Enter Captcha", layout, finalize=True)
    window.TKroot.focus_force()  # focus on window
    window.Element("inp").SetFocus()  # focus on field
    event, values = window.read()
    window.close()
    return values["inp"]
