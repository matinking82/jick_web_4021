def sendVerificationEmail(email:str, token:str):
    subject = 'Verify your email'
    message = f'Hi there, click on the link to verify your email: http://localhost:8000/user/activate/{token}'
    
    print(message)