## FACEBOOK API
1. Install requirements.txt

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
    
5. Views
    * index - Renders a simple string. The application is running on http://127.0.0.1:8000/ then , response will be "Hello There !!!. You  are running your application."
   
