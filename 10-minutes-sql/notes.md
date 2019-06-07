
Database A container (usually a file or set of files) to store organized data.


Database software is actually called the Database Management System (or DBMS). The database is the container created and manipulated via the DBMS. A database might be a file stored on a hard drive, but it might not.


A table is a structured file that can store data of a specific type. A table might contain a list of customers, a product catalog, or any other list of information. Table A structured list of data of a specific type.


Tables have characteristics and properties that define how data is stored in them. These include information about what data may be stored, how it is broken up, how individual pieces of information are named, and much more.


Tables have characteristics and properties that define how data is stored in them. These include information about what data may be stored, how it is broken up, how individual pieces of information are named, and much more. This set of information that describes a table is known as a schema, and schema are used to describe specific tables within a database, as well as entire databases


Tables are made up of columns. A column contains a particular piece of information within a table.


Each column in a database has an associated datatype. A datatype defines what type of data the column can contain.


Datatype A type of allowed data. Every table column has an associated datatype that restricts (or allows) specific data in that column.


Data in a table is stored in rows; each record saved is stored in its own row.


The number of rows in the table is the number of records in it. Row A record in a table.


Primary Key A column (or set of columns) whose values uniquely identify every row in a table.


SQL (pronounced as the letters S-Q-L or as sequel) is an abbreviation for Structured Query Language. SQL is a language designed specifically for communicating with databases.


Unlike other languages (spoken languages like English, or programming languages like Java or Visual Basic), SQL is made up of very few words. This is deliberate. SQL is designed to do one thing and do it well—provide you with a simple and efficient way to read and write data from a database.


When you store information in your filing cabinet you don't just toss it in a drawer. Rather, you create files within the filing cabinet, and then you file related data in specific files.


The key here is that the data stored in the table is one type of data or one list. You would never store a list of customers and a list of orders in the same database table.


Keyword A reserved word that is part of the SQL language. Never name a table or column using a keyword


The SQL statement that you'll probably use most frequently is the SELECT statement. Its purpose is to retrieve information from one or more tables.


To use SELECT to retrieve table data you must, at a minimum, specify two pieces of information—what you want to select, and from where you want to select it.


Use of White Space All extra white space within a SQL statement is ignored when that statement is processed. SQL statements can be specified on one long line or broken up over many lines. Most SQL developers find that breaking up statements over multiple lines makes them easier to read and debug.


Multiple SQL statements must be separated by semicolons (the ; character). Most DBMSs do not require that a semicolon be specified after single statements.


SQL Statement and Case It is important to note that SQL statements are case-insensitive, so SELECT is the same as select, which is the same as Select.


Take Care with Commas When selecting multiple columns be sure to specify a comma between each column name, but not after the last column name. Doing so will generate an error.


SQL statements typically return raw, unformatted data. Data formatting is a presentation issue, not a retrieval issue. Therefore, presentation (for example, displaying the above price values as currency amounts with the correct number of decimal places) is typically specified in the application that displays the data.


Using Wildcards As a rule, you are better off not using the * wildcard unless you really do need every column in the table. Even though use of wildcards may save you the time and effort needed to list the desired columns explicitly, retrieving unnecessary columns usually slows down the performance of your retrieval and your application.


Clause SQL statements are made up of clauses, some required and some optional. A clause usually consists of a keyword and supplied data. An example of this is the SELECT statement's FROM clause, which you saw in the last lesson.


To explicitly sort data retrieved using a SELECT statement, the ORDER BY clause is used. ORDER BY takes the name of one or more columns by which to sort the output.


Position of ORDER BY Clause When specifying an ORDER BY clause, be sure that it is the last clause in your SELECT statement.


Sorting by Nonselected Columns More often than not, the columns used in an ORDER BY clause will be ones that were selected for display. However, this is actually not required, and it is perfectly legal to sort data by a column that is not retrieved.


To sort by multiple columns, simply specify the column names separated by commas (just as you do when you are selecting multiple columns).


In addition to being able to specify sort order using column names, ORDER BY also supports ordering specified by relative column position. The best way to understand this is to look at an example: SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY 2,


Instead of specifying column names, the relative positions of selected columns in the SELECT list are specified. ORDER BY 2 means sort by the second column in the SELECT list, the prod_price column. ORDER BY 2, 3 means sort by prod_price and then by prod_name.


To sort by descending order, the keyword DESC must be specified.


To sort by descending order, the keyword DESC must be specified. The following example sorts the products by price in descending order (most expensive first): SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY prod_price DESC;


Retrieving just the data you want involves specifying search criteria, also known as a filter condition. Within a SELECT statement, data is filtered by specifying


Retrieving just the data you want involves specifying search criteria, also known as a filter condition. Within a SELECT statement, data is filtered by specifying search criteria in the WHERE clause. The WHERE clause is specified right after the table name (the FROM clause)


SELECT prod_name, prod_price
FROM Products
WHERE prod_price = 3.49;


This next statement retrieves all products costing $10 or less (although the result will be the same as in the previous example because there are no items with a price of exactly $10): SELECT prod_name, prod_price
FROM Products
WHERE prod_price <= 10;


When to Use Quotes If you look closely at the conditions used in the above WHERE clauses, you will notice that some values are enclosed within single quotes, and others are not. The single quotes are used to delimit a string. If you are comparing a value against a column that is a string datatype, the delimiting quotes are required. Quotes are not used to delimit values used with numeric columns.


check for a range of values, you can use the BETWEEN operator. Its syntax is a little different from other WHERE clause operators because it requires two values: the beginning and end of the range.


SELECT prod_name, prod_price
FROM Products
WHERE prod_price BETWEEN 5 AND 10;


The SELECT statement has a special WHERE clause that can be used to check for columns with NULL values—the IS NULL clause. The syntax looks like this: SELECT prod_name
FROM Products
WHERE prod_price IS NULL; This statement returns a list of all products that have no price (an empty prod_price field, not a price of 0),


The Vendors table, however, does contain columns with NULL values—the vend_state column will contain NULL if there is no state (as would be the case with non-U.S. addresses): SELECT vend_id
FROM Vendors
WHERE vend_state


The Vendors table, however, does contain columns with NULL values—the vend_state column will contain NULL if there is no state (as would be the case with non-U.S. addresses): SELECT vend_id


The Vendors table, however, does contain columns with NULL values—the vend_state column will contain NULL if there is no state (as would be the case with non-U.S. addresses): SELECT vend_id
FROM Vendors
WHERE vend_state IS NULL;


Operator A special keyword used to join or change clauses within a WHERE clause. Also known as logical operators.


To filter by more than one column, you use the AND operator to append conditions to your WHERE clause. The following code demonstrates this: SELECT prod_id, prod_price, prod_name
FROM Products
WHERE vend_id = 'DLL01' AND prod_price


To filter by more than one column, you use the AND operator to append conditions to your WHERE clause. The following code demonstrates this: SELECT prod_id, prod_price, prod_name
FROM Products
WHERE vend_id = 'DLL01' AND prod_price <= 4;


The OR operator is exactly the opposite of AND. The OR operator instructs the database management system software to retrieve rows that match either condition.


The OR operator is exactly the opposite of AND. The OR operator instructs the database management system software to retrieve rows that match either condition. In fact, most of the better DBMSs will not even evaluate the second condition in an OR WHERE clause if the first condition has already been met.


SQL (like most languages) processes AND operators before OR operators. When SQL sees the above WHERE clause, it reads any products costing $10 or more made by vendor BRS01, and any products made by vendor DLL01 regardless of price. In other words, because AND ranks higher in the order of evaluation, the wrong operators were joined together.


SQL (like most languages) processes AND operators before OR operators. When SQL sees the above WHERE clause, it reads any products costing $10 or more made by vendor BRS01, and any products made by vendor DLL01 regardless of price. In other words, because AND ranks higher in the order of evaluation, the wrong operators were joined together. The solution to this problem is to use parentheses to explicitly group related operators. Take a look at the following SELECT statement and output: SELECT prod_name, prod_price
FROM Products
WHERE (vend_id = 'DLL01' OR vend_id = 'BRS01')
    AND prod_price >= 10;


As parentheses have a higher order of evaluation than either AND or OR operators


The IN operator is used to specify a range of conditions, any of which can be matched. IN takes a comma-delimited list of valid values, all enclosed within parentheses. The following example demonstrates this: SELECT prod_name, prod_price
FROM Products
WHERE vend_id  IN ('DLL01','BRS01')
ORDER BY prod_name;


The SELECT statement retrieves all products made by vendor DLL01 and vendor BRS01. The IN operator is followed by a comma-delimited list of valid values, and the entire list must be enclosed within parentheses. If you are thinking that the IN operator accomplishes the same goal as OR, you are right.


IN A keyword used in a WHERE clause to specify a list of values to be matched using an OR comparison.


NOT A keyword used in a WHERE clause to negate a condition.


The following example demonstrates the use of NOT. To list the products made by all vendors except vendor DLL01, you can write the following: SELECT prod_name
FROM Products
WHERE NOT vend_id  = 'DLL01'
ORDER BY prod_name;


Wildcards Special characters used to match parts of a value. Search pattern A search condition made up of literal text, wildcard characters, or any combination of the two.


To use wildcards in search clauses, the LIKE operator must be used.


The most frequently used wildcard is the percent sign (%). Within a search string, % means match any number of occurrences of any character. For example, to find all products that start with the word Fish, you can issue the following SELECT statement: SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE 'Fish%';


Case-Sensitivity Depending on your DBMS and how it is configured, searches might be case-sensitive, in which case 'fish%' would not match Fish bean bag toy.


Wildcards can be used anywhere within the search pattern, and multiple wildcards can be used as well. The following example uses two wildcards, one at either end of the pattern: SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE '%bean bag%';


Another useful wildcard is the underscore (_). The underscore is used just like %, but instead of matching multiple characters, the underscore matches just a single character. Microsoft Access Wildcards If you are using Microsoft Access, you might need to use ? instead of _. Take a look at this example: SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE '__ inch teddy bear';


BR02        12 inch teddy bear
BR03        18 inch teddy bear


Unlike %, which can match zero characters, _ always matches one character—no more and no less.


The brackets ([]) wildcard is used to specify a set of characters, any one of which must match a character in the specified position


For example, to find all contacts whose names begin with the letter J or the letter M, you can do the following: SELECT cust_contact


For example, to find all contacts whose names begin with the letter J or the letter M, you can do the following: SELECT cust_contact
FROM Customers
WHERE cust_contact LIKE '[JM]%'
ORDER BY cust_contact;


This wildcard can be negated by prefixing the characters with ^ (the carat character). For example, the following matches any contact name that does not begin with the letter J or the letter M (the opposite of the previous example): SELECT cust_contact
FROM Customers
WHERE cust_contact LIKE '[^JM]%'
ORDER BY cust_contact;


Of course, you can accomplish the same result using the NOT operator. The only advantage of ^ is that it can simplify the syntax if you are using multiple WHERE clauses: SELECT cust_contact
FROM Customers
WHERE NOT cust_contact LIKE '[JM]%'
ORDER BY cust_contact;


As you can see, SQL's wildcards are extremely powerful. But that power comes with a price: Wildcard searches typically take far longer to process than any other search types discussed previously.
