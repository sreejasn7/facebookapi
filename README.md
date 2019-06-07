## FACEBOOK API
1. Install requirements.txt
2. Used Python 2.7 with Django 1.11

## FILES

1. Models 
   * MessengerUser , FacebookPage , FacebookLabel 
   * page : models.py
   
2. Serializers Used
   * UserSerializer
   * FacebookLabelSerializer
   * FacebookLabelRelatedSerializer
   * page : serializers.py
   
3. Pagination
   * LargeUserSetPagination - Used for Handling Large Bulk Data 
   * Page Size set to 2
   * This determines  actually max number of users configurable from API
   * page : pagination.py
   
 3. URls
    * Urls - set urls
    * PSID_list - Load all the PSID users from MessengerUser model
    * upload_csv - Upload CSV using MultiPartParser
    * upload_json - Upload JSON using JSONParser
    * PSID_page_map - Checks if a user and page exists together . This checking is done from table FacebookLabel
    * PSID_list_pages - This is the important link in the application. This shows the PSID users with labels and access token
        * It shows PSID users
        * It sends batch requests to FB at each pagination with the help of organize_bulk_fb_data and batch_mechanism_curl
      
    * page : urls.py
   
   
 4. LOGICS
    * These are the logical functions that are used. 
    * function - batch_mechanism_requests ,  is calling urls via python requests. This is not currently used in application
    * function - batch_mechanism_curl , is calling urls via python pycurl. This is the one used currently.
    * function -  organize_bulk_fb_data , is used to rearrange the data to post to fabebook
    * page : logics.py
    
5. Views
    * index - Renders a simple string. The application is running on http://127.0.0.1:8000/ then , response will be "Hello There !!!. You  are running your application."
    * UserList - Load all the PSID users from MessengerUser model
    * FileUploadCSV - Upload CSV using MultiPartParser
    * FileUploadJSON -  Upload JSON using JSONParser
    * PSIDPageMap -  Checks if a user and page exists together . This checking is done from table FacebookLabel
    * FacebookLabelPagination -This helps in fetching the users and adding the label to
them (assuming that label has already been fetched and saved. )
It uses the `list` function to get the paginated data and use the paginated data to send bulk requests.
    
    
## Work Flows
    * Upload PSID using either psid.json or psids.csv (these files are in the project main folder attached )by using the api urls upload_csv/ or upload_csv/. This will be saved to MessengerUser model.
    * Create some rough entries in FacebookPage. 
    * Map some users to pages in FacebookLabel. 
    * Try the functionality 
        * Assume there's an api for fetching the users by user id (psid) and page id. The response should contain a list of missing users (the user api will return None if user is not found) ||   URL is `PSID_page_map`
        * For associating labels, we need to use facebook batch api to send bulk requests (our api will allow a configurable max number of users). ||  URL is `PSID_list_pages`
        * The facebook batch mechanism needs to be reusable for other purposes. || Function is `batch_mechanism_curl`
        * There should be 2 versions of the api, one which takes a json and one which accepts a csv file upload (which will only contain lines with user ids). || Functions are `FileUploadCSV` & `FileUploadJSON`
        * How would you handle, if we need to support a very large number of users in the api? ||  By using Pagination and only sending requests to FB which resulted in paginated data. || Class used is `LargeUserSetPagination`
   
