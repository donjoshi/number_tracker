from phonenumbers import carrier
import phonenumbers

from test import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")

print("\nThe phone number is :" + number)

print("\nThe country is : ")
print(geocoder.description_for_number(ch_number, "en"))


service_number = phonenumbers.parse(number, "RO")
print("\nThe service provider is : ")
print(carrier.name_for_number(service_number, "en"))
