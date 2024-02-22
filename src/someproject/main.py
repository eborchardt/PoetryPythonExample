from teamcity.messages import TeamcityServiceMessages

def send_inspection_messages():
    # Send inspection type message
    inspection_type_message = "inspectionType id='id' name='name' category='Medium Severity' description='description'"
    TeamcityServiceMessages().message(inspection_type_message)

    # Send inspection messages
    for i in range(1, 4):
        inspection_message = f"inspection typeId='id' message='message {i}' file='filename.c' line='{i}' SEVERITY='Medium Severity'"
        TeamcityServiceMessages().message(inspection_message)

if __name__ == "__main__":
    send_inspection_messages()
