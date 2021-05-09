#pkg update && pkg upgrade
#pkg install python
cd
cd ../usr/etc                                                              
echo "alias cli-cal='cd && cd cli-calculator && python cli-calculator.py'" >> bash.bashrc
echo "alias calcu='cd && cd cli-calculator && python cli-calculator.py'" >> bash.bashrc
echo "alias ccal='cd && cd cli-calculator && python cli-calculator.py'" >> bash.bashrc
cd 
cd cli-calculator
chmod 777 cli-calculator.py
echo "Terminal shortcut successfully created"
echo "If not working this shortcut, Please Restart termux app"
echo "Next time just type: "
echo "cli-cal or ccal or calcu"
echo