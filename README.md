This project consist on the simplest blockchain program, whose goal is to serve as a baseline for future blockchain projects. 

It is based on the NeuralNine youtube tutorial that can be reached with the link: https://m.youtube.com/watch?v=pYasYyjByKI 

Thanks Neural NineNine for sharing this interesting content.


How to use a virtual environment:
1)  Creation    >> python -m venv venv  
2)  Activation  >> .\venv\Scripts\Activate    
    #Powershell: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
3)  Turn off    >> deactivate

Don't upload it to Github, use the requirements.txt:
1)  Creation    >> pip freeze > requirements.txt
2)  Use         >> pip install -r requirements.txt
3)  Write the folder "venv/" in the ".gitignore"

Run the Code:
1)  >> python main.py

Name & Email Setting:
1)  Name        >> git config --global user.name "Alonso García"
2)  Email       >> git config --global user.email "alonso.dev@gmail.com"
3)  Check-in    >> git config --global --list
