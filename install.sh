#pkg update && pkg upgrade
#pkg install python
cd
cd ../usr/etc                                                              
echo "alias cli-cal='cd && cd cli-calculator && python cli-calculator.py'" >> bash.bashrc
cd 
cd cli-calculator
chmod 777 cli-calculator.py
echo "Terminal shortcut successfully created"
echo "Next time just type: "
echo "cli-cal"
echo