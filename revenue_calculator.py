
def youtube_calculator(views:int, country:str)-> float:

    if views < 0:
        raise ValueError('Not valid view count') 

    if views <= 10000:
        raise ValueError('Not Eligible')

    rates = {
        "USA": 2.5,
        "UK": 2.0,
        "UAE": 1.5,
        "other": 0.5
    }

    rate = rates.get(country.lower(), rates["other"])
    revenue = views * rate

    return revenue

