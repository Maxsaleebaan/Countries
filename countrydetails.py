from countryinfo import CountryInfo
import flagpy as fp

Name = input("Enter a country name : ")

country = CountryInfo(Name)

print("Capital is : ",country.capital())
print("Currency is : ",country.currencies())
print("Language is : ",country.languages())
print("Borders are  : ",country.borders()) 
print("Others names : ", country.alt_spellings())
print("Population : ", f"{country.population():,d}")  # f-string says to format the number and use commas as thousand separators.
print("Provinces : ", len(country.provinces()))
print("Provinces : ", country.provinces())
print("Country Area : ", f"{country.area():,d}")
fp.display(Name)