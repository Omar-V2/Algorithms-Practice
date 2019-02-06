def yelp(reviews, topics):
    ans = {}
    for review in reviews:
        newstr = ""
        for char in review:
            newstr += char.lower()
        for topic in topics:
            for word in topics[topic]:
                if word in newstr:
                    if topic in ans:
                        ans[topic] += 1
                    else:
                        ans[topic] = 1
    return ans

review = ["a", "b"]
topics = {"Business": ["a", "b", "c"]}
ans = yelp(review, topics)
print(ans)

        
