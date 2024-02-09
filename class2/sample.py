def validation_age(age):
    if age < 0:
        raise ValueError("Age cannot be less then 0")