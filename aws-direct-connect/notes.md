# AWS Direct Connect

* A VPC is a logical isolated data center that lives in AWS in the cloud
* The VPC's live in geographic areas and we call the geographic areas regions
eu-central-1
* The regions consists of many physical data centers, AWS groups these data
centers into availability zones (AZ's)
* An availability zone maps the grouping of data centers in the geographic area
that are designed to overcome catastrophies
* Subnets/Route table are IP's 

* If you want to connect your on-premises data centers you need to configure a
virtual private gateway (VGW). It's a router that sits at the edge of your VPC.

* Around the world AWS have partners that provide co-location facilities. These
are referred as meet-me locations. AWS installs routers at these location that
acts as uplinks to the routers


![direct connect](../img/ce9-10-46-screenshot.png)
