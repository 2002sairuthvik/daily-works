# import requests
# import lxml
# from bs4 import BeautifulSoup
# import smtplib

# MY_EMAIL = "munugotisairuthvik@gmail.com"
# MY_PASSWORD = "use app password "

# URL = "https://www.amazon.in/Wellspire-Pot-Stainless-Pressure-CUSTOMISED/dp/B0BDS1PKFW/ref=sr_1_2_sspa?crid=11WER5KLO5PL1&dib=eyJ2IjoiMSJ9.RZ-Tal92wUMSme9E8BuI0V84CtQG1fSYcqnmTn41jWOgdfTM1XkhdXuVwB2vjAhsu5NroFXhfxvtgUmc5_h7PdfAtdDVwGb9UVpPDVJ_lz0Qi2B6XG_K5Xet9vp2IdYFan0pSka-Ag2T65_laqc2SZst4NiX1lW28hzDDMLD8Bp2O5DW6Mv2OK-W--u99ZwuiF6STVZ7EQfEwg_qaJoEjpPUWPWz_oY1wDIl-tw3jgH__bsKNVU1bObNInMTotyBq7gow-NrflJ6YL5XONY7wnw8TEjZ3hLv8xqXrcIIgHM.WGoH0vpQrPGrzSKagYRHwN8CiSOWjPDmAn_aV7IHSac&dib_tag=se&keywords=instant+pot&qid=1713168837&sprefix=instant+po%2Caps%2C230&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,te;q=0.7"
# }

# response = requests.get(URL, headers=header)

# soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

# price_element = soup.find(class_="a-offscreen")
# if price_element:
#     price = price_element.get_text()
#     # Proceed with further processing
#     price_without_currency = price.split("₹")[1]
#     price_without_commas = price_without_currency.replace(',', '')
#     price_as_float = float(price_without_commas)
#     # Now you can use price_as_float or any other variable as needed
# else:
#     # Handle case when price element is not found
#     print("Price element not found")



# title = soup.find(id="productTitle").get_text().strip()
# print(title)

# BUY_PRICE = 6000

# if price_as_float < BUY_PRICE:
#     message = f"{title} is now {price}"

#     with smtplib.SMTP("", port=587) as connection:
#         connection.starttls()
#         result = connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
#         )