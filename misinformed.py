from textblob import TextBlob

def subjectiveCount(text):

    blob = TextBlob(text)

    subjectiveCount = 0
    for sentence in blob.sentences:
        sub = sentence.sentiment.subjectivity
        if sub > 0.55:
            subjectiveCount += 1
            print("OPINION: `" + str(sentence) + "`")
    
    return subjectiveCount



