import requests

def main():
    print("##teamcity[inspectionType id='id' name='name' category='Medium Severity' description='description']")
    print("##teamcity[inspection typeId='id' message='message 1' file='filename.c' line='1' SEVERITY='Medium Severity']")
    print("##teamcity[inspection typeId='id' message='message 2' file='filename.c' line='2' SEVERITY='Medium Severity']")
    print("##teamcity[inspection typeId='id' message='message 3' file='filename.c' line='3' SEVERITY='Medium Severity']")

if __name__ == "__main__":
    main()
