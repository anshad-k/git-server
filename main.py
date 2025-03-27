#!/bin/python3

from dotenv import load_dotenv
import os
import requests

BASE_URL = "https://hackattic.com/challenges/hosting_git"

def main():
	load_dotenv()
	access_token = os.getenv("ACCESS_TOKEN")	
	problem_url = f"{BASE_URL}/problem?access_token={access_token}"	
	response = requests.get(problem_url).json()
	print(response)
	

if __name__ == "__main__":
	main()
