def validation_age(age):
    if age < 0:
        raise ValueError("Age can'nt be less then 0")