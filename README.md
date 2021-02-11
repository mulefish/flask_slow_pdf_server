
# code.py change
There is an absolute path in code.py. Change it to match your situation. 

 

# setup ( on my macos ) : windows or linux will be different
ENV  
python3 -m venv env  
cd env/bin  
source  activate   
DEPS    
pip3 install flask  
pip3 install flask-cors
pip3 install -r requirements.t 
pip3 freeze > requirements.txt  
pip3 install -r requirement.txt  


# Endpoints: 
http://localhost:5000/really_slow?pause=10 <-- pause 10 seconds   
http://localhost:5000/really_slow?pause=2 <-- pause 2 seconds  
http://localhost:5000/really_slow?pause=0 <-- pause 0 seconds  
http://localhost:5000/really_slow <-- pause 0 seconds  
http://localhost:5000/ <-- Mini about  





