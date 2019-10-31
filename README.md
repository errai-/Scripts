# Scripts
Dumb (but working) bash scripts for real-life problems

Monitoring the Helsinki "Hitas" page (applied succesfully):
- The Hitas system in Helsinki area is very odd and should probably be removed
- It offers affordable('ish) apartments, which are dealed through a lottery
- If and when some of the "lottery winners" do not accept to buy the apartment, it is released on the web page
- There is no information or schedule for the "free release" schedule of the apartments
- The only existing information is that on the Hitas web page
- Hence, I decided to create a simple script for monitoring the web page
- It downloads the whole web page html every 30s, and checks for changes in the apartment information
- The script sends a status report email every 6 hours (to check that it's still alive)
- If there is a change, the script sends a report immediately into my main email
- The user should insert a dummy gmail account into genhelp2.py for sending the emails
- The login info is hard-coded, so this should not be a "real account"
- The "recipent" email should be the real account, the user wants to monitor

The files freedom2.sh, genhelp2.py and the metadata file status2.txt are needed to use this program.
When the user has entered valid login details, the program can be run with 'bash freedom2.sh'
