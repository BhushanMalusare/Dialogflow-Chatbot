import re

def extract_session_id(session_str:str):
    match = re.search(r"/sessions/(.*?)/contexts/",session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    
    return ""

def get_str_from_dict(food_dict:dict):
    return ", ".join([f"{int(value)} {key}" for key,value in food_dict.items()])


#if __name__ == "__main__":
    #print( get_str_from_dict({"samosa": 2, "chhole": 5}))
    #print(extract_session_id("projects/eatery-chatbot-xkru/agent/sessions/005b1366-2fb5-5d62-7f3c-f15a14ecbd3d/contexts/ongoing-order"))