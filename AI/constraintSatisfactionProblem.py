colors=['red','green','blue']
states=['WA','NT','SA','Q','NSW','V']
neighbors={
    "WA":["NT","SA"],
    "NT":["WA","SA",'Q'],
    "SA":["WA",'NT','Q',"NSW",'V'],
    "Q":['NT',"NSW","SA"],
    "NSW":['Q',"SA",'V'],
    "V":["SA","NSW"]
}
colors_of_states={}
def promising(state,color):
    for neighbor in neighbors.get(state):
        colors_of_neighbors=colors_of_states.get(neighbor)
        if colors_of_neighbors==color:
            return False
    return True

def backtrack(state_index):
    if state_index==len(states):  # base case : if all the state are color then return true
        return True
    
    state=states[state_index]
    for color in colors:
        if promising(state,color):  #if the color is promissing safe
            colors_of_states[state]=color  #assign it to the state
            if backtrack(state_index+1):  # move to the next set recurcively
                return True
            colors_of_states[state]=None  
            # if no solution is satisfy the condition then undo color and try another color
    return False

def main():
    if backtrack(0):
        print(colors_of_states)
    else:
        print("No solution found")
main()
