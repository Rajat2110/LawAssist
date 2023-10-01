# nlu_data = {
#     "greet": ["hello", "hi", "hey"],
#     "goodbye": ["goodbye", "bye", "see you"],
#     # Add more intents and training phrases as needed
# }



nlu_data = {
    "greet": [
        "hello",
        "hello there",
        "hi",
        "good day",
        "hey",
        "what's up",
        "how do you do",
        "greetings"
    ],
    "goodbye": [
        "goodbye",
        "farewell",
        "see you later"
    ],
    "ask_legal_advice_general": [
        "can you provide me with general legal advice on tenant rights",
        "how can i understand my legal obligations as an employer",
        "explain the legal steps involved in filing for bankruptcy",
        "what are the rights of consumers under consumer protection laws",
        "general",
        "general legal advice"
        # "employer",
        # "bankruptcy",
        # "rights of consumer",
        # "consumer",
        # "tenant"
    ],
    "ask_contract_law": [
        "tell me about the essential elements of a valid contract",
        "explain the concept of consideration in contract law",
        "how can i draft a legally binding business contract",
        "what is the statute of frauds in contract law",
        "valid contract",
        "contract",
        "contract law",
        "frauds"
    ],
    "ask_family_law": [
        "what factors does the court consider in child custody cases?",
        "explain the legal process of adoption.",
        "how does divorce mediation work in family law?",
        "can you clarify the legal rights of grandparents in visitation matters?",
        "child custody",
        "adoption",
        "family"
    ],
    "ask_criminal_law": [
        "explain the process of a criminal trial.",
        "what are the legal defenses against assault charges?",
        "tell me about plea bargains in criminal law.",
        "how are juvenile offenders treated under criminal law?",
        "criminal",
        "juvenile",
        "plea",
        "bargain",
        "assault"
    ],
    "ask_property_law": [
        "explain adverse possession in property law.",
        "what is the legal process for buying commercial real estate?",
        "tell me about real estate zoning laws.",
        "how are property disputes resolved in court?",
        "property"
    ],
    "ask_immigration_law": [
        "how to apply for an h1-b visa?",
        "explain the legal requirements for family-sponsored immigration.",
        "what are the steps for obtaining a green card?",
        "how to challenge a deportation order legally?",
        "immigration",
        "green card",
        "deportation"
    ],
    "ask_personal_injury_law": [
        "what qualifies as a personal injury under the law?",
        "explain the legal process for filing a medical malpractice lawsuit.",
        "how are damages calculated in personal injury cases?",
        "legal rights of victims in a car accident case.",
        "injury",
        "car accident",
        "malpractice",
        "medical",
        "medical lawsuit"
    ],
    "ask_human_rights_law": [
        "what are the international human rights treaties?",
        "explain the legal protections against discrimination based on gender.",
        "tell me about legal actions against human trafficking.",
        "human rights in the context of refugee and asylum seekers.",
        "human rights",
        "human trafficking",
        "gender dicrimination",
        "discrimination on the basis of gender",
        "discrimination on gender",
        "discrimination based on gender",
        "refugee",
        "asylum seeker"
    ],
    "ask_intellectual_property_law": [
        "how to patent a software invention?",
        "explain the legal process for trademark registration.",
        "what constitutes copyright infringement under the law?",
        "legal remedies for trade secret misappropriation.",
        "patent",
        "property",
        "trade",
        "copyright",
        
    ],
    "ask_contract_disputes": [
        "how are contract disputes resolved in court?",
        "explain the legal concept of anticipatory breach of contract.",
        "what are the remedies for breach of a construction contract?",
        "legalities of contract termination in business partnerships.",
        "resolved",
        "breach",
        "construction",
        "partnerships",
        "agreement"
        
    ],
    "ask_labor_law": [
        "explain the legal rights of employees regarding workplace safety.",
        "what is the legal process for collective bargaining in labor unions?",
        "how are wage and hour disputes resolved under labor law?",
        "legal protections for whistleblowers in the workplace.",
        "workplace",
        "bargaining",
        "wage",
        "labor",
        "whistleblower",
        "protection"
    ],
    "ask_divorce_law": [
        "how is property division handled in divorce cases?",
        "explain the legal requirements for a no-fault divorce.",
        "what factors are considered in child custody decisions?",
        "legal process for spousal support and alimony.",
        "division",
        "divorce",
        "custody",
        "spousal support",
        "alimony"
        
    ],
    "ask_immigration_status": [
        "how to check my immigration application status?",
        "explain the legal process for changing immigration status.",
        "what documents are required to prove immigration status?",
        "legal steps for obtaining a work visa.",
        "immigration",
        "prove",
        "work"
    ],
    "ask_patent_law": [
        "explain the patent application process.",
        "what is patent infringement under intellectual property law?",
        "how long does a patent last?",
        "legal steps to challenge a granted patent.",
        "intellectual",
        "patent",
        "challenge"
    ],
    "ask_medical_malpractice": [
        "what constitutes medical malpractice?",
        "explain the legal process for medical negligence cases.",
        "how are damages calculated in medical malpractice lawsuits?",
        "legal rights of patients in surgical malpractice cases.",
        "medical",
        "malpractice",
        "lawsuits",
        "surgical"
    ],
    "ask_environmental_regulations": [
        "how are environmental regulations enforced?",
        "legal obligations of businesses under environmental laws.",
        "explain the clean air act and its legal implications.",
        "legal consequences for violating environmental regulations.",
        "enforced",
        "obligations",
        "violating",
        "environmental"
    ],
    "ask_employment_discrimination": [
        "what constitutes workplace discrimination?",
        "explain legal protections against racial discrimination at work.",
        "how to file a complaint for gender-based discrimination?",
        "legal rights of employees in cases of age discrimination.",
        "descrimination",
        "racial",
        "gender-based",
        "discrimination"
    ],
    "ask_international_trade_law": [
        "explain international trade agreements.",
        "legal process for resolving trade disputes between nations.",
        "how are tariffs and trade restrictions regulated internationally?",
        "legal implications of breaching international trade agreements.",
        "trade",
        "nations",
        "tariffs",
        "internationally"
    ],
    "ask_internet_privacy": [
        "what are the legal aspects of online privacy?",
        "explain the gdpr and its impact on internet privacy.",
        "legal rights of individuals regarding data breaches.",
        "how do social media platforms handle user privacy legally?",
        "online",
        "gdpr",
        "data breaches",
        "social media"
    ],
    "ask_human_trafficking_law": [
        "legal definitions of human trafficking.",
        "how are traffickers prosecuted under human trafficking laws?",
        "legal protections for trafficking victims.",
        "international efforts to combat human trafficking.",
        "trafficking",
        "prosecuted",
        "victims",
        "combact"
    ],
    "ask_construction_law": [
        "explain construction contracts and legal obligations.",
        "how are construction defects handled legally?",
        "legal process for resolving disputes in construction projects.",
        "construction permits and regulatory compliance.",
        "obligations",
        "defects",
        "constructive",
        "regulatory"
    ],
    "ask_tax_law": [
        "explain tax deductions for small businesses.",
        "legal obligations of taxpayers under tax laws.",
        "how are tax disputes resolved with the irs?",
        "tax implications of cryptocurrency transactions.",
        "deduction",
        "taxpayer",
        "cryptocurrency"
    ],
    "ask_insurance_law": [
        "legal requirements for insurance policies.",
        "how are insurance claims investigated legally?",
        "legal rights of policyholders in insurance disputes.",
        "insurance fraud and its legal consequences.",
        "polices",
        "investigated",
        "policyholder",
        "insurance"
    ],
    "ask_admiralty_law": [
        "explain admiralty and maritime law.",
        "maritime",
        "legal aspects of ship collisions and salvage operations.",
        "how are maritime pollution cases handled legally?",
        "legal rights of seafarers and shipowners",
        "admiralty",
        # "maritime",
        "collision",
        "seafare",
        "shipowners"
    ],
    "provide_feedback": [
        "the chatbot's expertise in maritime law was impressive.",
        "thanks for the detailed information on tax law.",
        "the legal advice on internet privacy was valuable.",
        "i appreciate the insights into international trade law.",
        "impressive",
        "information",
        "valuable",
        "appreciate"
    ],
    
    "About_Me": [
        "tell me about yourself",
        "tell me about who are you",
        "who are you",
        "what are you",
        "about you"
    ]
}


# response_data = {
#     "greet": ["Hello there!", "Hi! How can I assist you today?", "Greetings! What can I help you with?"],
#     "goodbye": ["Goodbye! If you have more questions, feel free to ask.", "Farewell! Reach out anytime you need assistance.",
#                 "See you later! Take care and have a great day!"],
#     # Add more intent-response pairs corresponding to your intents
# }

response_data = {
    "greet": [
        "hello! how can i assist you?",
        "hi there! how can i help?",
        "greetings! what legal information do you need?"
    ],
    "goodbye": [
        "goodbye! if you have more questions, feel free to ask.",
        "farewell! reach out anytime you need legal guidance.",
        "see you later! take care and stay legally informed."
    ],
    "ask_legal_advice_general": [
        '''Tenants have the right to pay a fair rent. 
        The owner cannot charge any amount of rent. 
        The rent needs to be decided according to market rates and the value of the property. 
        Any increase in rent must be in line with the hike agreed upon in the rental agreement.
        
        '''
    ],
    "ask_contract_law": [
        '''Contract law is the legal body that encompasses both the origination, enforcement and ultimate enactment of all legal contracts or agreements.
        All those who engage in business transactions, at some point or another, engage in contract law. 
        Companies and consumers alike use contracts in their everyday actions.
        '''
    ],
    "ask_family_law": [
        '''family law, body of law regulating family relationships, including marriage and divorce, 
        the treatment of children, and related economic matters.
        Family law shares an interest in certain social issues with other areas of law, including criminal law.'''
    ],
    "ask_criminal_law": [
        '''
        Criminal law is an area of the law that concerns crimes and laws applied to those who commit them.
        There are two main types of criminal law offenses: felonies and misdemeanors. 
        The most serious crimes are felonies, which include offenses like murder, robbery, and arson.
        
        '''
    ],
    "ask_property_law": [
        '''
        property law, principles, policies, and rules by which disputes over property are to be resolved and by which property transactions may be structured. 
        What distinguishes property law from other kinds of law is that property law deals with the relationships between and among members of a society with respect to “things.”
        Property law is best understood as the complex of jural relationships between and between persons with respect to things. 
        '''
    ],
    "ask_immigration_law": [
        '''
        Immigration law includes the national statutes, regulations, and legal precedents governing immigration into and deportation from a country.
        Strictly speaking, it is distinct from other matters such as naturalization and citizenship, although they are sometimes conflated.
        Immigration Law is the law which exclusively governs immigration in a nation. 
        Immigration law refers to the rules established by the concerned government of a country for determining who is allowed to enter their country, and for how long.
        
        
        '''
    ],
    "ask_personal_injury_law": [
        '''
        Personal Injury law is a branch of tort law that deals with the subject of providing compensation to individuals who have suffered any physical, 
        psychological or emotional injury due to the negligence of some individual.
        It is a broad area of law that includes everything from car accidents and slip and fall accidents to defamation and malicious prosecution.
        If you have been injured as a result of the negligence of another party, you may be able to file a personal injury lawsuit to recover damages.
        '''
    ],
    "ask_human_rights_law": [
        '''
        Human rights include the right to life and liberty, freedom from slavery and torture, freedom of opinion and expression, the right to work and education, and many more. 
        Everyone is entitled to these rights, without discrimination.
        This declaration consists of 30 articles affirming an individual's rights. 
        Those 30 articles currently known as 30 universal declaration of human rights or 30 basic human rights, 
        including rights to life, rights to education, rights to organize and rights to treated fair among others things.
                
        '''
    ],
    "ask_intellectual_property_law": [
      '''
      
      Intellectual property rights (IPR) refers to the legal rights given to the inventor or creator to protect his invention or creation for a certain period of time.
      These legal rights confer an exclusive right to the inventor/creator or his assignee to fully utilize his invention/creation for a given period of time.
      Patents, trademarks, copyrights, and trade secrets are valuable assets of the company and understanding how they work 
      and how they are created is critical to knowing how to protect them.
      
      '''
    ],
    "ask_contract_disputes": [
        '''
        Contract disputes occur when one or both parties to an agreement disagree about the terms and conditions. 
        A contract is only valid when both parties fully understand the agreement and are willing to accept its terms.
        If the agreement is not mutual, it may be challenged in court.
        
        
        '''
    ],
    "ask_labor_law": [
        '''
        Labor law is legislation specifying responsibilities and rights in employment, particularly the responsibilities of the employer and the rights of the employee.
        The four labour codes -- the Code on Wages, Industrial Relations Code, 
        Social Security Code and the Occupational Safety, Health and Working Conditions Code -- are set to replace 29 labour laws.
        
        
        '''
    ],
    "ask_divorce_law": [
        '''
        Divorce can be granted on several grounds, including adultery, cruelty, desertion, conversion, mental disorder, venereal disease, and irretrievable breakdown of marriage. 
        The district court where the couple last resided together has jurisdiction over divorce cases.
        A divorce is a formal ending of a marriage. 
        It's more permanent than a separation and involves a legal process. If you get a divorce, that means the marriage is officially over.
        Divorce has both a noun and a verb form.
        
        '''
    ],
    "ask_immigration_status": [
       '''
       Immigration status refers to the way in which a person is present in the United States.  Everyone has an immigration status. Some examples of immigration status include:

US citizen 
Family petitions
Employer petitions
Violence Against Women Act self-petitions (of any gender)
       
       
       '''
    ],
    "ask_patent_law": [
        '''
        
        They also protect intellectual property.
        When an inventor obtains a patent, they secure the right to exclude others from using, making and selling their product or method of use for 20 years, 
        while maintaining the right to sell the item exclusively and for a higher price.
        
        
        '''
    ],
    "ask_medical_malpractice": [
       '''
       A person, who holds himself out ready to give medical advice and treatment, impliedly undertakes that he is possessed of skill or knowledge for the purpose, such person when consulted by a patient owes him certain duties. 
       A breach of these duties gives a right of action for negligence to the patient.
       for more info visit: https://www.legalserviceindia.com/article/l8-Medical-malpractice.html#:~:text=A%20person%2C%20who%20holds%20himself,for%20negligence%20to%20the%20patient.
       '''
    ],
    
    "ask_international_trade_law": [
        '''
        
        International Trade Law is an aggregate of legal rules of "international legislation" and new lex mercatoria, regulating relations in international trade.
        "International legislation" – international treaties and acts of international intergovernmental organizations regulating relations in international trade.
        Generally, international trade law includes the rules and customs governing trade between countries. 
        International trade lawyers may focus on applying domestic laws to international trade, and applying treaty-based international law governing trade.
        '''
    ],
    
    "ask_human_trafficking_law": [
        '''
        
        Trafficking in Human Beings or Persons is prohibited under the Constitution of India under Article 23 (1)
        The Immoral Traffic (Prevention) Act, 1956 (ITPA) is the premier legislation for prevention of trafficking for commercial sexual exploitation.
        human trafficking, also called trafficking in persons, form of modern-day slavery involving the illegal transport of individuals by force or deception for the purpose of labour, sexual exploitation, or activities in which others benefit financially.
        
        '''
    ],
    
    "ask_tax_law": [
    '''
    
    tax law, body of rules under which a public authority has a claim on taxpayers, requiring them to transfer to the authority part of their income or property. 
    The power to impose taxes is generally recognized as a right of governments.
    Tax law falls within the domain of public law—i.e., the rules that determine and limit the activities and reciprocal interests of the political community and the members composing it—as distinguished from relationships between individuals (the sphere of private law).
    for more details visit: https://www.britannica.com/money/topic/tax-law
    '''
    ],
    "ask_insurance_law": [
        
        '''
        `Insurance` is an arrangement by which a company or the State undertakes to provide a guarantee of compensation for specified loss, damage, illness, or death in return for payment of a specified premium.
        Insurance is a means of protection from financial loss. 
        It is a form of risk management primarily used to hedge against the risk of a contingent, uncertain loss.
        
        '''
        
    ],
    
    "provide_feedback": [
        "Thankyou for your feedback.",
        "thanks for the detailed information on tax law.",
        "the legal advice on internet privacy was valuable."
    ],
    "About_Me": [
        "I am a legal assistant chatbot.",
        "thanks for the detailed information on tax law.",
        "the legal advice on internet privacy was valuable."
    ],
    
    
}


# def get_intent(user_input):
#     # Check user input against training phrases for each intent
#     for intent, phrases in nlu_data.items():
#         for phrase in phrases:
#             if phrase in user_input.lower():
#                 return intent
#     return None

# def chatbot_response(user_input):
#     intent = get_intent(user_input)
#     if intent:
#         responses = response_data.get(intent, ["I'm not sure how to respond to that."])
#         return responses
#     else:
#         return ["I'm sorry, I didn't understand your question. Can you please rephrase it?"]

# # Example usage
# while True:
#     user_input = input("User: ")
#     if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
#         print("Chatbot: Goodbye! Have a great day!")
#         break
#     responses = chatbot_response(user_input)
#     print("Chatbot:", responses[0])  # Print the first response for simplicity

def get_intent(user_input):
    # Check if any keyword in the user input matches a training phrase for an intent
    for intent, keywords in nlu_data.items():
        if any(keyword in user_input.lower() for keyword in keywords):
            return intent
    return None

def chatbot_response(user_input):
    intent = get_intent(user_input)
    if intent:
        responses = response_data.get(intent, ["I'm not sure how to respond to that."])
        return responses
    else:
        return ["I'm sorry, I didn't understand your question. Can you please rephrase it?"]

# Example usage
def cbt(user_input):
    if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
        print("Chatbot: Goodbye! Have a great day!")
    responses = chatbot_response(user_input)
    print("Chatbot:", responses[0])  # Print the first response for simplicity
