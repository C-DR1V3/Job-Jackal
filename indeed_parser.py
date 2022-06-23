class Indeed_Parser:

    def Check_Wage_Type(raw_wage):
        if("year" in raw_wage):
            return "salary"
        else:
            return "hourly"

    def Extract_Minimum_Wage(raw_wage):
        return int(''.join(filter(str.isalnum,raw_wage.split()[0])))

