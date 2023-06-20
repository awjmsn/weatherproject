#Final Draft of Program

#imports json and requests library
import json, requests

#defines function that takes data and validates it
def main(): 
  #captures user input and assigns it to a variable
  user_input = input("Enter a city or zip code: ") 
  
  base_url = "https://api.openweathermap.org/data/2.5/weather"
  appid = "914726094cca2a19513c24fa8da0169e"

  #concatinates the url with the user input and the api key
  
  url = f"{base_url}?q={user_input}&units=imperial&APPID={appid}"
  print ()

  #gets the json data from the webserver if connection isn't successful prints a message
  try:
    response = requests.get(url)
    unformated_data = response.json()
    print("Connection Successful\n")
  except:
    print("unable to connect, connection not successful")

  #Try and except block if user data is not valid 
  try: 
    temp = unformated_data["main"]["temp"]
    print(f"The current temperature in {user_input.title()} is: {temp}")
  except:
    print("Please Enter a Valid Input")
    main()


#a boolean variable to allow the while loop to run
active = True
print("Welcome to Alex's Weather Application")

while active:

  print("\nWould you like to search for your local weather?\n")
  #takes user input as a string on whether or not to search
  function_input = str(input("Yes or No: "))

  if function_input.lower() == "yes":
    main()
  elif function_input.lower() == "no":
    print("Thanks for searching")
    active = False
  else:
    print("Either yes or no please")