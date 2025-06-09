--task1
create table product_inventory (
    product_id number primary key,
    product_name varchar2(50),
    stock number not null check (stock >= 0),
    price number(12, 2) not null
);

create table returns (
    return_id number primary key,
    product_id number references product_inventory(product_id),
    return_date date default sysdate,
    reason varchar2(255),
    quantity number not null check (quantity > 0)
);

insert into product_inventory (product_id, product_name, stock, price)
values (1, 'Laptop', 10, 1000.00);

insert into product_inventory (product_id, product_name, stock, price)
values (2, 'Smartphone', 20, 500.00);

insert into product_inventory (product_id, product_name, stock, price)
values (3, 'Tablet', 15, 300.00);


declare
    product_id number := 1;
    return_quantity number := 3;
    restocking_fee number := 0.05;
    net_quantity number;

    net_quantity := return_quantity - (return_quantity * restocking_fee);

    insert into returns (return_id, product_id, return_date, reason, quantity)
    values (
        (select nvl(max(return_id), 0) + 1 from returns),
        product_id,
        sysdate,
        'Customer dissatisfaction',
        return_quantity
    );
    savepoint stock_update;

    update product_inventory
    set stock = stock + net_quantity
    where product_id = product_id;

    commit;

exception
    when others then
        rollback to stock_update;
        raise;
end;

--Task2
create table bank_accounts (
    account_id number primary key,
    balance number(12, 2) not null check (balance >= 0),
    account_type varchar2(20)
);

create table transactions (
    transaction_id number primary key,
    account_id number references bank_accounts(account_id),
    type varchar2(10) check (type in ('debit', 'credit')),
    amount number(12, 2) not null,
    transaction_date date default sysdate
);

insert into bank_accounts (account_id, balance, account_type)
values (1, 1000, 'savings');

insert into bank_accounts (account_id, balance, account_type)
values (2, 500, 'current');

declare
    sender_id number := 1;
    receiver_id number := 2;
    transfer_amount number := 200;
    transaction_fee number := transfer_amount * 0.02;
    transaction_id_counter number := 1;
begin
    update bank_accounts set balance = balance - (transfer_amount + transaction_fee)
    where account_id = sender_id;
    savepoint balance_updated;

    insert into transactions (transaction_id, account_id, type, amount, transaction_date)
    values (transaction_id_counter, sender_id, 'debit', transfer_amount + transaction_fee, sysdate);
    transaction_id_counter := transaction_id_counter + 1;

    update bank_accounts
    set balance = balance + transfer_amount
    where account_id = receiver_id;

    insert into transactions (transaction_id, account_id, type, amount, transaction_date)
    values (transaction_id_counter, receiver_id, 'credit', transfer_amount, sysdate);
    transaction_id_counter := transaction_id_counter + 1;

    commit;

exception
    when others then
        rollback to balance_updated;
        raise;
end;



-- task3

create table customers (
    customer_id number primary key,
    name varchar2(50)
);

create table loyalty_program (
    customer_id number references customers(customer_id),
    points_earned number default 0,
    points_redeemed number default 0
);

insert into customers (customer_id, name) values (1, 'Alice');
insert into customers (customer_id, name) values (2, 'Bob');

insert into loyalty_program (customer_id, points_earned, points_redeemed) values (1, 0, 0);
insert into loyalty_program (customer_id, points_earned, points_redeemed) values (2, 0, 0);

declare
    customer_id number := 1;
    purchase_amount number := 600;
    points_awarded number;

    if purchase_amount > 500 then
        points_awarded := purchase_amount * 1.5;
    else
        points_awarded := purchase_amount;
    end if;

    update loyalty_program
    set points_earned = points_earned + points_awarded
    where customer_id = customer_id;
    savepoint points_updated;

    if points_awarded < 0 then
        raise_application_error(-20001, 'Error in points calculation.');
    end if;

    commit;

exception
    when others then
        rollback to points_updated;
        raise;
end;



