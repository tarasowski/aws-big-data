# Generation of sample data

1. Setup an Ec2 machine with 100gb storage
2. `sudo yum install make git`
3. `git clone https://github.com/gregrahn/tpch-kit` 
4. `cd tpch-kit/dbget`
5. `sudo yum install gcc`
6. `make OS=LINUX`

## Create data for emr

7. `cd $HOME && mkdir emrdata` 
8. `export DSS_PATH=$HOME/emrdata`  
9. `cd tpch-kit/dbgen && ./dbgen -v -T o -s 10` (run dbgen in verbose mode, -T
   specified the table, we're using o for orders / line orders table, -s 10 gb
   data size)  
10. `aws s3api create-bucket --bucket bigdatalabdt` 
11. `aws s3 cp $HOME/emrdata s3://bigdatalabdt/emrdata --recursive` 

## Create data for redshift

12. `cd $HOME && mkdir redshiftdata`
13. `export DSS_PATH=$HOME/redshiftdata`
14. `cd tpch-kit/dbgen && ./dbgen -v -T o -s 40`
15. `cd $HOME/redshiftdata && wc -l orders.tbl`
16. `split -d -l 15000000 -a 4 orders.tbl orders.tlb.` - splitting the big file
    into 4 parts of 15M lines per file
16. `split -d -l 60000000 -a 4 lineitem.tbl lineitem.tbl.` - splitting the other
    big file into 4 parts of 60M lines per file
16. `rm orders.tlb && rm lineitem.tbl`
15. `aws s3 cp $HOME/redshiftdata s3://bigdatalabdt/redshiftdata --recursive`

