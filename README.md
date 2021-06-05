python3 -m venv .venv
source .venv/bin/activate
pipenv install behave
pipenv install selenium
pipenv install nose
pipenv install behave2cucumber
# Run: 
behave --tags=login,someOtherTag
# or 
behave features/featureFile.feature
# You can use the followimng commandline options to generate a test report > 
npm i multiple-cucumber-html-reporter
behave -f json -o report.json

# Then convert the behave json to cucumber format
python3 -m behave2cucumber -i report.json -o reports/cucumber_report.json

# Run the cucumber reports generator
node generate