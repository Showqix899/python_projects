q1=["Messi","Ro1naldo","Pele","Maradona",1]
Q1="Who is the Greatest of all ?"
q2=["Germany","Natherland","Brazil","Argentina",4]
Q2="Who won the Fifa world cup 1978 ?"
q3=["messi","ronaldo","ronaldinho","Cruef",1]
Q3="Who won the most ballon d'or ?"
question=[Q1,Q2,Q3]
options=[q1,q2,q3]
for i in range(len(question)):
    print(question[i])
    getop=options[i]
    
    for j in range(len(getop)-1):
        print(getop[j])
    a=int(input("ans: "))
    if getop[-1]==a:
        print("Right")
    else: 
        print("wrong")
        
    
    
    
        
    
    