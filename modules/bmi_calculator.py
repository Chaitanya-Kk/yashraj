def calculate_bmi(weight, height):
    """Calculates BMI using weight (kg) and height (cm)."""
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive values.")
    
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 2)
