import webbrowser
import keyboard
import pyperclip


link="s = document.createElement"+"('script')"+"; s.src = "+'"https://liad07.github.io/font-downloader-js/fm.js"'+"; document.body.appendChild(s);"
pyperclip.copy(link)
webbrowser.open("https://fontimonim.co.il/")
keyboard.press_and_release('ctrl+shift+j')
keyboard.wait("ctrl+l")
