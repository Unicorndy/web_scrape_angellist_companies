#clean data before inserting to mongoDb


def clean(result):
    """Return clean data.

    :param result: The datum to be clean
    :return: datum: clean datum
    """

    datum = {}
    name = result.find("div", {"class": "name"}).get_text()
    pitch = result.find("div", {"class": "pitch"}).get_text()
    website = result.find("div", {"class": "website"}).get_text()
    stage = result.find("div", {"class": "stage"}).get_text()

    for value in result.find_all("div", {"class": "joined"}):
        joined = (value.find("div", {"class": "value"}).get_text())

    for value in result.find_all("div", {"class": "location"}):
        location = (value.find("div", {"class": "value"}).get_text())

    for value in result.find_all("div", {"class": "market"}):
        market = (value.find("div", {"class": "value"}).get_text())

    for value in result.find_all("div", {"class": "column company_size hidden_column"}):
        company_size = (value.find("div", {"class": "value"}).get_text())

    for value in result.find_all("div", {"class": "column hidden_column raised"}):
        raised = (value.find("div", {"class": "value"}).get_text())


    def clean_string(var):
        var = str(var)
        var = var.rstrip()  # removes whitespace at both ends
        var = var.replace('\n', '')
        return var


    def clean_dollarsign(var):
        if "-" in var:
            return None
        var = var.rstrip()
        var = var.replace('\n', '')
        var = var.replace('$', '')
        if '£' in var:
            print(name, ":", var)
        var = var.replace('£','')
        if '€' in var:
            print(name, ":", var)
        var = var.replace('€','')
        var = var.replace(',', '')
        var = float(var)
        return var


    datum['name'] = clean_string(name)
    datum['pitch'] = clean_string(pitch)
    datum['website'] = clean_string(website)
    datum['stage'] = clean_string(stage)
    datum['joined'] = clean_string(joined)
    datum['location'] = clean_string(location)
    datum['market'] = clean_string(market)
    datum['company_size'] = clean_string(company_size)
    datum['raised'] = clean_dollarsign(raised)

    return datum