from typing import List

class JobSearch:
    _should_exclude_substrings = False
    _should_include_substrings = False
    _should_exclude_noPayRate = False
    _minimum_salary = -1
    _minimum_hourly = -1
    _radius = -1
    _job_title = ""
    _location = ""
    _URL = ""
    _domain = "https://www.indeed.com/jobs?q="
    _excluded_substrings: List[str] = []
    _included_substrings: List[str] = []


    def __init__(self, title="", location="", radius=-1):
        self.Set_JobTitle(title)
        self.Set_Location(location)
        self.Set_Radius(radius)

# GETTERS
    def Should_Exclude_Substrings(self):
        return self._should_exclude_substrings

    def Should_Include_Substrings(self):
        return self._should_include_substrings

    def Should_Exclude_NoPayRate(self):
        return self._should_exclude_noPayRate

    def Get_Minimum_Salary(self):
        return self._minimum_salary

    def Get_Minimum_Hourly(self):
        return self._minimum_hourly

    def Get_Radius(self):
        return self._radius

    def Get_JobTitle(self):
        return self._job_title

    def Get_Location(self):
        return self._location

    def Get_URL(self):
        return self._URL

    def Get_ExcludedSubstrings(self):
        return self._excluded_substrings

    def Get_IncludedSubstrings(self):
        return self._included_substrings

# SETTERS

    def Tick_ExcludeSubstrings(self):
        self._should_exclude_substrings = not self._should_exclude_substrings

    def Tick_IncludeSubstrings(self):
        self._should_include_substrings = not self._should_include_substrings

    def Tick_ExcludeNoPayRate(self):
        self._should_exclude_noPayRate = not self._should_exclude_noPayRate
        print(self._should_exclude_noPayRate)

    def Set_Salary(self, salary):
        if salary > 0:
            self._minimum_salary = salary
        else:
            print("Salary Wage is out of bounds, please enter a positive number")


    def Set_Hourly(self, hourly_wage):
        if hourly_wage > 0:
            self._minimum_hourly = hourly_wage
        else:
            print("Hourly Wage is out of bounds, please enter a positive number")

    def Set_Radius(self, radius):
        if radius >= 0:
            self._radius = radius
        else:
            print("Radius is out of bounds, please enter a positive number")  # put the error message in the GUI later
            radius = -1
        self.Update_URL()

    def Set_JobTitle(self, title):
        self._job_title = self.FormatToURI(title)
        self.Update_URL()

    def Set_Location(self, location):
        self._location = "&l=" + self.FormatToURI(location)
        self.Update_URL()

    def Update_URL(self):
        self._URL = self._domain + self._job_title + self._location
        if self._radius != -1:
            self._URL += "&radius=" + (str)(self._radius)


# Methods
    def FormatToURI(self,query):
        space = "+"
        comma = "%2C"
        result = ""
        for character in query:
            if character == " ":
                result += space
            elif character == ",":
                result += comma
            elif character.isalnum():
                result += character
            else:
                print("Unsupported Character in argument. please only use spaces, commas, and alphanumerics")

        return result