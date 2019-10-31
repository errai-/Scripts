import smtplib, imaplib

def mailer(subject,body):
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    
    print "Sending: ", body
    send_from = 'YOURDUMMYEMAIL@gmail.com'
    password = 'YOURDUMMYPASSWD'
    recipient = "YOURREALEMAIL@gmail.com"
    headers = ["From: " + send_from,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/plain"]
    headers = "\r\n".join(headers)
    
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(send_from, password)
    
    session.sendmail(send_from, recipient, headers + "\r\n\r\n" + body)
    session.quit()

def writer(total,nonvara,counter):
    with open("status2.txt", 'w') as fp:
        fp.write("{} {} {}".format(total,nonvara,counter))
        fp.close()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    total = 81
    nonvara = 0
    counter = 0
    with open('status2.txt') as fp:
        line = fp.readline()
        ilist = [int(i) for i in line.split()]
        if len(ilist)==3:
            total = ilist[0]
            nonvara = ilist[1]
            counter = ilist[2]+1
        else:
            print bcolors.WARNING + "Unable to read status file!" + bcolors.ENDC
        fp.close()
    
    with open('study.html') as fp:
        line = fp.readline()
        ecount = 0
        ocount = 0
        remember = []
        vremember = []
        listening = False
        varattu = False
        apt = ''
        stat = ''
        while line:
            line = line.strip()
            if line!="":
                if not listening:
                    if '<tr class="odd ' in line:
                        ocount += 1
                        listening = True
                        varattu = ("Varattu" in line)
                    elif '<tr class="even ' in line:
                        ecount += 1
                        listening = True
                        varattu = ("Varattu" in line)
                else:
                    if '/tr>' in line:
                        listening = False
                        if varattu:
                            vremember.append(apt)
                        else:
                            remember.append("{} {}".format(apt,stat))
                        varattu = False
                        apt = ''
                        stat = ''
                    elif '<td class="views-field views-field-views-conditional-2" >' in line:
                        line = fp.readline()
                        line = line.strip()
                        varattu = ("Varattu" in line)
                        if not varattu:
                            stat = line.split()[0]
                    elif '<td class="views-field views-field-nid active" >' in line:
                        line = fp.readline()
                        line = line.strip()
                        apt = line.split()[0]
            line = fp.readline()
        newtot = ecount+ocount
        if newtot==0:
            print "Somehow, the list is empty!"
            mailer("Page is empty","It is empty! :(")
        else:
            newnonvara = len(remember)
            if counter>0 and counter%720==0:
                indicator = counter/720
                print "Sending status report!"
                info = "Report: status OK, {} apartments, {} other than Varattu.\nNot varattu: ".format(newtot,newnonvara)\
                     +', '.join(str(x) for x in remember)+"\nVarattu: "+', '.join(str(x) for x in vremember)
                mailer("Status report",info)
                if indicator==4:
                    counter = 0

            formaggio = bcolors.WARNING
            if newtot!=total:
                formaggio = bcolors.OKBLUE
                info = "Number of apartments changed from {} to {}!".format(total,newtot)
                mailer("Apartment removed from list",info)
                info = "Report: status OK, {} apartments, {} other than Varattu.\nNot varattu: ".format(newtot,newnonvara)\
                     +', '.join(str(x) for x in remember)+"\nVarattu: "+', '.join(str(x) for x in vremember)
                mailer("Changes report",info)
            elif newnonvara!=nonvara:
                formaggio = bcolors.OKGREEN
                info = "Number of un-reserved apartments changed from {} to {}! See apts: ".format(nonvara,newnonvara)+', '.join(str(x) for x in remember)
                mailer("Non-Varattu observed",info)
                info = "Report: status OK, {} apartments, {} other than Varattu.\nNot varattu: ".format(newtot,newnonvara)\
                     +', '.join(str(x) for x in remember)+"\nVarattu: "+', '.join(str(x) for x in vremember)
                mailer("Changes report",info)
            writer(newtot,newnonvara,counter)
            print formaggio + "{}/{} not varattu ({} even, {} odd)!".format(newnonvara,ecount+ocount,ecount,ocount) + bcolors.ENDC
        fp.close()

if __name__ == "__main__":
    main()

