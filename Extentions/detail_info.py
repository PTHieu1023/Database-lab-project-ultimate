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

product_format = """
Product ID: {product_id}

Title: {title}

Supplier: {supplier}

Price: {price}

Quantity: {quantity_in_stock}

Sold: {sold}

Feedback:
{feedback}
"""

order_format = """
Bill Id: {id}

Created time: {created_time}

Customer: {customer}

Saler: {saler}

Total pay: {total_pay}

Discount: {discount}

Customer paid: {customer_paid}

Refund: {refund}

Products:
{detail}
"""

product_feedback = """
**{customer} (cid:{customer_id}) 
    commented at {create_time}:
    - {comment}
    - Rate {rating} points
"""
def export_data(format_str, info_dict):
    return format_str.format(**info_dict)

bill_detail = """
-   Produc ID: {product_id}
    Title: {title}
    Supply by: {supplier}
    Quantity: {quantity}
    Price: {price}     
"""