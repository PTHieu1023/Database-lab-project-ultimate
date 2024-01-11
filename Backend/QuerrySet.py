#-----------------------------------------------------------------------------------------------------
#   Queries to get all records of entities (Order, Product, Customer, Staff)
#-----------------------------------------------------------------------------------------------------
GET_ALL_STAFF = """
SELECT 
    s.staff_id as "ID", CONCAT_WS(' ', s.first_name, s.last_name) as "NAME", 
    r.role as "ROLE", s.salary AS "SALARY" 
FROM 
    staff as s 
LEFT JOIN 
    staff_role as r ON s.role = r.staff_role_id;
"""

GET_ALL_CUSTOMER = """
SELECT 
    customer_id as "ID", 
    CONCAT_WS(\' \', first_name, last_name) as "NAME", 
    telephone as "TEL",
    address as "ADDRESS", 
    bonus_point as "POINT" 
FROM 
    customer;
"""

GET_ALL_PRODUCT = """
select 
    p.product_id as "Product ID",
    p.title as "Title",
    p.output_price as "Price",
    s.name as "Supplier",
    p.quantity_in_stock as "Quantity"
from
    product as p left join
    supplier as s on p.supplier = s.supplier_id
order by
    p.product_id asc
"""

GET_ALL_ORDER = """
SELECT
    *
FROM
    bill
"""

#-----------------------------------------------------------------------------------------------------
#   Queries to get detail info of an entity (Order, Product, Customer, Staff)
#-----------------------------------------------------------------------------------------------------
GET_DETAIL_STAFF_BY_ID = """
SELECT 
	s.staff_id, concat_ws(' ', s.first_name, s.last_name) as fname, s.dob, s.telephone,
    r.role, s.salary, s.email, s.address, s.start_working_date, s.working_type, 
    s.end_working_date
FROM 
    staff as s 
LEFT JOIN 
    staff_role as r ON r.staff_role_id = s.role
WHERE 
    s.staff_id = {id}
"""


GET_DETAIL_CUSTOMER_BY_ID = """
SELECT
    c.customer_id,
    CONCAT_WS(' ', c.first_name, c.last_name) AS full_name,
    c.telephone,
    c.email,
    c.address,
    c.bonus_point,
    COUNT(b.bill_id) AS order_count,
    COALESCE(SUM(b.total_pay), 0) AS total_purchased
FROM
    customer AS c
LEFT JOIN (
    SELECT
        bill.customer AS customer,
        bill.bill_id AS bill_id,
        SUM(bill_detail.price) AS total_pay
    FROM
        bill
    JOIN bill_detail ON bill.bill_id = bill_detail.bill_id
    GROUP BY bill.bill_id
) AS b ON b.customer = c.customer_id
WHERE 
    c.customer_id = {id}
GROUP BY
    c.customer_id
"""

GET_DETAIL_PRODUCT_BY_ID = """
select
    p.product_id,
    p.title,
    s.name as supplier,
    p.output_price as price,
    p.quantity_in_stock,
    sum(bd.quantity) as sold
from
    product as p
    left join supplier as s on p.supplier = s.supplier_id
    left join bill_detail as bd on p.product_id = bd.product_id
where
    p.product_id = {id}
group by
    p.product_id,
    s.name
"""

GET_DETAIL_ORDER_BY_ID = """
"""

#-----------------------------------------------------------------------------------------------------
#   Other necessary querries
#-----------------------------------------------------------------------------------------------------
GET_PRODUCT_FEEDBACK_BY_ID = """
select
  pf.*,
  concat_ws(' ', c.first_name, c.last_name) as customer
from
  product_feedback as pf
  left join customer as c on c.customer_id = pf.customer_id
where
  pf.product_id = {id}
order by
  pf.created_date asc
"""