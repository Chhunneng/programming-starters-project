const { exec } = require('child_process');

function visitGitHubProfile(username, times) {
    const profileUrl = `https://github.com/${username}`;
    for (let i = 0; i < times; i++) {
        exec(`start ${profileUrl}`);
    }
}

// Replace 'YOUR_USERNAME' with your actual GitHub username
const username = 'SUDEEP-M-SHETTY';
const visitCount = 50; // Change this number to the desired visit count
visitGitHubProfile(username, visitCount);
