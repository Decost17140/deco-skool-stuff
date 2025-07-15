print("โปรแกรมสอบถามการทําบัตรเครดิต")
cred = int(input("กรอกรายได้ของคุณ:"))
if cred <= 30000:
    print("คุณไม่สารถทำบัตรได้")
elif cred >= 40000 and cred <= 89999:
    print("คุณมีสิทธิทำบัตรเงิน")
    if cred >= 70000 and cred <= 99999:
        print("คุณมีสิทธิทำบัตรทอง")
elif cred >= 70000 and cred <= 99999:
    print("คุณมีสิทธิทำบัตรทอง")
else:
    print("คุณมีสิทธิทำบัตร Platinum")