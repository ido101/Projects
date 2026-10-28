import ctypes

message_box = ctypes.windll.user32.MessageBoxW

result = message_box(None, "Hello, User!\nMake a Choice", "Message Box", 0x40 | 0x1)  

if result == 1:
    print("User clicked OK.")
else:
    print("User closed the message box without making a choice.")