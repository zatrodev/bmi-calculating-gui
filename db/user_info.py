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
            return "Underweight", "Individuals who are underweight may need to increase their calorie intake to gain weight. A balanced diet that includes a variety of nutrient-dense foods such as whole grains, lean proteins, healthy fats, and fruits and vegetables is recommended. Additionally, drink plenty of fluids and minimize having foods that are high in fat, salt, and sugar by having it less often in small amounts. Lastly, resistance training and physical activity can help to build muscle mass."
        elif self.bmi >= 18.5 and self.bmi < 25:
            return "Normal", "For individuals in the normal weight range, a balanced diet that includes a variety of nutrient-dense foods is recommended. This should include whole grains, lean proteins, healthy fats, and fruits and vegetables. It is also important to maintain an appropriate calorie balance by consuming only the amount of calories needed to maintain a healthy weight, and engaging in regular physical activity."
        elif self.bmi >= 25 and self.bmi < 30:
            return "Overweight", "For individuals who are overweight, the primary goal should be to achieve a modest weight loss of 5-10% of body weight. This can be achieved by reducing calorie intake and increasing physical activity. A diet that is low in saturated fats and added sugars, and rich in fruits, vegetables, and whole grains is recommended."
        elif self.bmi >= 30:
            return "Obese", "Eat a variety of foods where you aim to consume a wide range of different foods, including fruits, vegetables, whole grains, lean proteins, and low-fat dairy products. Also, pay attention to how much you are eating and try to avoid overeating. Using smaller plates, bowls, and cups can help to control portion sizes. Try to avoid foods and drinks that are high in sugar, salt, and fat, as they can contribute to weight gain. Examples include sugary drinks, fried foods, and snacks like chips and chocolate bars. Choose healthier cooking methods such as baking, grilling, steaming, or boiling instead of frying to reduce the use of oils. Additionally, drink plenty of water and limit sugary or alcoholic drinks.      ."
