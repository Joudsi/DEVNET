class Database:
    """
    represents the interface to the data (model).
    Uses statically-defined data to keep things simple for now.
    """
    def __init__(self, path):
        """
        constructor to initialize the data attributed as a dictionary
        where the account numbee is the key and the value is another
        directory with keys "paid" and "due"
        """

        #  -----  static assignment
        # self.data = {
        #     "ACCT100":{"paid": 60, "due": 100}, # balance = 40
        #     "ACCT200": {"paid": 70, "due": 60}, # balance = -10
        #     "ACCT300": {"paid": 60, "due": 0}, # balance = 0
        # }


        # open the specified database file for reading and perform loading

        with open(path, "r") as handle:
            # JSON
            import json
            self.data = json.load(handle)

            # #YAML
            # import yaml
            # self.data = yaml.safe_load(handle)

            # import xmltodict
            # self.data = xmltodict.parse(handle.read())["root"]
            # print(self.data)



    def balance(self, acct_id):
        """
         takes the acct_id as a parameter and gets the value from the data
        """
        acct = self.data.get(acct_id)
        if acct:
            bal = float(acct["due"]) - float(acct["paid"])
            return f"${bal:.2f}"
        return None

    def owes_money(self, acct_id):
        """
        not yet implemented
        """
        acct = self.data.get(acct_id)
        if acct:
            return int(acct["due"]) - int(acct["paid"]) > 0
        return None

