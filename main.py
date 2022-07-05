import json
from flask import Flask
app = Flask(__name__)

JSON_URL = "cv.json"

class CVData:
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

class PersonalData(CVData):
    def __str__(self) -> str:
        return 'Personal CV: ' + super().__dict__.__str__()

class ExperienceData(CVData):
    def __str__(self) -> str:
        return 'Experience on CV: ' + super().__dict__.__str__()

class EducationData(CVData):
    def __str__(self) -> str:
        return 'Education: ' + super().__dict__.__str__()

class CVRepo:

    def __init__(self, json_file_path: str) -> None:
        file_content = self.__read_file(json_file_path)
        self.__personal = PersonalData(file_content['personal'])
        self.__experience = ExperienceData(file_content['experience'])
        self.__education = EducationData(file_content['education'])
    
    def __read_file(self, json_file_path: str):
        '''
        Reads the file and returns the dict associated to the json file
        '''
        with open(json_file_path, 'r') as file:
            file_content = file.read()
            return json.loads(file_content)
    
    def get_personal(self):
        return self.__personal
    
    def get_experience(self):
        return self.__experience

    def get_education(self):
        return self.__education

class CVService:
    def __init__(self, repo: CVRepo) -> None:
        self.__repo = repo
    
    def get_personal(self):
        return self.__repo.get_personal()

    def get_experience(self):
        return self.__repo.get_experience()

    def get_education(self):
        return self.__repo.get_education()

def dependency_inj():
    repo = CVRepo(json_file_path=JSON_URL)
    service = CVService(repo=repo)
    return service

service = dependency_inj()

@app.route("/personal")
def personal():
    global service
    return service.get_personal().__dict__

@app.route("/experience")
def experience():
    global service
    return service.get_experience().__dict__

@app.route("/education")
def education():
    global service
    return service.get_education().__dict__
    

@app.cli.command("print")
def print_stdout():
    global service
    print(str(service.get_personal()))
    print(str(service.get_education()))
    print(str(service.get_education()))