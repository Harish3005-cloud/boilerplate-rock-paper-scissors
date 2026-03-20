# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def make_paired_player(steps=3):
    pair_history = []
    play_order = {}
    
    def player(prev_play, dummy=[]):
        if not prev_play:
            prev_play = 'R'
            pair_history.clear()
            play_order.clear()
            
        if pair_history and len(pair_history[-1]) == 1:
            pair_history[-1] += prev_play
            
        if len(pair_history) >= steps + 1:
            context = "".join(pair_history[-(steps+1):-1])
            target = prev_play
            seq = context + target
            play_order[seq] = play_order.get(seq, 0) + 1
            
        if len(pair_history) >= steps:
            context = "".join(pair_history[-steps:])
            potential = {
                context + "R": play_order.get(context + "R", 0),
                context + "P": play_order.get(context + "P", 0),
                context + "S": play_order.get(context + "S", 0)
            }
            prediction = max(potential, key=potential.get)[-1:]
        else:
            prediction = "P" # Start by predicting the opponent will play R or whatever
            
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        my_move = ideal_response[prediction]
        
        pair_history.append(my_move)
        
        return my_move
    return player

player = make_paired_player(3)

if __name__ == "__main__":
    from RPS_game import play, mrugesh, abbey, quincy, kris
    for h in [2, 3, 4, 5]:
        print(f"\nHISTORY LEN {h} pairs")
        p = make_paired_player(h)
        play(p, quincy, 1000, verbose=False)
        play(p, abbey, 1000, verbose=False)
        play(p, kris, 1000, verbose=False)
        play(p, mrugesh, 1000, verbose=False)
