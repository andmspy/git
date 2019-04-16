import win32ui


# 打开文件windows窗口
dlg = win32ui.CreateFileDialog(1)
dlg.SetOFNInitialDir("C:")
flag = dlg.DoModal()
print(flag)

print(dlg.GetPathName())


# 另存为windows窗口
def save():
    dlg = win32ui.CreateFileDialog(0)
    dlg.SetOFNInitialDir("C:")
    flag = dlg.DoModal()
    file_name = dlg.GetPathName()
    return file_name


with open(save(), 'w')as f:
    f.write('haha')



