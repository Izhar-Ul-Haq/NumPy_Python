contacts = {
    "fname" : "Izhar",
    "lname" : "Ul Haq",
}
print(contacts["lname"])
print(contacts.get("fname"))
print(contacts.get("name"))
contacts["name"] = "Izhar Ul Haq"
print(contacts["name"])
contacts["address"] = "Merdan Khel Karak, KPK"
print(contacts["address"])