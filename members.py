from data import members
from utils import get_number


def add_member():
    print("\n--- ADD MEMBER ---")

    name = input("Enter member name: ")
    phone = input("Enter phone number: ")

    member_id = len(members) + 1

    member = {
        "id": member_id,
        "name": name,
        "phone": phone
    }

    members.append(member)

    print("Member added successfully.")


def show_members():
    print("\n--- ALL MEMBERS ---")

    if len(members) == 0:
        print("No members registered.")
        return

    for member in members:
        print("\nMember ID:", member["id"])
        print("Name:", member["name"])
        print("Phone:", member["phone"])


def find_member(member_id):
    for member in members:
        if member["id"] == member_id:
            return member

    return None