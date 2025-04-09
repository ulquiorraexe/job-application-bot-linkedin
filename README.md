# Job Application Bot for LinkedIn

This Python script automates the process of applying to jobs on LinkedIn by logging into your account, searching for Python Developer jobs in London, and saving them for later review.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ulquiorraexe/job-application-bot-linkedin.git
   cd job-application-bot-linkedin
   ```

2. **Install the required dependencies**:

   Ensure you have Python installed, then install the necessary packages by running:

   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**:

   - Go to [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/) and download the ChromeDriver that matches your version of Google Chrome.
   - Place the `chromedriver` executable in your project folder or provide the path in the script.

4. **Set Your LinkedIn Credentials**:

   Open the script `main.py` and set your LinkedIn login credentials by modifying the `mail_input.send_keys("")` and `password_input.send_keys("")` lines with your email and password:

   ```python
   mail_input.send_keys("your_email", Keys.TAB)
   password_input.send_keys("your_password", Keys.ENTER)
   ```

## Usage

1. After setting your LinkedIn credentials, run the bot by executing the following command:

   ```bash
   python main.py
   ```

2. The bot will:
   - Log in to your LinkedIn account.
   - Search for Python Developer jobs in London.
   - Click on each job listing and save it for later review.

3. The script will automatically interact with the page by filling in your credentials, navigating through job listings, and clicking the "Save" button for each job.

4. The bot will close the browser once all jobs are saved.

## Code Overview

### Script Flow:
1. **Login**: The bot logs into your LinkedIn account using your credentials.
2. **Job Search**: The bot navigates to the Python Developer jobs page for London.
3. **Save Jobs**: The bot clicks on each job listing and clicks the "Save" button for later application.

### Key Functions:
- **Login to LinkedIn**: The script automatically fills in the email and password fields and submits the login form.
- **Navigate and Save Jobs**: The bot searches for jobs and saves each listing by clicking the "Save" button.

## Notes
- **Rate Limiting**: Be cautious when using the bot. LinkedIn may flag or block accounts for automating job applications. Use it responsibly.
- **Customizing the Search**: You can change the job search URL in the script to search for different job titles, locations, or other filters.

## License
This project does not have a license.
