class UserInfo:
    def __init__(self, name, age, lrn, weight, height):
        self.name = name
        self.age = age
        self.lrn = lrn
        self.weight = weight
        self.height = height
        self.bmi = weight / pow(height, 2)
        self.classification, self.nutritional_guide = self.classify_bmi()

    def classify_bmi(self):
        if self.bmi < 18.5:
            return "Underweight", "Increase intake of healthy fats, proteins, and carbohydrates."
        elif self.bmi >= 18.5 and self.bmi < 25:
            return "Normal", "Maintain a healthy, balanced diet."
        elif self.bmi >= 25 and self.bmi < 30:
            return "Overweight", "Reduce intake of unhealthy fats and sugars, increase intake of fiber-rich foods."
        elif self.bmi >= 30:
            return "Obese", "Consult a healthcare professional for personalized dietary and exercise advice."
