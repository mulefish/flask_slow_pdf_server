
# Might or might not be needed on your setup. My virtual:  
ENV  
python3 -m venv env  
cd env/bin  
source  activate   
pip3 install -r requirement.txt  


# Endpoints: 
http://localhost:5000/really_slow?pause=10 <-- pause 10 seconds   
http://localhost:5000/really_slow?pause=2 <-- pause 2 seconds  
http://localhost:5000/really_slow?pause=0 <-- pause 0 seconds  
http://localhost:5000/really_slow <-- pause 0 seconds  
http://localhost:5000/ <-- Mini about  





