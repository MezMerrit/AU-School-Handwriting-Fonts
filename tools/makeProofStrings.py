
UC = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
UC2 = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

lc = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
lc2 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

punct = [ '.', ':', ';', '¡', '!', '¿', '?', '*', '-', '–', '—', '_', '(', ')', '{', '}', '[', ']', '"', "'", '@', '&' ]

N = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
N2 = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

def makeProofString ( list1, list2, prefix, sufix ):

    parapgraph = ''

    for g in list1:
        for g2 in list2:
            parapgraph += prefix + g + g2 + sufix
        parapgraph += '\n\n'
    return parapgraph 
    

UC_x_UC_string = makeProofString(UC, UC2, '', '')
print( UC_x_UC_string )

lc_x_lc_string = makeProofString(lc, lc2, '', '')
print( lc_x_lc_string )

UC_x_lc_string = makeProofString(UC, lc, 'H', 'n ')
print( UC_x_lc_string )

UC_x_punct = makeProofString(UC, punct, '', '')
print( UC_x_punct )

lc_x_punct = makeProofString(lc, punct, '', '')
print( lc_x_punct )

N_x_N_string = makeProofString(N, N2, '', '')
print( N_x_N_string )

N_x_punct = makeProofString(N, punct, '', '')
print( N_x_punct )

N_x_UC_string = makeProofString(N, UC2, '', '')
print( N_x_UC_string )

N_x_lc_string = makeProofString(N, lc2, '', '')
print( N_x_lc_string )
