Utilizes the BeautifulSoup module to send a GET request to a given site for HTML parsing  
Checks if the request was successful by verifying the status code (HTTP 200 OK)  
If successful, prints the text content of each paragraph  
If unsuccessful, prints an error message with the HTTP status code  
Most websites are built with methods to prevent web scraping and will give a 403 error when this program is run on them  
