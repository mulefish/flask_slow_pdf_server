
# code.py change
There is an absolute path is code.py. Change it to match your situation. 

 

# I used a virutal env to setup flask on my macos setup ( on my macos ) : windows or linux will be different. If you do not need a virtual... skip this step
ENV  
python3 -m venv env  
cd env/bin  
source  activate   
DEPS    
pip3 install flask  
pip3 freeze > requirements.txt  
pip3 install -r requirement.txt  

# Endpoints: 
http://localhost:5000/really_slow?pause=10 <-- pause 10 seconds   
http://localhost:5000/really_slow?pause=2 <-- pause 2 seconds  
http://localhost:5000/really_slow?pause=0 <-- pause 0 seconds  
http://localhost:5000/really_slow <-- pause 0 seconds  
http://localhost:5000/ <-- Mini about  





