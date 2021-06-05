// var reporter = require('cucumber-html-reporter');

// var options = {
//         theme: 'bootstrap',
//         jsonFile: 'reports/report.json',
//         output: 'features/reports/cucumber_report.html',
//         reportSuiteAsScenarios: true,
//         scenarioTimestamp: true,
//         launchReport: true,
//         metadata: {
//             "App Version":"0.3.2",
//             "Test Environment": "STAGING",
//             "Browser": "Chrome  54.0.2840.98",
//             "Platform": "Windows 10",
//             "Parallel": "Scenarios",
//             "Executed": "Remote"
//         }
//     };

//     reporter.generate(options);


const report = require('multiple-cucumber-html-reporter');

report.generate({
	jsonDir: 'reports',
	reportPath: 'reports/cucumber/report.html',
	metadata:{
        browser: {
            name: 'chrome',
            version: '89.0.4389.114'
        },
        device: 'Local test machine',
        platform: {
            name: 'osx',
            version: '10.15.7'
        }
    },
    customData: {
        title: 'Run info',
        data: [
            {label: 'Project', value: 'Actable AI'},
            {label: 'Release', value: '0.0.1'},
            {label: 'Cycle', value: 'B11221.34321'},
            {label: 'Execution Start Time', value: 'Apr 12th 2021, 02:31 PM EST'},
            {label: 'Execution End Time', value: 'Apr 12th 2021, 02:56 PM EST'}
        ]
    }
});
