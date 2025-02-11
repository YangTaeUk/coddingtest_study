def solution(babbling):
    answer = 0
    for text in babbling:
        num = 0
        text = text.replace("aya"," ").replace("ye"," ").replace("woo"," ").replace("ma"," ")
        if len(text.replace(" ","")) == 0: answer += 1

    return answer


babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
print (solution(babbling));
