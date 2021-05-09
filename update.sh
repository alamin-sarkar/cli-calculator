cd
rm -rf cli-calculator
echo
echo
echo "Downloading new version"
git clone https://github.com/alamin-sarkar/cli-calculator.git
cd cli-calculator
chmod 777 install.sh
sh install.sh
echo
echo "Update Complete"
echo "Please Restart Termux app"
