Set serveroutput on;
DECLARE  
    message VARCHAR2(20) := 'Hello World';
BEGIN 
    DBMS_OUTPUT.PUT_LINE(message);
END;
/
