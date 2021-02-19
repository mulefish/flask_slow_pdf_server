
# Might or might not be needed on your setup. My virtual:  
ENV  
python3 -m venv env  
cd env/bin  
source  activate   
pip3 install -r requirement.txt  


# # Endpoints: 
# Get a PDF 
curl --location --request GET 'localhost:4040/really_slow?pause=1' \  
--header 'Content-Type: application/json' \
--data-raw '{
    "loanId":"29292"
}'

# Pretend document server meta-info - this is a GET
curl --location --request GET 'localhost:4040/doc_hub_get' \
--header 'Content-Type: application/json' \
--data-raw '{
    "loanId":"29292"
}'

# Pretend document server meta-info - this is a POST - this has random load amounts
curl --location --request POST 'localhost:4040/doc_hub' \
--header 'Content-Type: application/json' \
--data-raw '{
    "loanId":"29292"
}'

# Pretend document server meta-info - this is a POST - this has NON random load amounts
curl --location --request POST 'localhost:4040/doc_hub' \
--header 'Content-Type: application/json' \
--data-raw '{
    "loanId":"29292",
    "forceCount":"the value here does not matter, only that the key exists"
}'

