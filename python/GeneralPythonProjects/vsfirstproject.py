def checklist(lst, message,call):
    while True:
        if call in lst:
            break
        else:
            call = input(f"please enter a valid {message}!\n").lower().strip()
    return call


family_info = {
    "ido" : {
        "height" : "165cm", 
        "weight" : "46kg",
        "hair color" : "dark brown"
        }
    ,
    "amit" : {
        "height" : "149cm", 
        "weight" : "37kg",
        "hair color" : "brown"
        }
    ,
    "merav" : {
        "height" : "167cm", 
        "weight" : "56kg",
        "hair color" : "blonde"
        }
    ,
    "tal" : {
        "height" : "182cm", 
        "weight" : "84kg",
        "hair color" : "black"
        }
    ,
    "oz" : {
        "height" : "117cm", 
        "weight" : '22.5kg',
        "hair color" : "dark brown"
        }
    ,
    "atay" : {
        "height" : '96.5cm', 
        "weight" : '17kg',
        "hair color" : "dark brown"
        }
    }


while True:
    name = input("Who's information in the family would you like to see?(type 'q' to quit)\n").lower().strip()
    if name == 'q':
        quit()
    name = checklist(family_info,'name',name)
    info_type = input(f"What info would you like to see about {name.capitalize()}?(height, weight, hair color or type 'all' for all the information)\n").lower().strip()
    info_type = checklist(['height', 'weight', 'hair color','all'], 'input', info_type)
    if info_type == 'all':
        final_message = "".join(str(family_info[name]).strip("{}").split("'"))
    else:
        final_message = family_info[name][info_type]
    print(final_message)
    print("-----------------------------------------------------")