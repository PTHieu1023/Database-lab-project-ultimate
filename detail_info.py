staff_detail_format = """
Staff: {staff_id}

Name: {fname}

DOB: {dob}

Tel: {telephone}

Email: {email}

Address: {address}

Role: {role}

Start working date: {start_working_date}

Salary: {salary}

Working type: {working_type}

"""

customer_format = """
Customer: {customer_id}

Name: {full_name}

Tel: {telephone}

Email: {email}

Address: {address}

Bonus point: {bonus_point}

Number of orders: {order_count}

Purchased: {total_purchased}

"""

def export_data(format_str, info_dict):
    return format_str.format(**info_dict)
