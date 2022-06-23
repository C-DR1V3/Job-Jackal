import requests
import os
from bs4 import BeautifulSoup
from openpyxl import Workbook
from job_search import JobSearch
from spreadsheet import SpreadSheet
from indeed_parser import Indeed_Parser

class Indeed_Scraper:

    def __init__(self, title="", location="", radius=-1,):
        self.search = JobSearch(title, location, radius)
        # self.result_sheet = SpreadSheet(os.environ["USERPROFILE"]+"\\Desktop\\jobsearch.xlsx")
        self.parser = Indeed_Parser

    def pull_indeed_into_spreadsheet(self):
        print(self.search.Get_URL())
        page = requests.get(self.search.Get_URL())
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="mosaic-provider-jobcards")
        job_elements = results.find_all("div", class_="job_seen_beacon")

        # self.search.Tick_ExlcludeNoPayRate()
        self.search.Set_Hourly(19)

        i = 1
        for element in job_elements:
            i += 1
            post_is_elligible = False

            salary_text = self.Determine_Posting_Salary(element)

            post_is_elligible = self.Salary_Is_Elligible(post_is_elligible, salary_text)



            if post_is_elligible:
                title_element = element.find("h2", class_="jobTitle")
                company_element = element.find("span", class_="companyName")
                location_element = element.find("div", class_="companyLocation")
                posting_url = "https://indeed.com"+(title_element.find("a", class_="jcs-JobTitle").get("href"))

                self.result_sheet.PopulateNewRow(i,title_element.text,company_element.text,
                                                 location_element.text, salary_text, posting_url)

                print(title_element.text)
                print(company_element.text)
                print(location_element.text)
                print(posting_url)
                print(salary_text)
                print("---------------------"*5)

            self.result_sheet.ApplyAutomaticColumnWidth()
            self.result_sheet.Save_Workbook()

    def Salary_Is_Elligible(self, post_is_elligible, salary_text):
        if salary_text != "Not Listed":
            wage_type = self.parser.Check_Wage_Type(salary_text)
            min_pay = self.parser.Extract_Minimum_Wage(salary_text)

            if (wage_type == "salary") & (self.search.Get_Minimum_Salary() != -1):
                if self.Wage_Is_Within_Range(min_pay, self.search.Get_Minimum_Salary()):
                    post_is_elligible = True
            elif (wage_type == "hourly") & (self.search.Get_Minimum_Hourly() != -1):
                if self.Wage_Is_Within_Range(min_pay, self.search.Get_Minimum_Hourly()):
                    post_is_elligible = True
        else:
            if self.Should_Exclude_Wagless_Posts():
                post_is_elligible = False
            else:
                post_is_elligible = True
        return post_is_elligible

    def Determine_Posting_Salary(self, element):
        if self.Wage_Exists(element):
            salary_text = element.find("div", class_="metadata salary-snippet-container").text
        else:
            salary_text = "Not Listed"
        return salary_text

    def Wage_Exists(self, element):
        return element.find("div", class_="metadata salary-snippet-container")

    def Should_Exclude_Wagless_Posts(self):
        return self.search.Should_Exclude_NoPayRate()

    def Wage_Is_Within_Range(self, wage, target):
        return wage >= target

if __name__ == "__main__":
    scraper = Indeed_Scraper("technical support", "Beaverton Oregon", 3)
    scraper.pull_indeed_into_spreadsheet()
