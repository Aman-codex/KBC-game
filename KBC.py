questions =[
    [
         "Q1.Which technology has the potential to revolutionize fields like cryptography and drug discovery?",
          "Blockchain",
          " Quantum Computing",
           " Edge Computing",
            "Artificial Intelligence",  2 
    ],
    [
        "Q2.Which of the following is considered a sustainable energy technology?",
        "Quantum cmputing",
        "Blockchain",
        "solar and wind energy",
        "Artificial intlligence",3
    ],
    [
        "Q3.What is the primary application of blockchain technology beyond cryptocurrency?",
        "Virtual reality development",
        "Secure and transparent transactions in various industries",
        " Autonomous driving control systems",
        " Data storage in quantum computers",2
    ],
    [
        "Q4.Generative AI, like OpenAI’s DALL-E, is used to:-",
        "Generate cryptocurrency",
        "Generate art, code, and other content from prompts",
        "Build quantum algorithms",
        "Control autonomous vehicles",2
    ],
    [
      "Q5.The term “Metaverse” refers to:",
      "A system for quantum data transmission",
      "A virtual and augmented reality-based interconnected virtual world",
      "A blockchain-based financial ecosystem",
      "A new protocol for high-speed internet",2 
    ],
    [
        "Q6.Which of the following companies is working on the development of quantum computing technology?",
        "Meta",
        "Google",
        "Tesla",
        "Waymo",2
    ],
    [
      "Q7.CRISPR technology is primarily used in which of the following fields?",
      "Artificial Intelligence",
      " Quantum Computing",
      "Genetic Editing",
      "Virtual Reality",3   
    ],
    [
      "Q8.What is the main goal of 6G technology that differentiates it from 5G?",
      "Improved cloud storage capabilities",
      " Faster internet speed and more ubiquitous wireless connectivity",
      "Higher battery efficiency",
      "Enhanced voice recognition accuracy",2  
    ],
    [
       "Q9.Which of the following technologies is primarily associated with the development of self-driving cars?",
       " Blockchain",
       " Autonomous Vehicles",
       " Edge Computing",
       "Quantum Computing",2 
    ],
    [
       "Q10.What is the primary benefit of edge computing compared to cloud computing?",
       "Increased power consumption",
       " Slower data processing",
       "Faster data processing and reduced latency",
       "Higher dependency on central servers",3 
    ]
    
]

levels =[500,1000,2000,4000,8000,16000,32000,64000,128000,512000]

for i in range(0, len(questions)):
    question = questions[i]

    print(f"\nquestion for rs.{levels[i]}")
    print(question[0])
    print(f"a.{question[1]}                   b.{question[2]}")
    print(f"c.{question[3]}                  d.{question[4]}")
    reply = int(input("enter your ans:-(1-4)"))
    if(reply == question[-1]):
        print(f"\ncorrect answer,you won rs.{levels[i]}")
        if( i ==4):
            money =8000
        elif(i == 9):
                money =128000
        else:
            continue
    else:
        print("wrong ans")
        break