import phonenumbers
import carrier
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+919832471912")
print("\n Phnone Number Location : ",geocoder.description_for_number(phone_number1,"en"))
print(carrier.name_for_number(phone_number1, "en"))