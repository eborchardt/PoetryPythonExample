import requests

def main():
    exampleVariable = "asdfasdf"
    print(f"##teamcity[setParameter name='someParameter' value='{exampleVariable}']")

if __name__ == "__main__":
    main()
