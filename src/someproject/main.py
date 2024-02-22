from teamcity.messages import TeamcityServiceMessages

def send_inspection_messages():
    # Send inspection type message
    TeamcityServiceMessages().message("inspectionType id='id' name='name' category='Medium Severity' description='description'")

    # Send inspection messages
    TeamcityServiceMessages().message("inspection typeId='id' message='message 1' file='filename.c' line='1' SEVERITY='Medium Severity'")
    TeamcityServiceMessages().message("inspection typeId='id' message='message 2' file='filename.c' line='2' SEVERITY='Medium Severity'")
    TeamcityServiceMessages().message("inspection typeId='id' message='message 3' file='filename.c' line='3' SEVERITY='Medium Severity'")

if __name__ == "__main__":
    send_inspection_messages()
