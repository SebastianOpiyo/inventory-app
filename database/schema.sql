-- Create tables
CREATE TABLE lab_items (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(255) NOT NULL,
    quantity NUMBER NOT NULL
);

CREATE TABLE users (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(255) NOT NULL
);

CREATE TABLE borrowed_items (
    id NUMBER PRIMARY KEY,
    user_id NUMBER NOT NULL,
    item_id NUMBER NOT NULL,
    date_borrowed DATE NOT NULL,
    date_to_return DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (item_id) REFERENCES lab_items(id)
);
