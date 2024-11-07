line_format_zh = {
    'default': {
        'address_line1': "CountryProvince/StateCityDistrict",
        'address_line2': "Street",
        'address_line3': "Bldg/Complex Name, Block/Tower/Phase Floor/Rm/Suite",
        'address_line4': "Postal Code",
    },
    "CHN": {
        'address_line1': "Postal Code",
        'address_line2': "Country/Pronvince/State/City/District",
        'address_line3': "Street",
        'address_line4': "Bldg/Complex Name, Block/Tower/Phase Floor/Rm/Suite",
    },

}


line_format_en = {
    "default": {
        'address_line1': "Room/Suite Number,Floor,Block/Tower/Phase",
        'address_line2': "Building / Complex Name",
        'address_line3': "Road/Street",
        'address_line4': "District, City,Postal Code,Country/Territory",
    }
}

rule = {
    "default": ("English address should be inputted in upper and lower case."
        "Users can choose to input the address in fuor in abbreviation."
        "But in any case where abbreviation is used, the standardized Address Abbreviation (Appendix 2) should be followed. "
        "Comma is needed only in between address in 1st line and 4th line. "
        "No punctuation is needed at the end of the line. The English address should follow the following input sequence :"
        "Room/ Suite Number "
        "Floor "
        "Block/ Tower/ Phase "
        "Building Name "
        "Complex Name "
        "Road/ Street "
        "District "
        "CityCountry/Territory "
    ),
    "CHN": (
        "Chinese address should be input according to the following order: "
        "- Country "
        "- Province/State "
        "- City "
        "- District "
        "- Street "
        "- Building/Complex Name "
        "- Block/Tower/Phase "
        "- Room / Suite Number "
        "- Floor "
        "1st line: Country Province/State City District"
        "2nd line: Street"
        "3rd line: Bldg/Complex Name Block/Tower/Phase Floor/Rm/Suite"
        "4th line: Postal Code"
    )
}
