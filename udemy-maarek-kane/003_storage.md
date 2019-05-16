# Storage

### AWS S3 Overview - Buckets

* Amazon S3 allows people to store object (files) in "buckets" (directories)
* Buckets must have a globally unique name
* Buckets are defined at the region level
* Naming convention
  * No uppercase
  * No uderscore
  * 3 - 63 char long
  * Not an IP
  * Must start with lowercase letter or number

#### AWS S3 Overview - Objects

* Objects (files) have a Key. The key is the Full path:
  * <my_bucket>/my_file.txt
  * <my_bucket>/my_folder/another_folder/my_file.txt
* There's no concept of "directories" within buckets (although the UI will trick
  yo to think otherwise)
* Just keys with very long names that contain slashes ("/")
* Object Values are the content of the body:
  * Max size is 5 TB
  * If uploading more than 5GB, must use "multi-part upload"
* Metadata (list of text key / value pairs - system or user metadata)
* Tags (Unicode key / value pair - up to 10) - useful for security / lifecycle
* Version ID (if version is enabled)

#### AWS S3 - Consistency Model

* Read after write consistency for PUTS of new object. Means as soon as you
  write an object you can retreive it
    * As soon as an object is written, we can retrieve it e.g. (PUT 200 -> GET
      200)
    * This is true, expect if we did a GET before to see if the object existed
      e.g. GET 404 -> PUT 200 -> GET 404 - eventually consistent. The last GET
      404 comes form a result that the first time you tried to GET the object
      you've got 404 (you need to write 1-2 second)

* Eventual Consistency for DELETES and PUTS of existing objects
  * if we read an object after updating, we might get the older version e.g. PUT
    200 -> PUT 200 -> GET 200 (might be older version)
  * If we delete an object, we might still be able to retrieve it for a short
    time e.g. DELETE 200 -> GET 200
