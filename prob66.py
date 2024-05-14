# Pset 4, Problem 66
class Dfa:
    def __init__(self, state_space, alphabet, start_state, final_state, delta_fct):
        self.state_space = state_space
        self.alphabet = alphabet
        self.start_state = start_state
        self.final_state = final_state
        self.delta_fct = delta_fct

    def path_tr(self, state, letter):
        return self.delta_fct[state + letter]

    def is_accepted(self, string):
        current_state = self.start_state
        for index, letter in enumerate(string):
            # print(current_state + letter)
            current_state = self.delta_fct[current_state + letter]

        if current_state in self.final_state:
            return True
        else:
            return False


    def lang(self, length):
        lang = set(()) 
        
        for letter in self.alphabet:
                lang.add(letter)
        for idx in range(length - 1):
            temp_lang = set(())
            for word in lang:
                for letter in self.alphabet:
                    temp_lang.add(word + letter)
            lang.update(temp_lang)


        temp_lang = lang.copy()
        for word in temp_lang:
            if not self.is_accepted(word):
                lang.remove(word)
        return sorted(lang)
    
    def regex(self, current_state=None):
        if current_state == None:
            current_state = self.start_state
        system = {}
        for state in self.state_space:
            system[state] = ""
        for state in self.state_space:
            if state in self.final_state:
                system[state] = "#" # note # is the empty word (like one)
            else:
                system[state] = "&" # & is empty set (like zero)
            star_wrap = None
            for char in self.alphabet:
                path_to = self.delta_fct[f"{state}{char}"]
                if path_to != state:
                    system[state] += f"+{path_to}{char}"
                else:
                    star_wrap = char

            system[state] = f"{star_wrap}*({system[state]})"


        final_eq = system[self.start_state]
        true = True
        post_state_space = self.state_space.copy()
        post_state_space.remove(self.start_state)
        while true == True:
            true = False

            # step 1, put Q_0 in terms of only Q_0
            for post_state in post_state_space:
                print("0 =",final_eq)
                if post_state in final_eq:
                    true = True
                    final_eq = final_eq.replace(post_state, system[post_state])
                    # # distribute as replacing states, (easier during only step 1, may have to be done only in step 2)
                    # if "(" in final_eq:
                    #     wrapped = final_eq[final_eq.find("(")+1:-2]
                    #     distribute = final_eq[:final_eq.find("(")]
                    #     final_eq = f"{distribute}{wrapped}"
                    
                    

            #step 2, distribute for any ()
                
                

            # step 3 isolate Q_0


            # solve final s = t + rs, s = Q_0

            

                    
                

            



        print(system)
                
        
    




            

A2_Qspace = ["0", "1", "2"]
A2_alphabet = ['a', 'b']
A2_delta = {"0a": "0", "0b": "1", "1a": "1", "1b": "2", "2a": "2", "2b": "0"}
A2_final = ["0", "2"]
A2_start_state = "0"
A2 = Dfa(A2_Qspace, A2_alphabet, A2_start_state, A2_final, A2_delta)

# print(A2.is_accepted("aab"))
A2.regex()
