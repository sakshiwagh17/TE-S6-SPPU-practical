class SymptomChecker:
    def __init__(self):
        self.symptoms={
            "fever":False,
            "cough":False,
            "headache":False,
            "rash":False
        }
    
    def ask_symptoms(self):
        print("Please answer with 'yes' or 'no'.")
        for symptom in self.symptoms:
            response=input(f"Do you have {symptom}?").lower()
            if response == 'yes':
                self.symptoms[symptom]=True

    def diagnose(self):
        if self.symptoms["fever"] and self.symptoms["cough"]:
            print("You may have flu.")
        elif self.symptoms["fever"] and self.symptoms["headache"]:
            print("You may have a Meningitis.")
        elif self.symptoms["fever"] and self.symptoms["rash"]:
            print("You may have a Measles.")
        elif self.symptoms["headache"] and self.symptoms["fever"]:
            print("You may have a tension fever.")
        else:
            print("Its difficult to diagnose with the given symptoms. Please consult doctor.")
    
if __name__=="__main__":
    checker=SymptomChecker()
    checker.ask_symptoms()
    checker.diagnose()
