import os

def bulid_all():
    print("Building GUI")
    os.system("pyuic6 -o ./UI/pop_up_staff.py -x ./UI/add_data_pop_up.ui")
    os.system("pyuic6 -o ./UI/form_ui.py -x ./UI/ultimate-design.ui")
    os.system("pyuic6 -o ./UI/customer_popup.py -x ./UI/add_customer.ui")
    print("Building completed!")

bulid_all()