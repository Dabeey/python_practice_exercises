# Selenium Projects

This folder contains various automation projects using **Selenium WebDriver** and **BeautifulSoup** for web scraping and data automation tasks. Each project demonstrates different use cases of web automation, such as scraping real estate listings and automatically filling Google Forms.

## Project: Zillow Listings Scraper & Google Forms Automation

### Description:
This project automates the process of scraping real estate listings from a Zillow clone webpage and automatically filling in the collected data into a Google Form. The project uses **BeautifulSoup** for web scraping and **Selenium WebDriver** to automate form submissions.

### Technologies Used:
- **Selenium WebDriver** (for browser automation)
- **BeautifulSoup** (for web scraping)
- **Requests** (to fetch web content)
- **Python** (core language)
- **Google Forms** (target form for automation)

### Project Workflow:
1. **Web Scraping**:
   - Scrapes the property addresses, prices, and links from the Zillow clone website using BeautifulSoup.
   
2. **Form Automation**:
   - Automatically fills a Google Form with the scraped data (property addresses, prices, and links) using Selenium WebDriver.

### How to Run the Project:

1. **Install Required Libraries**:
   Install all required Python packages using `pip`:
   ```bash
   pip install selenium beautifulsoup4 requests
