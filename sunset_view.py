def sunset_view(buildings):
    stack = [buildings[0]]
    for i in range(1, len(buildings)):
        # if buildings[i] < stack[-1]:
        #     stack.append(buildings[i])
        # else:
        while stack and buildings[i] >= stack[-1]:
            stack.pop()
        stack.append(buildings[i])
    return stack

def sunset_view2(buildings):
    biggest = None
    ans = []
    for building in buildings:
        if building > biggest or not building:
            ans.append(building)
        biggest = max(building, biggest)
    return ans

buildings = [2, 3, 4, 5]
# buildings.reverse()
print(sunset_view2(buildings))
# print(sunset_view(buildings))

